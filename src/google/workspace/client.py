from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleWorkspaceClient(UniversalGoogleClient):
    """
    Client for the workspaceevents API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='workspaceevents', version='v1')

    def list_subscriptions(self) -> List[Dict[str, Any]]:
        """List event subscriptions."""
        if not self.is_ready():
            return []
        result = self.service.subscriptions().list().execute()
        return result.get("subscriptions", [])

