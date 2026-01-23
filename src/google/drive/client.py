from typing import Dict, Any, List, Optional
import os
import logging
from google.base_client import GoogleMCPClient
from google.utils import get_base_credentials_path, load_google_credentials_env

class GoogleDriveClient(GoogleMCPClient):
    """
    A Python client that interfaces with the Google Drive MCP tools (via @dav23/google-mcp).
    """
    
    def __init__(self, 
                 credentials_path: Optional[str] = None):
        
        self.credentials_path = credentials_path or get_base_credentials_path()
        
        env = os.environ.copy()
        try:
            env.update(load_google_credentials_env())
        except Exception as e:
            logging.warning(f"Failed to load credentials for env: {e}")
        
        super().__init__(
            server_command=["npx", "-y", "@dav23/google-mcp", "start"],
            env=env
        )

    def list_files(self, query: str = "", page_size: int = 10) -> List[Dict[str, Any]]:
        """List files in Drive."""
        args = {"pageSize": page_size}
        if query:
            args["query"] = query
        return self.call_tool("google_drive_list_files", args)

    def create_folder(self, name: str, parent_id: Optional[str] = None) -> Dict[str, Any]:
        """Create a new folder."""
        args = {
            "name": name,
            "mimeType": "application/vnd.google-apps.folder",
            "content": "" # Required by schema strictly
        }
        if parent_id:
            args["folderId"] = parent_id # Tool uses folderId not parents
            
        return self.call_tool("google_drive_create_file", args)
        
    def upload_file(self, name: str, local_path: str, mime_type: str = "text/plain") -> Dict[str, Any]:
        """Upload a file."""
        with open(local_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        return self.call_tool("google_drive_create_file", {
            "name": name,
            "mimeType": mime_type,
            "content": content
        })

    def delete_file(self, file_id: str):
        """Delete a file."""
        return self.call_tool("google_drive_delete_file", {"fileId": file_id})

    def get_file_content(self, file_id: str) -> str:
        """Get the content of a file."""
        return self.call_tool("google_drive_get_file_content", {"fileId": file_id})

    def update_file(self, file_id: str, content: str, mime_type: Optional[str] = None) -> Dict[str, Any]:
        """Update the content of an existing file."""
        args = {
            "fileId": file_id,
            "content": content
        }
        if mime_type: args["mimeType"] = mime_type
        return self.call_tool("google_drive_update_file", args)

    def share_file(self, file_id: str, email_address: str, role: str = "reader", 
                   send_notification: bool = True, message: Optional[str] = None) -> Dict[str, Any]:
        """Share a file with another user."""
        args = {
            "fileId": file_id,
            "emailAddress": email_address,
            "role": role,
            "sendNotification": send_notification
        }
        if message: args["message"] = message
        return self.call_tool("google_drive_share_file", args)
