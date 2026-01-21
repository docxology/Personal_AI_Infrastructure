from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleChatClient(UniversalGoogleClient):
    """
    Client for the chat API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='chat', version='v1')

    def list_spaces(self) -> List[Dict[str, Any]]:
        """List all Chat spaces."""
        if not self.is_ready():
            return []
        result = self.service.spaces().list().execute()
        return result.get("spaces", [])

    def get_space(self, space_name: str) -> Optional[Dict[str, Any]]:
        """Get a specific space."""
        if not self.is_ready():
            return None
        return self.service.spaces().get(name=space_name).execute()

    def create_message(self, space_name: str, text: str) -> Optional[Dict[str, Any]]:
        """Create a message in a space."""
        if not self.is_ready():
            return None
        return self.service.spaces().messages().create(parent=space_name, body={"text": text}).execute()

