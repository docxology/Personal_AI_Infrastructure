"""
Coda Formulas Client

Named formula operations.
"""

from typing import Dict, Any, List, Optional
from coda.base_client import CodaClient


class CodaFormulasClient(CodaClient):
    """
    Client for Coda formula operations.
    """
    
    def list_formulas(
        self,
        doc_id: str,
        sort_by: Optional[str] = None,
        limit: int = 25
    ) -> List[Dict[str, Any]]:
        """
        List named formulas in a doc.
        
        Args:
            doc_id: ID of the doc
            sort_by: Sort order ('name')
            limit: Maximum results
            
        Returns:
            List of formula references
        """
        params = {
            "limit": limit,
            "sortBy": sort_by
        }
        
        return self._collect_pages(f"/docs/{doc_id}/formulas", params, limit=limit)
    
    def get_formula(
        self,
        doc_id: str,
        formula_id_or_name: str
    ) -> Dict[str, Any]:
        """
        Get a formula with its computed value.
        
        Args:
            doc_id: ID of the doc
            formula_id_or_name: Formula ID or URL-encoded name
            
        Returns:
            Formula metadata with value
        """
        return self._get(f"/docs/{doc_id}/formulas/{formula_id_or_name}")
    
    def get_formula_value(
        self,
        doc_id: str,
        formula_id_or_name: str
    ) -> Any:
        """
        Get only the computed value of a formula.
        
        Args:
            doc_id: ID of the doc
            formula_id_or_name: Formula ID or name
            
        Returns:
            Computed value
        """
        formula = self.get_formula(doc_id, formula_id_or_name)
        return formula.get("value")
