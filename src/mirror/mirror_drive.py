"""
Google Drive Mirror

Mirror knowledge base to Google Drive.
"""

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class DriveMirror:
    """
    Mirror knowledge files to Google Drive.
    
    Supports:
    - Creating folder structure
    - Uploading new files
    - Updating existing files
    - File ID tracking
    
    Usage:
        mirror = DriveMirror(folder_id="abc123")
        result = mirror.sync(source_dir=Path("~/.pai/knowledge"))
    """
    
    def __init__(self, folder_id: Optional[str] = None):
        """
        Initialize Drive mirror.
        
        Args:
            folder_id: Target folder ID (None = root)
        """
        self.folder_id = folder_id
        self._drive = None
        self._file_map: Dict[str, str] = {}  # path -> file_id
    
    @property
    def drive(self):
        """Lazy-load Drive client."""
        if self._drive is None:
            from google.drive.client import GoogleDriveClient
            self._drive = GoogleDriveClient()
        return self._drive
    
    def sync(
        self,
        source_dir: Path,
        create_root_folder: bool = True
    ) -> Dict[str, Any]:
        """
        Sync knowledge files to Drive.
        
        Args:
            source_dir: Source directory to mirror
            create_root_folder: Create a root folder for this mirror
            
        Returns:
            Sync result with stats
        """
        logger.info(f"Syncing {source_dir} to Google Drive")
        
        if not source_dir.exists():
            return {"success": False, "error": f"Source not found: {source_dir}"}
        
        stats = {
            "success": True,
            "files_uploaded": 0,
            "files_updated": 0,
            "folders_created": 0,
            "errors": 0,
        }
        
        # Create root folder if needed
        root_folder_id = self.folder_id
        if create_root_folder and not root_folder_id:
            root_folder_id = self._create_folder(
                f"PAI-Knowledge-{datetime.now().strftime('%Y%m%d')}"
            )
            stats["root_folder_id"] = root_folder_id
        
        # Process files
        for item in source_dir.rglob("*"):
            if item.is_file():
                relative = item.relative_to(source_dir)
                
                # Skip hidden files
                if any(part.startswith(".") for part in relative.parts):
                    continue
                
                try:
                    self._upload_file(item, relative, root_folder_id)
                    stats["files_uploaded"] += 1
                except Exception as e:
                    logger.error(f"Failed to upload {relative}: {e}")
                    stats["errors"] += 1
        
        logger.info(f"Drive sync complete: {stats}")
        return stats
    
    def _create_folder(
        self,
        name: str,
        parent_id: Optional[str] = None
    ) -> str:
        """
        Create a folder in Drive.
        
        Args:
            name: Folder name
            parent_id: Parent folder ID
            
        Returns:
            Created folder ID
        """
        result = self.drive.create_folder(name, parent_id)
        folder_id = result.get("id", result.get("fileId", ""))
        logger.debug(f"Created folder: {name} -> {folder_id}")
        return folder_id
    
    def _upload_file(
        self,
        local_path: Path,
        relative_path: Path,
        parent_folder_id: Optional[str]
    ) -> str:
        """
        Upload a file to Drive.
        
        Args:
            local_path: Local file path
            relative_path: Relative path for naming
            parent_folder_id: Parent folder ID
            
        Returns:
            Uploaded file ID
        """
        # Determine MIME type
        suffix = local_path.suffix.lower()
        mime_types = {
            ".md": "text/markdown",
            ".txt": "text/plain",
            ".json": "application/json",
            ".yaml": "text/yaml",
            ".yml": "text/yaml",
            ".py": "text/x-python",
        }
        mime_type = mime_types.get(suffix, "text/plain")
        
        # Read content
        try:
            content = local_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = local_path.read_bytes().decode("utf-8", errors="replace")
        
        # Upload
        name = str(relative_path).replace("/", "_")  # Flatten path
        
        # Check if file exists in map
        path_key = str(relative_path)
        if path_key in self._file_map:
            # Update existing
            file_id = self._file_map[path_key]
            self.drive.update_file(file_id, content, mime_type)
            logger.debug(f"Updated: {name}")
            return file_id
        else:
            # Create new - use call_tool directly for folderId
            result = self.drive.call_tool("google_drive_create_file", {
                "name": name,
                "mimeType": mime_type,
                "content": content,
                "folderId": parent_folder_id or ""
            })
            file_id = result.get("id", result.get("fileId", ""))
            self._file_map[path_key] = file_id
            logger.debug(f"Uploaded: {name} -> {file_id}")
            return file_id
    
    def list_files(self) -> List[Dict[str, Any]]:
        """
        List files in the mirror folder.
        
        Returns:
            List of file metadata
        """
        if self.folder_id:
            query = f"'{self.folder_id}' in parents"
        else:
            query = ""
        
        return self.drive.list_files(query=query, page_size=50)
