from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleMeetClient(UniversalGoogleClient):
    """
    Client for the Google Meet API (meet v2).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='meet', version='v2')

    def get_space(self, space_name: str) -> Optional[Dict[str, Any]]:
        """Get a meeting space by name (format: spaces/{space})."""
        if not self.is_ready():
            return None
        return self.service.spaces().get(name=space_name).execute()

    def create_space(self) -> Optional[Dict[str, Any]]:
        """Create a new meeting space."""
        if not self.is_ready():
            return None
        return self.service.spaces().create(body={}).execute()

    def end_active_conference(self, space_name: str) -> Dict[str, Any]:
        """End an active conference in a space."""
        if not self.is_ready():
            return {}
        return self.service.spaces().endActiveConference(name=space_name, body={}).execute()
