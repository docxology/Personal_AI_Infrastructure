from google.universal_client import UniversalGoogleClient
from typing import Dict, Any, Optional, List

class GoogleSlidesClient(UniversalGoogleClient):
    """
    Client for the Google Slides API (slides v1).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='slides', version='v1')

    def get_presentation(self, presentation_id: str) -> Optional[Dict[str, Any]]:
        """Get a presentation by ID."""
        if not self.is_ready():
            return None
        return self.service.presentations().get(presentationId=presentation_id).execute()

    def create_presentation(self, title: str) -> Optional[Dict[str, Any]]:
        """Create a new presentation."""
        if not self.is_ready():
            return None
        body = {'title': title}
        return self.service.presentations().create(body=body).execute()

    def batch_update(self, presentation_id: str, requests: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Apply batch updates to a presentation."""
        if not self.is_ready():
            return {}
        body = {'requests': requests}
        return self.service.presentations().batchUpdate(presentationId=presentation_id, body=body).execute()
