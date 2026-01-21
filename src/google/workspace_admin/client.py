from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleWorkspaceAdminClient(UniversalGoogleClient):
    """
    Client for the admin API (directory_v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='admin', version='directory_v1')

    def list_users(self) -> List[Dict[str, Any]]:
        """List users in the domain."""
        if not self.is_ready():
            return []
        result = self.service.users().list(customer="my_customer").execute()
        return result.get("users", [])

    def get_user(self, user_email: str) -> Optional[Dict[str, Any]]:
        """Get a user by email."""
        if not self.is_ready():
            return None
        return self.service.users().get(userKey=user_email).execute()

    def list_groups(self) -> List[Dict[str, Any]]:
        """List groups in the domain."""
        if not self.is_ready():
            return []
        result = self.service.groups().list(customer="my_customer").execute()
        return result.get("groups", [])

