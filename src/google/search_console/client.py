from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleSearchConsoleClient(UniversalGoogleClient):
    """
    Client for the searchconsole API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='searchconsole', version='v1')

    def list_sites(self) -> List[Dict[str, Any]]:
        """List verified sites."""
        if not self.is_ready():
            return []
        result = self.service.sites().list().execute()
        return result.get("siteEntry", [])

    def search_analytics(self, site_url: str, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Query search analytics data."""
        if not self.is_ready():
            return None
        return self.service.searchanalytics().query(siteUrl=site_url, body=query).execute()

