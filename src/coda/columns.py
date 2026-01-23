"""
Coda Columns Client

Column operations for tables.
"""

from typing import Dict, Any, List, Optional
from coda.base_client import CodaClient


class CodaColumnsClient(CodaClient):
    """
    Client for Coda column operations.
    """
    
    def list_columns(
        self,
        doc_id: str,
        table_id_or_name: str,
        visible_only: bool = False,
        limit: int = 25
    ) -> List[Dict[str, Any]]:
        """
        List columns in a table.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            visible_only: Only return visible columns (base tables only)
            limit: Maximum results (1-100)
            
        Returns:
            List of column metadata
        """
        params = {
            "limit": min(limit, 100),
            "visibleOnly": visible_only if visible_only else None
        }
        
        return self._collect_pages(
            f"/docs/{doc_id}/tables/{table_id_or_name}/columns",
            params,
            limit=limit
        )
    
    def get_column(
        self,
        doc_id: str,
        table_id_or_name: str,
        column_id_or_name: str
    ) -> Dict[str, Any]:
        """
        Get details about a column.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            column_id_or_name: Column ID or URL-encoded name
            
        Returns:
            Column metadata including format, formula, default value
        """
        return self._get(
            f"/docs/{doc_id}/tables/{table_id_or_name}/columns/{column_id_or_name}"
        )
    
    def get_display_column(
        self,
        doc_id: str,
        table_id_or_name: str
    ) -> Optional[Dict[str, Any]]:
        """
        Get the display column for a table.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            
        Returns:
            Display column or None
        """
        columns = self.list_columns(doc_id, table_id_or_name)
        for col in columns:
            if col.get("display"):
                return col
        return None
    
    def get_formula_columns(
        self,
        doc_id: str,
        table_id_or_name: str
    ) -> List[Dict[str, Any]]:
        """
        Get columns that have formulas.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            
        Returns:
            List of calculated columns
        """
        columns = self.list_columns(doc_id, table_id_or_name, limit=100)
        return [c for c in columns if c.get("calculated")]
