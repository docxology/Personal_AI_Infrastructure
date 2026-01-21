from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleWalletClient(UniversalGoogleClient):
    """
    Client for the walletobjects API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='walletobjects', version='v1')

    def list_loyalty_classes(self, issuer_id: str) -> List[Dict[str, Any]]:
        """List loyalty classes."""
        if not self.is_ready():
            return []
        result = self.service.loyaltyclass().list(issuerId=issuer_id).execute()
        return result.get("resources", [])

