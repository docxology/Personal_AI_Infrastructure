"""
Coda Permissions Client

ACL and sharing operations.
"""

from typing import Dict, Any, List, Optional, Literal
from coda.base_client import CodaClient


AccessType = Literal["readonly", "write", "comment"]


class CodaPermissionsClient(CodaClient):
    """
    Client for Coda permission and ACL operations.
    """
    
    def get_sharing_metadata(self, doc_id: str) -> Dict[str, Any]:
        """
        Get sharing capabilities for a doc.
        
        Args:
            doc_id: ID of the doc
            
        Returns:
            Sharing capabilities (canShare, canCopy, etc.)
        """
        return self._get(f"/docs/{doc_id}/acl/metadata")
    
    def list_permissions(
        self,
        doc_id: str,
        limit: int = 25
    ) -> List[Dict[str, Any]]:
        """
        List permissions on a doc.
        
        Args:
            doc_id: ID of the doc
            limit: Maximum results
            
        Returns:
            List of permissions with principals
        """
        return self._collect_pages(
            f"/docs/{doc_id}/acl/permissions",
            {"limit": limit},
            limit=limit
        )
    
    def add_permission(
        self,
        doc_id: str,
        access: AccessType,
        email: Optional[str] = None,
        domain: Optional[str] = None,
        suppress_email: bool = False
    ) -> Dict[str, Any]:
        """
        Add a permission to a doc.
        
        Args:
            doc_id: ID of the doc
            access: Access level ('readonly', 'write', 'comment')
            email: User email (for email principal)
            domain: Domain (for domain principal)
            suppress_email: Don't send notification email
            
        Returns:
            Result
        """
        if email:
            principal = {"type": "email", "email": email}
        elif domain:
            principal = {"type": "domain", "domain": domain}
        else:
            raise ValueError("Must provide email or domain")
        
        data = {
            "access": access,
            "principal": principal,
            "suppressEmail": suppress_email
        }
        
        return self._post(f"/docs/{doc_id}/acl/permissions", data=data)
    
    def share_with_user(
        self,
        doc_id: str,
        email: str,
        access: AccessType = "readonly",
        suppress_email: bool = False
    ) -> Dict[str, Any]:
        """
        Share a doc with a user.
        
        Args:
            doc_id: ID of the doc
            email: User email
            access: Access level
            suppress_email: Don't notify
            
        Returns:
            Result
        """
        return self.add_permission(
            doc_id,
            access=access,
            email=email,
            suppress_email=suppress_email
        )
    
    def delete_permission(
        self,
        doc_id: str,
        permission_id: str
    ) -> Dict[str, Any]:
        """
        Remove a permission from a doc.
        
        Args:
            doc_id: ID of the doc
            permission_id: Permission ID
            
        Returns:
            Result
        """
        return self._delete(f"/docs/{doc_id}/acl/permissions/{permission_id}")
    
    def search_principals(
        self,
        doc_id: str,
        query: str
    ) -> Dict[str, Any]:
        """
        Search for users/groups to share with.
        
        Args:
            doc_id: ID of the doc
            query: Search term
            
        Returns:
            Dict with 'users' and 'groups' lists
        """
        return self._get(
            f"/docs/{doc_id}/acl/principals/search",
            params={"query": query}
        )
    
    def get_acl_settings(self, doc_id: str) -> Dict[str, Any]:
        """
        Get ACL settings for a doc.
        
        Args:
            doc_id: ID of the doc
            
        Returns:
            Settings (allowEditorsToChangePermissions, allowCopying, etc.)
        """
        return self._get(f"/docs/{doc_id}/acl/settings")
    
    def update_acl_settings(
        self,
        doc_id: str,
        allow_editors_to_change_permissions: Optional[bool] = None,
        allow_copying: Optional[bool] = None,
        allow_viewers_to_request_editing: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        Update ACL settings for a doc.
        
        Args:
            doc_id: ID of the doc
            allow_editors_to_change_permissions: Editors can share
            allow_copying: Viewers can copy
            allow_viewers_to_request_editing: Viewers can request edit
            
        Returns:
            Updated settings
        """
        data = {}
        if allow_editors_to_change_permissions is not None:
            data["allowEditorsToChangePermissions"] = allow_editors_to_change_permissions
        if allow_copying is not None:
            data["allowCopying"] = allow_copying
        if allow_viewers_to_request_editing is not None:
            data["allowViewersToRequestEditing"] = allow_viewers_to_request_editing
        
        return self._patch(f"/docs/{doc_id}/acl/settings", data=data)
