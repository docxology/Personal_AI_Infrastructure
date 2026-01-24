"""
Coda Analytics Client

Doc and Pack analytics operations.
"""

from typing import Dict, Any, List, Optional, Literal
from coda.core.base_client import CodaClient


AnalyticsScale = Literal["daily", "cumulative"]
SortDirection = Literal["ascending", "descending"]


class CodaAnalyticsClient(CodaClient):
    """
    Client for Coda analytics operations.
    """
    
    def list_doc_analytics(
        self,
        doc_ids: Optional[List[str]] = None,
        workspace_id: Optional[str] = None,
        query: Optional[str] = None,
        is_published: Optional[bool] = None,
        since_date: Optional[str] = None,
        until_date: Optional[str] = None,
        scale: AnalyticsScale = "daily",
        order_by: Optional[str] = None,
        direction: Optional[SortDirection] = None,
        limit: int = 1000
    ) -> List[Dict[str, Any]]:
        """
        Get doc analytics data.
        
        Args:
            doc_ids: Filter by doc IDs
            workspace_id: Filter by workspace
            query: Search term
            is_published: Published docs only
            since_date: Start date (YYYY-MM-DD)
            until_date: End date (YYYY-MM-DD)
            scale: 'daily' or 'cumulative'
            order_by: Sort field
            direction: Sort direction
            limit: Maximum results (1-5000)
            
        Returns:
            List of analytics items
        """
        params = {
            "docIds": doc_ids,
            "workspaceId": workspace_id,
            "query": query,
            "isPublished": is_published,
            "sinceDate": since_date,
            "untilDate": until_date,
            "scale": scale,
            "orderBy": order_by,
            "direction": direction,
            "limit": min(limit, 5000)
        }
        
        return self._collect_pages("/analytics/docs", params, limit=limit)
    
    def list_page_analytics(
        self,
        doc_id: str,
        since_date: Optional[str] = None,
        until_date: Optional[str] = None,
        limit: int = 1000
    ) -> List[Dict[str, Any]]:
        """
        Get page analytics for a doc (Enterprise only).
        
        Args:
            doc_id: ID of the doc
            since_date: Start date
            until_date: End date
            limit: Maximum results
            
        Returns:
            List of page analytics items
        """
        params = {
            "sinceDate": since_date,
            "untilDate": until_date,
            "limit": min(limit, 5000)
        }
        
        return self._collect_pages(f"/analytics/docs/{doc_id}/pages", params, limit=limit)
    
    def get_doc_analytics_summary(
        self,
        workspace_id: Optional[str] = None,
        is_published: Optional[bool] = None,
        since_date: Optional[str] = None,
        until_date: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get summarized doc analytics.
        
        Args:
            workspace_id: Filter by workspace
            is_published: Published docs only
            since_date: Start date
            until_date: End date
            
        Returns:
            Summary with totalSessions
        """
        params = {
            "workspaceId": workspace_id,
            "isPublished": is_published,
            "sinceDate": since_date,
            "untilDate": until_date
        }
        
        return self._get("/analytics/docs/summary", params={k: v for k, v in params.items() if v is not None})
    
    def list_pack_analytics(
        self,
        pack_ids: Optional[List[int]] = None,
        workspace_id: Optional[str] = None,
        query: Optional[str] = None,
        is_published: Optional[bool] = None,
        since_date: Optional[str] = None,
        until_date: Optional[str] = None,
        scale: AnalyticsScale = "daily",
        order_by: Optional[str] = None,
        direction: Optional[SortDirection] = None,
        limit: int = 1000
    ) -> List[Dict[str, Any]]:
        """
        Get Pack analytics data.
        
        Args:
            pack_ids: Filter by Pack IDs
            workspace_id: Filter by workspace
            query: Search term
            is_published: Published only
            since_date: Start date
            until_date: End date
            scale: 'daily' or 'cumulative'
            order_by: Sort field
            direction: Sort direction
            limit: Maximum results
            
        Returns:
            List of Pack analytics items
        """
        params = {
            "packIds": pack_ids,
            "workspaceId": workspace_id,
            "query": query,
            "isPublished": is_published,
            "sinceDate": since_date,
            "untilDate": until_date,
            "scale": scale,
            "orderBy": order_by,
            "direction": direction,
            "limit": min(limit, 5000)
        }
        
        return self._collect_pages("/analytics/packs", params, limit=limit)
    
    def get_pack_analytics_summary(
        self,
        pack_ids: Optional[List[int]] = None,
        workspace_id: Optional[str] = None,
        is_published: Optional[bool] = None,
        since_date: Optional[str] = None,
        until_date: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get summarized Pack analytics.
        
        Args:
            pack_ids: Filter by Pack IDs
            workspace_id: Filter by workspace
            is_published: Published only
            since_date: Start date
            until_date: End date
            
        Returns:
            Summary with totalDocInstalls, totalInvocations
        """
        params = {
            "packIds": pack_ids,
            "workspaceId": workspace_id,
            "isPublished": is_published,
            "sinceDate": since_date,
            "untilDate": until_date
        }
        
        return self._get("/analytics/packs/summary", params={k: v for k, v in params.items() if v is not None})
    
    def list_pack_formula_analytics(
        self,
        pack_id: int,
        formula_names: Optional[List[str]] = None,
        formula_types: Optional[List[str]] = None,
        since_date: Optional[str] = None,
        until_date: Optional[str] = None,
        scale: AnalyticsScale = "daily",
        order_by: Optional[str] = None,
        direction: Optional[SortDirection] = None,
        limit: int = 1000
    ) -> List[Dict[str, Any]]:
        """
        Get Pack formula analytics.
        
        Args:
            pack_id: Pack ID
            formula_names: Filter by formula names
            formula_types: Filter by types (action, formula, sync, metadata)
            since_date: Start date
            until_date: End date
            scale: Quantization period
            order_by: Sort field
            direction: Sort direction
            limit: Maximum results
            
        Returns:
            List of formula analytics items
        """
        params = {
            "packFormulaNames": ",".join(formula_names) if formula_names else None,
            "packFormulaTypes": ",".join(formula_types) if formula_types else None,
            "sinceDate": since_date,
            "untilDate": until_date,
            "scale": scale,
            "orderBy": order_by,
            "direction": direction,
            "limit": min(limit, 5000)
        }
        
        return self._collect_pages(f"/analytics/packs/{pack_id}/formulas", params, limit=limit)
    
    def get_analytics_last_updated(self) -> Dict[str, Any]:
        """
        Get when analytics were last updated.
        
        Returns:
            Dict with docAnalyticsLastUpdated, packAnalyticsLastUpdated dates
        """
        return self._get("/analytics/updated")
