"""
Coda Mirror

Mirror knowledge base to Coda document pages.
"""

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# Default PAI Document Controller
PAI_DOC_ID = "NDxZHneeIw"


class CodaMirror:
    """
    Mirror knowledge files to Coda document pages.
    
    Supports:
    - Creating pages for each knowledge file
    - Updating existing pages
    - Organizing by subfolder structure
    
    Usage:
        mirror = CodaMirror(doc_id="NDxZHneeIw")
        result = mirror.sync(source_dir=Path("~/.pai/knowledge"))
    """
    
    def __init__(self, doc_id: str = PAI_DOC_ID):
        """
        Initialize Coda mirror.
        
        Args:
            doc_id: Coda document ID to sync to
        """
        self.doc_id = doc_id
        self._pages_client = None
        self._page_map: Dict[str, str] = {}  # path -> page_id
    
    @property
    def pages_client(self):
        """Lazy-load Coda pages client."""
        if self._pages_client is None:
            from coda.clients.pages import CodaPagesClient
            self._pages_client = CodaPagesClient()
        return self._pages_client
    
    def sync(
        self,
        source_dir: Path,
        parent_page_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Sync knowledge files to Coda pages.
        
        Args:
            source_dir: Source directory to mirror
            parent_page_id: Parent page for created pages
            
        Returns:
            Sync result with stats
        """
        logger.info(f"Syncing {source_dir} to Coda doc {self.doc_id}")
        
        if not source_dir.exists():
            return {"success": False, "error": f"Source not found: {source_dir}"}
        
        # Load existing pages for mapping
        self._load_existing_pages()
        
        stats = {
            "success": True,
            "pages_created": 0,
            "pages_updated": 0,
            "errors": 0,
        }
        
        # Process markdown files
        for item in sorted(source_dir.rglob("*.md")):
            relative = item.relative_to(source_dir)
            
            # Skip hidden files
            if any(part.startswith(".") for part in relative.parts):
                continue
            
            try:
                result = self._sync_file(item, relative, parent_page_id)
                if result.get("created"):
                    stats["pages_created"] += 1
                else:
                    stats["pages_updated"] += 1
            except Exception as e:
                logger.error(f"Failed to sync {relative}: {e}")
                stats["errors"] += 1
        
        logger.info(f"Coda sync complete: {stats}")
        return stats
    
    def _load_existing_pages(self) -> None:
        """Load existing pages to avoid duplicates."""
        try:
            pages = self.pages_client.list_pages(self.doc_id, limit=100)
            for page in pages:
                name = page.get("name", "")
                page_id = page.get("id", "")
                if name and page_id:
                    self._page_map[name] = page_id
            logger.debug(f"Loaded {len(self._page_map)} existing pages")
        except Exception as e:
            logger.warning(f"Failed to load existing pages: {e}")
    
    def _sync_file(
        self,
        local_path: Path,
        relative_path: Path,
        parent_page_id: Optional[str]
    ) -> Dict[str, Any]:
        """
        Sync a single file to a Coda page.
        
        Args:
            local_path: Local file path
            relative_path: Relative path for naming
            parent_page_id: Parent page ID
            
        Returns:
            Sync result
        """
        # Read content
        content = local_path.read_text(encoding="utf-8")
        
        # Extract title from first heading or filename
        title = self._extract_title(content, relative_path)
        
        # Generate subtitle with metadata
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        subtitle = f"Mirrored from {relative_path} at {now}"
        
        # Check if page exists
        if title in self._page_map:
            # Update existing page
            page_id = self._page_map[title]
            self.pages_client.update_page(
                self.doc_id,
                page_id,
                subtitle=subtitle
            )
            logger.debug(f"Updated page: {title}")
            return {"created": False, "page_id": page_id}
        else:
            # Create new page
            result = self.pages_client.create_page(
                self.doc_id,
                name=title,
                subtitle=subtitle,
                parent_page_id=parent_page_id
            )
            page_id = result.get("id", "")
            self._page_map[title] = page_id
            logger.debug(f"Created page: {title}")
            return {"created": True, "page_id": page_id}
    
    def _extract_title(self, content: str, relative_path: Path) -> str:
        """
        Extract title from content or filename.
        
        Args:
            content: File content
            relative_path: Relative path
            
        Returns:
            Title string
        """
        # Try to find first heading
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()[:50]
        
        # Use filename
        return relative_path.stem.replace("_", " ").replace("-", " ").title()[:50]
    
    def list_pages(self) -> List[Dict[str, Any]]:
        """
        List pages in the target document.
        
        Returns:
            List of page metadata
        """
        return self.pages_client.list_pages(self.doc_id, limit=100)
