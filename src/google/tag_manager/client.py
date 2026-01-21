from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleTagManagerClient(UniversalGoogleClient):
    """
    Client for the tagmanager API (v2).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='tagmanager', version='v2')

    def list_accounts(self) -> List[Dict[str, Any]]:
        """List Tag Manager accounts."""
        if not self.is_ready():
            return []
        result = self.service.accounts().list().execute()
        return result.get("account", [])

    def list_containers(self, account_path: str) -> List[Dict[str, Any]]:
        """List containers for an account."""
        if not self.is_ready():
            return []
        result = self.service.accounts().containers().list(parent=account_path).execute()
        return result.get("container", [])

