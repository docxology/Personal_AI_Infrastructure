"""
Coda Tables Client

Table and view operations.
"""

from typing import Dict, Any, List, Optional
from coda.core.base_client import CodaClient


class CodaTablesClient(CodaClient):
    """
    Client for Coda table operations.
    """
    
    def list_tables(
        self,
        doc_id: str,
        table_types: Optional[List[str]] = None,
        sort_by: Optional[str] = None,
        limit: int = 25
    ) -> List[Dict[str, Any]]:
        """
        List tables in a doc.
        
        Args:
            doc_id: ID of the doc
            table_types: Filter by type ('table', 'view')
            sort_by: Sort order ('name')
            limit: Maximum results
            
        Returns:
            List of table metadata
        """
        params = {
            "limit": limit,
            "sortBy": sort_by
        }
        if table_types:
            params["tableTypes"] = ",".join(table_types)
        
        return self._collect_pages(f"/docs/{doc_id}/tables", params, limit=limit)
    
    def get_table(
        self,
        doc_id: str,
        table_id_or_name: str,
        use_updated_layouts: bool = False
    ) -> Dict[str, Any]:
        """
        Get details about a table or view.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or URL-encoded name
            use_updated_layouts: Return new layout field values
            
        Returns:
            Table metadata including row count, columns, sorts
        """
        params = {}
        if use_updated_layouts:
            params["useUpdatedTableLayouts"] = True
        
        return self._get(f"/docs/{doc_id}/tables/{table_id_or_name}", params=params or None)
    
    def list_base_tables(self, doc_id: str, limit: int = 25) -> List[Dict[str, Any]]:
        """
        List only base tables (not views).
        
        Args:
            doc_id: ID of the doc
            limit: Maximum results
            
        Returns:
            List of base tables
        """
        return self.list_tables(doc_id, table_types=["table"], limit=limit)
    
    def list_views(self, doc_id: str, limit: int = 25) -> List[Dict[str, Any]]:
        """
        List only views.
        
        Args:
            doc_id: ID of the doc
            limit: Maximum results
            
        Returns:
            List of views
        """
        return self.list_tables(doc_id, table_types=["view"], limit=limit)
    
    def get_row_count(self, doc_id: str, table_id_or_name: str) -> int:
        """
        Get the row count of a table.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            
        Returns:
            Number of rows
        """
        table = self.get_table(doc_id, table_id_or_name)
        return table.get("rowCount", 0)
