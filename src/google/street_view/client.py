from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleStreetViewClient(UniversalGoogleClient):
    """
    Client for the streetviewpublish API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='streetviewpublish', version='v1')

    def list_photos(self, page_size: int = 100) -> List[Dict[str, Any]]:
        """List published photos."""
        if not self.is_ready():
            return []
        result = self.service.photos().list(pageSize=page_size).execute()
        return result.get("photos", [])

    def get_photo(self, photo_id: str) -> Optional[Dict[str, Any]]:
        """Get a photo by ID."""
        if not self.is_ready():
            return None
        return self.service.photo().get(photoId=photo_id).execute()

