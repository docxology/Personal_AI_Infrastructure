from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any

class GoogleAnalyticsClient(UniversalGoogleClient):
    """
    Client for the Google Analytics API (analytics v3).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='analytics', version='v3')

    def list_accounts(self) -> List[Dict[str, Any]]:
        """List all Analytics accounts accessible by the user."""
        if not self.is_ready():
            return []
        result = self.service.management().accounts().list().execute()
        return result.get('items', [])

    def list_properties(self, account_id: str) -> List[Dict[str, Any]]:
        """List web properties for an account."""
        if not self.is_ready():
            return []
        result = self.service.management().webproperties().list(accountId=account_id).execute()
        return result.get('items', [])

    def list_profiles(self, account_id: str, property_id: str) -> List[Dict[str, Any]]:
        """List profiles (views) for a property."""
        if not self.is_ready():
            return []
        result = self.service.management().profiles().list(
            accountId=account_id,
            webPropertyId=property_id
        ).execute()
        return result.get('items', [])
