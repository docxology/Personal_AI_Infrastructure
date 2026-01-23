"""
Coda Docs Client

Document management operations.
"""

from typing import Dict, Any, List, Optional
from coda.base_client import CodaClient


class CodaDocsClient(CodaClient):
    """
    Client for Coda document operations.
    
    Inherits from CodaClient and provides doc-specific convenience methods.
    """
    
    # All doc methods inherited from CodaClient:
    # - list_docs()
    # - get_doc()
    # - create_doc()
    # - update_doc()
    # - delete_doc()
    
    def copy_doc(
        self,
        source_doc_id: str,
        title: Optional[str] = None,
        folder_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a copy of an existing doc.
        
        Args:
            source_doc_id: ID of doc to copy
            title: Title for the copy
            folder_id: Destination folder
            
        Returns:
            New doc metadata
        """
        return self.create_doc(
            title=title,
            source_doc=source_doc_id,
            folder_id=folder_id
        )
    
    def get_doc_size(self, doc_id: str) -> Dict[str, Any]:
        """
        Get the size metrics of a doc.
        
        Args:
            doc_id: ID of the doc
            
        Returns:
            Dict with totalRowCount, tableAndViewCount, pageCount
        """
        doc = self.get_doc(doc_id)
        return doc.get("docSize", {})
    
    def search_docs(self, query: str, limit: int = 25) -> List[Dict[str, Any]]:
        """
        Search docs by title/content.
        
        Args:
            query: Search term
            limit: Maximum results
            
        Returns:
            Matching docs
        """
        return self.list_docs(query=query, limit=limit)
    
    def list_my_docs(self, limit: int = 25) -> List[Dict[str, Any]]:
        """
        List docs owned by current user.
        
        Args:
            limit: Maximum results
            
        Returns:
            Owned docs
        """
        return self.list_docs(is_owner=True, limit=limit)
    
    def list_starred_docs(self, limit: int = 25) -> List[Dict[str, Any]]:
        """
        List starred docs.
        
        Args:
            limit: Maximum results
            
        Returns:
            Starred docs
        """
        return self.list_docs(is_starred=True, limit=limit)
