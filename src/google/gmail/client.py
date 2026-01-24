from typing import Dict, Any, List, Optional
import os
import base64
import logging
from google.base_client import GoogleMCPClient


def encode_subject(subject: str) -> str:
    """
    Encode email subject for MIME compatibility per RFC 2047.
    Non-ASCII subjects (like emoji) are base64-encoded with UTF-8.
    """
    if subject.isascii():
        return subject
    encoded = base64.b64encode(subject.encode('utf-8')).decode('ascii')
    return f'=?UTF-8?B?{encoded}?='
from google.utils import get_base_credentials_path, get_base_token_path, load_google_credentials_env

class GoogleGmailClient(GoogleMCPClient):
    """
    A Python client that interfaces with the Google Gmail MCP server.
    Enhanced with comprehensive email management methods including:
    - Email listing and retrieval
    - Drafts and sending
    - Labels and organization
    - Thread management
    - Attachments
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

    # =====================
    # Email Operations
    # =====================

    def list_emails(self, query: str = "", max_results: int = 10,
                    include_spam_trash: bool = False) -> List[Dict[str, Any]]:
        """
        List emails matching a query.
        
        Args:
            query: Gmail search query (e.g., 'from:user@example.com is:unread')
            max_results: Maximum number of emails to return
            include_spam_trash: Include spam and trash folders
        """
        args = {"maxResults": max_results}
        if query:
            args["query"] = query
        if include_spam_trash:
            args["includeSpamTrash"] = True
        return self.call_tool("google_gmail_list_emails", args)

    def get_email(self, message_id: str, format: str = "full") -> Dict[str, Any]:
        """
        Get a specific email.
        
        Args:
            message_id: The email ID
            format: 'full', 'minimal', 'raw', or 'metadata'
        """
        return self.call_tool("google_gmail_get_email", {
            "messageId": message_id,
            "format": format
        })

    def get_email_by_index(self, index: int, email_format: str = "full") -> Dict[str, Any]:
        """Get email by its index from the most recent search results."""
        return self.call_tool("google_gmail_get_email_by_index", {
            "index": index,
            "format": email_format
        })

    def search_emails(self, query: str, max_results: int = 25) -> List[Dict[str, Any]]:
        """
        Search emails with advanced Gmail query syntax.
        
        Example queries:
        - 'from:someone@example.com' - From specific sender
        - 'is:unread' - Unread emails
        - 'has:attachment' - Emails with attachments
        - 'after:2024/01/01 before:2024/12/31' - Date range
        - 'subject:meeting' - Subject contains word
        - 'label:important' - With specific label
        """
        return self.list_emails(query=query, max_results=max_results)

    # =====================
    # Compose & Send
    # =====================

    def create_draft(self, to: str, subject: str, body: str,
                     cc: Optional[List[str]] = None,
                     bcc: Optional[List[str]] = None,
                     is_html: bool = False) -> Dict[str, Any]:
        """
        Create a draft email.

        Args:
            to: Recipient email
            subject: Email subject (emoji/unicode supported)
            body: Email body
            cc: CC recipients
            bcc: BCC recipients
            is_html: True if body contains HTML
        """
        # Encode subject for MIME compatibility (handles emoji/unicode)
        encoded_subject = encode_subject(subject)
        args = {
            "to": [to],
            "subject": encoded_subject,
            "body": body,
            "isHtml": is_html
        }
        if cc:
            args["cc"] = cc
        if bcc:
            args["bcc"] = bcc
        return self.call_tool("google_gmail_draft_email", args)

    def send_email(self, to: str, subject: str, body: str,
                   cc: Optional[List[str]] = None,
                   bcc: Optional[List[str]] = None,
                   is_html: bool = False,
                   attachments: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Send a new email.

        Args:
            to: Recipient email
            subject: Email subject (emoji/unicode supported)
            body: Email body (plain text or HTML)
            cc: CC recipients list
            bcc: BCC recipients list
            is_html: True if body contains HTML
            attachments: List of attachment dicts with 'filename' and 'content' keys
        """
        # Encode subject for MIME compatibility (handles emoji/unicode)
        encoded_subject = encode_subject(subject)
        args = {
            "to": [to],
            "subject": encoded_subject,
            "body": body,
            "isHtml": is_html
        }
        if cc: 
            args["cc"] = cc
        if bcc: 
            args["bcc"] = bcc
        if attachments: 
            args["attachments"] = attachments
        return self.call_tool("google_gmail_send_email", args)

    def reply_to_email(self, message_id: str, body: str, 
                       is_html: bool = False) -> Dict[str, Any]:
        """
        Reply to an existing email.
        
        Args:
            message_id: ID of the email to reply to
            body: Reply body
            is_html: True if body is HTML
        """
        return self.call_tool("google_gmail_reply_email", {
            "messageId": message_id,
            "body": body,
            "isHtml": is_html
        })

    # =====================
    # Labels & Organization
    # =====================

    def list_labels(self) -> List[Dict[str, Any]]:
        """List all available Gmail labels."""
        return self.call_tool("google_gmail_list_labels", {})

    def modify_labels(self, message_id: str, 
                      add_labels: Optional[List[str]] = None, 
                      remove_labels: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Add or remove labels from an email.
        
        Common label IDs:
        - 'INBOX', 'SPAM', 'TRASH', 'UNREAD', 'STARRED', 'IMPORTANT'
        - 'CATEGORY_PERSONAL', 'CATEGORY_SOCIAL', 'CATEGORY_PROMOTIONS'
        """
        args = {"messageId": message_id}
        if add_labels: 
            args["addLabelIds"] = add_labels
        if remove_labels: 
            args["removeLabelIds"] = remove_labels
        return self.call_tool("google_gmail_modify_labels", args)

    def batch_modify_labels(self, message_ids: List[str],
                            add_labels: Optional[List[str]] = None,
                            remove_labels: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Modify labels for multiple emails at once."""
        results = []
        for msg_id in message_ids:
            result = self.modify_labels(msg_id, add_labels, remove_labels)
            results.append(result)
        return results

    def star_email(self, message_id: str) -> Dict[str, Any]:
        """Add a star to an email."""
        return self.modify_labels(message_id, add_labels=["STARRED"])

    def unstar_email(self, message_id: str) -> Dict[str, Any]:
        """Remove star from an email."""
        return self.modify_labels(message_id, remove_labels=["STARRED"])

    def mark_as_read(self, message_id: str) -> Dict[str, Any]:
        """Mark an email as read."""
        return self.modify_labels(message_id, remove_labels=["UNREAD"])

    def mark_as_unread(self, message_id: str) -> Dict[str, Any]:
        """Mark an email as unread."""
        return self.modify_labels(message_id, add_labels=["UNREAD"])

    def archive_email(self, message_id: str) -> Dict[str, Any]:
        """Archive an email (remove from inbox)."""
        return self.modify_labels(message_id, remove_labels=["INBOX"])

    # =====================
    # Delete & Trash
    # =====================

    def delete_email(self, message_id: str, permanently: bool = False) -> Dict[str, Any]:
        """
        Delete or trash an email.
        
        Args:
            message_id: The email ID
            permanently: If True, permanently delete. If False, move to trash.
        """
        return self.call_tool("google_gmail_delete_email", {
            "messageId": message_id,
            "permanently": permanently
        })

    def trash_email(self, message_id: str) -> Dict[str, Any]:
        """Move an email to trash."""
        return self.delete_email(message_id, permanently=False)

    def untrash_email(self, message_id: str) -> Dict[str, Any]:
        """Restore an email from trash."""
        return self.modify_labels(message_id, remove_labels=["TRASH"], add_labels=["INBOX"])

    # =====================
    # Attachments
    # =====================

    def download_attachments(self, message_id: str, 
                             download_path: Optional[str] = None) -> Dict[str, Any]:
        """
        Download all attachments from a specific email.
        
        Args:
            message_id: The email ID
            download_path: Directory to save attachments (optional)
        """
        args = {"messageId": message_id}
        if download_path: 
            args["downloadPath"] = download_path
        return self.call_tool("google_gmail_download_attachments", args)

    # =====================
    # Thread Operations
    # =====================

    def list_threads(self, query: str = "", max_results: int = 10) -> List[Dict[str, Any]]:
        """
        List email threads.
        
        Args:
            query: Gmail search query
            max_results: Maximum threads to return
        """
        args = {"maxResults": max_results}
        if query:
            args["query"] = query
        return self.call_tool("google_gmail_list_threads", args)

    def get_thread(self, thread_id: str) -> Dict[str, Any]:
        """Get all messages in a thread."""
        return self.call_tool("google_gmail_get_thread", {"threadId": thread_id})

    def trash_thread(self, thread_id: str) -> Dict[str, Any]:
        """Move an entire thread to trash."""
        return self.call_tool("google_gmail_trash_thread", {"threadId": thread_id})

    # =====================
    # Convenience Methods
    # =====================

    def get_unread_count(self) -> int:
        """Get count of unread emails in inbox."""
        results = self.list_emails(query="is:unread", max_results=100)
        return len(results) if isinstance(results, list) else 0

    def get_recent_from(self, sender: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Get recent emails from a specific sender."""
        return self.list_emails(query=f"from:{sender}", max_results=max_results)

    def get_emails_with_attachments(self, max_results: int = 10) -> List[Dict[str, Any]]:
        """Get emails that have attachments."""
        return self.list_emails(query="has:attachment", max_results=max_results)

    def get_starred_emails(self, max_results: int = 25) -> List[Dict[str, Any]]:
        """Get starred emails."""
        return self.list_emails(query="is:starred", max_results=max_results)

