"""
Coda Rows Client

Row CRUD operations for tables.
"""

from typing import Dict, Any, List, Optional, Union
from coda.core.base_client import CodaClient


class CodaRowsClient(CodaClient):
    """
    Client for Coda row operations.
    """
    
    def list_rows(
        self,
        doc_id: str,
        table_id_or_name: str,
        query: Optional[str] = None,
        sort_by: Optional[str] = None,
        use_column_names: bool = False,
        value_format: str = "simple",
        visible_only: bool = False,
        sync_token: Optional[str] = None,
        limit: int = 25
    ) -> List[Dict[str, Any]]:
        """
        List rows in a table.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            query: Filter query (column_id:"value")
            sort_by: Sort order ('createdAt', 'natural', 'updatedAt')
            use_column_names: Use names instead of IDs in values
            value_format: 'simple', 'simpleWithArrays', or 'rich'
            visible_only: Only visible rows
            sync_token: Token for incremental sync
            limit: Maximum results
            
        Returns:
            List of rows with values
        """
        params = {
            "limit": limit,
            "query": query,
            "sortBy": sort_by,
            "useColumnNames": use_column_names if use_column_names else None,
            "valueFormat": value_format if value_format != "simple" else None,
            "visibleOnly": visible_only if visible_only else None,
            "syncToken": sync_token
        }
        
        return self._collect_pages(
            f"/docs/{doc_id}/tables/{table_id_or_name}/rows",
            params,
            limit=limit
        )
    
    def get_row(
        self,
        doc_id: str,
        table_id_or_name: str,
        row_id_or_name: str,
        use_column_names: bool = False,
        value_format: str = "simple"
    ) -> Dict[str, Any]:
        """
        Get a single row.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            row_id_or_name: Row ID or display value
            use_column_names: Use names in values
            value_format: Value format
            
        Returns:
            Row with values
        """
        params = {
            "useColumnNames": use_column_names if use_column_names else None,
            "valueFormat": value_format if value_format != "simple" else None
        }
        
        return self._get(
            f"/docs/{doc_id}/tables/{table_id_or_name}/rows/{row_id_or_name}",
            params={k: v for k, v in params.items() if v is not None} or None
        )
    
    def insert_rows(
        self,
        doc_id: str,
        table_id_or_name: str,
        rows: List[Dict[str, Any]],
        key_columns: Optional[List[str]] = None,
        disable_parsing: bool = False
    ) -> Dict[str, Any]:
        """
        Insert or upsert rows.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name (must be base table)
            rows: List of row data [{"cells": [{"column": "col_id", "value": val}]}]
            key_columns: Columns for upsert matching
            disable_parsing: Skip value parsing
            
        Returns:
            Result with requestId and addedRowIds
        """
        data = {"rows": rows}
        if key_columns:
            data["keyColumns"] = key_columns
        
        params = {}
        if disable_parsing:
            params["disableParsing"] = True
        
        return self._post(
            f"/docs/{doc_id}/tables/{table_id_or_name}/rows",
            data=data,
            params=params or None
        )
    
    def insert_row(
        self,
        doc_id: str,
        table_id_or_name: str,
        values: Dict[str, Any],
        disable_parsing: bool = False
    ) -> Dict[str, Any]:
        """
        Insert a single row with column:value mapping.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            values: Dict of column_id: value
            disable_parsing: Skip value parsing
            
        Returns:
            Result with requestId and addedRowIds
        """
        cells = [{"column": k, "value": v} for k, v in values.items()]
        return self.insert_rows(
            doc_id,
            table_id_or_name,
            rows=[{"cells": cells}],
            disable_parsing=disable_parsing
        )
    
    def upsert_rows(
        self,
        doc_id: str,
        table_id_or_name: str,
        rows: List[Dict[str, Any]],
        key_columns: List[str],
        disable_parsing: bool = False
    ) -> Dict[str, Any]:
        """
        Upsert rows (insert or update based on key columns).
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            rows: Row data
            key_columns: Columns to match for upsert
            disable_parsing: Skip value parsing
            
        Returns:
            Result with requestId
        """
        return self.insert_rows(
            doc_id,
            table_id_or_name,
            rows=rows,
            key_columns=key_columns,
            disable_parsing=disable_parsing
        )
    
    def update_row(
        self,
        doc_id: str,
        table_id_or_name: str,
        row_id_or_name: str,
        values: Dict[str, Any],
        disable_parsing: bool = False
    ) -> Dict[str, Any]:
        """
        Update a single row.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            row_id_or_name: Row ID or display value
            values: Column:value updates
            disable_parsing: Skip value parsing
            
        Returns:
            Result with requestId
        """
        cells = [{"column": k, "value": v} for k, v in values.items()]
        data = {"row": {"cells": cells}}
        
        params = {}
        if disable_parsing:
            params["disableParsing"] = True
        
        return self._put(
            f"/docs/{doc_id}/tables/{table_id_or_name}/rows/{row_id_or_name}",
            data=data
        )
    
    def delete_row(
        self,
        doc_id: str,
        table_id_or_name: str,
        row_id_or_name: str
    ) -> Dict[str, Any]:
        """
        Delete a single row.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            row_id_or_name: Row ID or display value
            
        Returns:
            Result with requestId
        """
        return self._delete(
            f"/docs/{doc_id}/tables/{table_id_or_name}/rows/{row_id_or_name}"
        )
    
    def delete_rows(
        self,
        doc_id: str,
        table_id_or_name: str,
        row_ids: List[str]
    ) -> Dict[str, Any]:
        """
        Delete multiple rows.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            row_ids: List of row IDs to delete
            
        Returns:
            Result with requestId and rowIds
        """
        return self._delete(
            f"/docs/{doc_id}/tables/{table_id_or_name}/rows",
            data={"rowIds": row_ids}
        )
    
    def push_button(
        self,
        doc_id: str,
        table_id_or_name: str,
        row_id_or_name: str,
        column_id_or_name: str
    ) -> Dict[str, Any]:
        """
        Push a button in a row.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            row_id_or_name: Row ID or display value
            column_id_or_name: Button column ID or name
            
        Returns:
            Result with requestId, rowId, columnId
        """
        return self._post(
            f"/docs/{doc_id}/tables/{table_id_or_name}/rows/{row_id_or_name}/buttons/{column_id_or_name}"
        )
    
    def query_rows(
        self,
        doc_id: str,
        table_id_or_name: str,
        column: str,
        value: Union[str, int, float, bool]
    ) -> List[Dict[str, Any]]:
        """
        Query rows where column equals value.
        
        Args:
            doc_id: ID of the doc
            table_id_or_name: Table ID or name
            column: Column ID or name
            value: Value to match
            
        Returns:
            Matching rows
        """
        # Format value for query
        if isinstance(value, str):
            query_value = f'"{value}"'
        elif isinstance(value, bool):
            query_value = "true" if value else "false"
        else:
            query_value = str(value)
        
        query = f'{column}:{query_value}'
        return self.list_rows(doc_id, table_id_or_name, query=query)
