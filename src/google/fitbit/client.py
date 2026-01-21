from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleFitbitClient(UniversalGoogleClient):
    """
    Client for the fitness API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='fitness', version='v1')

    def list_data_sources(self) -> List[Dict[str, Any]]:
        """List fitness data sources."""
        if not self.is_ready():
            return []
        result = self.service.users().dataSources().list(userId="me").execute()
        return result.get("dataSource", [])

