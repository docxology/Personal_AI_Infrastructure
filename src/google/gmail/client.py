from typing import Dict, Any, List, Optional
import os
from google.base_client import GoogleMCPClient
from google.utils import get_base_credentials_path, get_base_token_path, load_google_credentials_env

class GoogleGmailClient(GoogleMCPClient):
    """
    A Python client that interfaces with the Google Gmail MCP server.
    """
    
    def __init__(self, 
                 credentials_path: Optional[str] = None):
        
        self.credentials_path = credentials_path or get_base_credentials_path()
        
        env = os.environ.copy()
        try:
             env.update(load_google_credentials_env())
        except Exception as e:
             print(f"Warning: Failed to load credentials for env: {e}")
        
        super().__init__(
            server_command=["npx", "-y", "@dav23/google-mcp", "start"],
            env=env
        )

    def list_emails(self, query: str = "", max_results: int = 10) -> List[Dict[str, Any]]:
        """List emails."""
        args = {"maxResults": max_results}
        if query:
            args["query"] = query
        # Using google_gmail_list_emails
        return self.call_tool("google_gmail_list_emails", args)

    def get_email(self, message_id: str) -> Dict[str, Any]:
        """Get a specific email."""
        return self.call_tool("google_gmail_get_email", {"messageId": message_id})
    
    def create_draft(self, to: str, subject: str, body: str) -> Dict[str, Any]:
        """Create a draft email."""
        # 'to' must be an array of strings
        return self.call_tool("google_gmail_draft_email", {
            "to": [to], 
            "subject": subject,
            "body": body
        })

    def list_labels(self) -> List[Dict[str, Any]]:
        """List all available Gmail labels."""
        return self.call_tool("google_gmail_list_labels", {})

    def get_email_by_index(self, index: int, email_format: str = "full") -> Dict[str, Any]:
        """Get email by its index from the most recent search results."""
        return self.call_tool("google_gmail_get_email_by_index", {
            "index": index,
            "format": email_format
        })

    def send_email(self, to: str, subject: str, body: str, 
                   cc: Optional[List[str]] = None, bcc: Optional[List[str]] = None, 
                   is_html: bool = False, attachments: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """Send a new email."""
        args = {
            "to": [to],
            "subject": subject,
            "body": body,
            "isHtml": is_html
        }
        if cc: args["cc"] = cc
        if bcc: args["bcc"] = bcc
        if attachments: args["attachments"] = attachments
        return self.call_tool("google_gmail_send_email", args)

    def delete_email(self, message_id: str, permanently: bool = False) -> Dict[str, Any]:
        """Delete or trash an email."""
        return self.call_tool("google_gmail_delete_email", {
            "messageId": message_id,
            "permanently": permanently
        })

    def modify_labels(self, message_id: str, add_labels: Optional[List[str]] = None, remove_labels: Optional[List[str]] = None) -> Dict[str, Any]:
        """Add or remove labels from an email."""
        args = {"messageId": message_id}
        if add_labels: args["addLabelIds"] = add_labels
        if remove_labels: args["removeLabelIds"] = remove_labels
        return self.call_tool("google_gmail_modify_labels", args)

    def download_attachments(self, message_id: str, download_path: Optional[str] = None) -> Dict[str, Any]:
        """Download all attachments from a specific email."""
        args = {"messageId": message_id}
        if download_path: args["downloadPath"] = download_path
        return self.call_tool("google_gmail_download_attachments", args)
