from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleAdManagerClient(UniversalGoogleClient):
    """
    Client for the adexchangebuyer API (v1.4).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='adexchangebuyer', version='v1.4')

    def list_accounts(self) -> List[Dict[str, Any]]:
        """List buyer accounts."""
        if not self.is_ready():
            return []
        result = self.service.accounts().list().execute()
        return result.get("items", [])

