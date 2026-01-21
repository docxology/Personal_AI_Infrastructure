from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleContactsClient(UniversalGoogleClient):
    """
    Client for the people API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='people', version='v1')

    def list_connections(self) -> List[Dict[str, Any]]:
        """List user contacts."""
        if not self.is_ready():
            return []
        result = self.service.people().connections().list(resourceName="people/me", personFields="names,emailAddresses").execute()
        return result.get("connections", [])

    def get_person(self, resource_name: str) -> Optional[Dict[str, Any]]:
        """Get a person by resource name."""
        if not self.is_ready():
            return None
        return self.service.people().get(resourceName=resource_name, personFields="names,emailAddresses,phoneNumbers").execute()

