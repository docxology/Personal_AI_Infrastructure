"""
Coda Controls Client

Control (input) operations.
"""

from typing import Dict, Any, List, Optional
from coda.base_client import CodaClient


class CodaControlsClient(CodaClient):
    """
    Client for Coda control operations.
    """
    
    def list_controls(
        self,
        doc_id: str,
        sort_by: Optional[str] = None,
        limit: int = 25
    ) -> List[Dict[str, Any]]:
        """
        List controls in a doc.
        
        Args:
            doc_id: ID of the doc
            sort_by: Sort order ('name')
            limit: Maximum results
            
        Returns:
            List of control references
        """
        params = {
            "limit": limit,
            "sortBy": sort_by
        }
        
        return self._collect_pages(f"/docs/{doc_id}/controls", params, limit=limit)
    
    def get_control(
        self,
        doc_id: str,
        control_id_or_name: str
    ) -> Dict[str, Any]:
        """
        Get a control with its current value.
        
        Args:
            doc_id: ID of the doc
            control_id_or_name: Control ID or URL-encoded name
            
        Returns:
            Control metadata with value and type
        """
        return self._get(f"/docs/{doc_id}/controls/{control_id_or_name}")
    
    def get_control_value(
        self,
        doc_id: str,
        control_id_or_name: str
    ) -> Any:
        """
        Get only the current value of a control.
        
        Args:
            doc_id: ID of the doc
            control_id_or_name: Control ID or name
            
        Returns:
            Current value
        """
        control = self.get_control(doc_id, control_id_or_name)
        return control.get("value")
    
    def list_controls_by_type(
        self,
        doc_id: str,
        control_type: str
    ) -> List[Dict[str, Any]]:
        """
        List controls of a specific type.
        
        Args:
            doc_id: ID of the doc
            control_type: Type (button, checkbox, datePicker, etc.)
            
        Returns:
            Matching controls
        """
        controls = self.list_controls(doc_id, limit=100)
        return [c for c in controls if c.get("controlType") == control_type]
