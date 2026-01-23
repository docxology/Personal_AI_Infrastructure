"""
Coda Miscellaneous Client

Utility operations.
"""

from typing import Dict, Any
from coda.base_client import CodaClient


class CodaMiscClient(CodaClient):
    """
    Client for Coda miscellaneous operations.
    
    Inherits resolve_browser_link() and get_mutation_status() from CodaClient.
    """
    
    def wait_for_mutation(
        self,
        request_id: str,
        max_attempts: int = 30,
        poll_interval: float = 1.0
    ) -> bool:
        """
        Wait for an async mutation to complete.
        
        Args:
            request_id: ID from mutation response
            max_attempts: Maximum poll attempts
            poll_interval: Seconds between polls
            
        Returns:
            True if completed, False if timed out
        """
        import time
        
        for _ in range(max_attempts):
            status = self.get_mutation_status(request_id)
            if status.get("completed"):
                return True
            time.sleep(poll_interval)
        
        return False
    
    def get_resource_from_url(self, url: str) -> Dict[str, Any]:
        """
        Get API resource info from a browser URL.
        
        Args:
            url: Coda browser URL
            
        Returns:
            Resource info with type, id, name, href
        """
        result = self.resolve_browser_link(url)
        return result.get("resource", {})
    
    def get_doc_id_from_url(self, url: str) -> str:
        """
        Extract doc ID from a browser URL via API.
        
        Args:
            url: Coda browser URL
            
        Returns:
            Doc ID
        """
        resource = self.get_resource_from_url(url)
        # Walk up to find doc
        href = resource.get("href", "")
        if "/docs/" in href:
            parts = href.split("/docs/")[1].split("/")
            return parts[0]
        return ""
