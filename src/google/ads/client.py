from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleAdsClient(UniversalGoogleClient):
    """
    Client for the adsense API (v2).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='adsense', version='v2')

    def list_accounts(self) -> List[Dict[str, Any]]:
        """List ad accounts."""
        if not self.is_ready():
            return []
        result = self.service.accounts().list().execute()
        return result.get("accounts", [])

