"""
Coda Pages Client

Page management and content operations.
"""

from typing import Dict, Any, List, Optional
from coda.core.base_client import CodaClient


class CodaPagesClient(CodaClient):
    """
    Client for Coda page operations.
    """
    
    def list_pages(
        self,
        doc_id: str,
        limit: int = 25
    ) -> List[Dict[str, Any]]:
        """
        List pages in a doc.
        
        Args:
            doc_id: ID of the doc
            limit: Maximum results
            
        Returns:
            List of page metadata
        """
        return self._collect_pages(f"/docs/{doc_id}/pages", {"limit": limit}, limit=limit)
    
    def get_page(
        self,
        doc_id: str,
        page_id_or_name: str
    ) -> Dict[str, Any]:
        """
        Get details about a page.
        
        Args:
            doc_id: ID of the doc
            page_id_or_name: Page ID or URL-encoded name
            
        Returns:
            Page metadata including content type, children, authors
        """
        return self._get(f"/docs/{doc_id}/pages/{page_id_or_name}")
    
    def create_page(
        self,
        doc_id: str,
        name: Optional[str] = None,
        subtitle: Optional[str] = None,
        icon_name: Optional[str] = None,
        image_url: Optional[str] = None,
        parent_page_id: Optional[str] = None,
        page_content: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a new page in a doc.
        
        Args:
            doc_id: ID of the doc
            name: Page name
            subtitle: Page subtitle
            icon_name: Icon name
            image_url: Cover image URL
            parent_page_id: Parent page for subpages
            page_content: Initial content (canvas or embed URL)
            
        Returns:
            Result with requestId and page id
        """
        data = {}
        if name:
            data["name"] = name
        if subtitle:
            data["subtitle"] = subtitle
        if icon_name:
            data["iconName"] = icon_name
        if image_url:
            data["imageUrl"] = image_url
        if parent_page_id:
            data["parentPageId"] = parent_page_id
        if page_content:
            data["pageContent"] = page_content
        
        return self._post(f"/docs/{doc_id}/pages", data=data)
    
    def update_page(
        self,
        doc_id: str,
        page_id_or_name: str,
        name: Optional[str] = None,
        subtitle: Optional[str] = None,
        icon_name: Optional[str] = None,
        image_url: Optional[str] = None,
        is_hidden: Optional[bool] = None,
        content_update: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Update page properties.
        
        Args:
            doc_id: ID of the doc
            page_id_or_name: Page ID or name
            name: New name
            subtitle: New subtitle
            icon_name: New icon
            image_url: New cover image
            is_hidden: Hide/show page
            content_update: Content update object
            
        Returns:
            Result with requestId
        """
        data = {}
        if name:
            data["name"] = name
        if subtitle:
            data["subtitle"] = subtitle
        if icon_name:
            data["iconName"] = icon_name
        if image_url:
            data["imageUrl"] = image_url
        if is_hidden is not None:
            data["isHidden"] = is_hidden
        if content_update:
            data["contentUpdate"] = content_update
        
        return self._put(f"/docs/{doc_id}/pages/{page_id_or_name}", data=data)
    
    def delete_page(
        self,
        doc_id: str,
        page_id_or_name: str
    ) -> Dict[str, Any]:
        """
        Delete a page.
        
        Args:
            doc_id: ID of the doc
            page_id_or_name: Page ID or name
            
        Returns:
            Result with requestId
        """
        return self._delete(f"/docs/{doc_id}/pages/{page_id_or_name}")
    
    def list_page_content(
        self,
        doc_id: str,
        page_id_or_name: str,
        content_format: str = "plainText",
        limit: int = 50
    ) -> List[Dict[str, Any]]:
        """
        List content elements in a page.
        
        Args:
            doc_id: ID of the doc
            page_id_or_name: Page ID or name
            content_format: Format (plainText)
            limit: Maximum results (1-500)
            
        Returns:
            List of content elements
        """
        params = {
            "contentFormat": content_format,
            "limit": limit
        }
        return self._collect_pages(
            f"/docs/{doc_id}/pages/{page_id_or_name}/content",
            params,
            limit=limit
        )
    
    def delete_page_content(
        self,
        doc_id: str,
        page_id_or_name: str,
        element_ids: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Delete content from a page.
        
        Args:
            doc_id: ID of the doc
            page_id_or_name: Page ID or name
            element_ids: Specific elements to delete (None = all)
            
        Returns:
            Result with requestId
        """
        data = {}
        if element_ids:
            data["elementIds"] = element_ids
        
        return self._delete(f"/docs/{doc_id}/pages/{page_id_or_name}/content", data=data)
    
    def begin_page_export(
        self,
        doc_id: str,
        page_id_or_name: str,
        output_format: str = "html"
    ) -> Dict[str, Any]:
        """
        Start exporting page content.
        
        Args:
            doc_id: ID of the doc
            page_id_or_name: Page ID or name
            output_format: 'html' or 'markdown'
            
        Returns:
            Export status with id, status, href
        """
        return self._post(
            f"/docs/{doc_id}/pages/{page_id_or_name}/export",
            data={"outputFormat": output_format}
        )
    
    def get_page_export_status(
        self,
        doc_id: str,
        page_id_or_name: str,
        request_id: str
    ) -> Dict[str, Any]:
        """
        Check page export status.
        
        Args:
            doc_id: ID of the doc
            page_id_or_name: Page ID or name
            request_id: Export request ID
            
        Returns:
            Status with downloadLink when complete
        """
        return self._get(f"/docs/{doc_id}/pages/{page_id_or_name}/export/{request_id}")
