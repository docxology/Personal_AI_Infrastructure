from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleGroupsClient(UniversalGoogleClient):
    """
    Client for the groupssettings API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='groupssettings', version='v1')

    def get_group(self, group_email: str) -> Optional[Dict[str, Any]]:
        """Get group settings."""
        if not self.is_ready():
            return None
        return self.service.groups().get(groupUniqueId=group_email).execute()

