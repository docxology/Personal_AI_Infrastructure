from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleAdsenseClient(UniversalGoogleClient):
    """
    Client for the adsense API (v2).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='adsense', version='v2')

    def list_accounts(self) -> List[Dict[str, Any]]:
        """List AdSense accounts."""
        if not self.is_ready():
            return []
        result = self.service.accounts().list().execute()
        return result.get("accounts", [])

    def get_account(self, account_name: str) -> Optional[Dict[str, Any]]:
        """Get an AdSense account."""
        if not self.is_ready():
            return None
        return self.service.accounts().get(name=account_name).execute()

