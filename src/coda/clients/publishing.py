"""
Coda Publishing Client

Doc publishing and categories.
"""

from typing import Dict, Any, List, Optional, Literal
from coda.core.base_client import CodaClient


PublishMode = Literal["view", "play", "edit"]


class CodaPublishingClient(CodaClient):
    """
    Client for Coda publishing operations.
    """
    
    def get_categories(self) -> List[Dict[str, Any]]:
        """
        Get all available doc categories.
        
        Returns:
            List of categories
        """
        response = self._get("/categories")
        return response.get("items", [])
    
    def publish_doc(
        self,
        doc_id: str,
        slug: Optional[str] = None,
        discoverable: bool = True,
        earn_credit: bool = False,
        category_names: Optional[List[str]] = None,
        mode: PublishMode = "view"
    ) -> Dict[str, Any]:
        """
        Publish a doc.
        
        Args:
            doc_id: ID of the doc
            slug: URL slug for published doc
            discoverable: Show in gallery
            earn_credit: Earn credit for signups
            category_names: Categories to apply
            mode: Interaction mode (view, play, edit)
            
        Returns:
            Result with requestId
        """
        data = {
            "discoverable": discoverable,
            "earnCredit": earn_credit,
            "mode": mode
        }
        if slug:
            data["slug"] = slug
        if category_names:
            data["categoryNames"] = category_names
        
        return self._put(f"/docs/{doc_id}/publish", data=data)
    
    def unpublish_doc(self, doc_id: str) -> Dict[str, Any]:
        """
        Unpublish a doc.
        
        Args:
            doc_id: ID of the doc
            
        Returns:
            Result
        """
        return self._delete(f"/docs/{doc_id}/publish")
    
    def get_publish_status(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """
        Get publishing status of a doc.
        
        Args:
            doc_id: ID of the doc
            
        Returns:
            Published info or None if not published
        """
        doc = self.get_doc(doc_id)
        return doc.get("published")
