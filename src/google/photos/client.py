from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GooglePhotosClient(UniversalGoogleClient):
    """
    Client for Photos Library API (photoslibrary v1).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='photoslibrary', version='v1')

    def list_albums(self, page_size: int = 50) -> List[Dict[str, Any]]:
        """List user's photo albums."""
        if not self.is_ready():
            return []
        result = self.service.albums().list(pageSize=page_size).execute()
        return result.get('albums', [])

    def get_album(self, album_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific album by ID."""
        if not self.is_ready():
            return None
        return self.service.albums().get(albumId=album_id).execute()

    def search_media(self, filters: Dict[str, Any] = None, page_size: int = 100) -> List[Dict[str, Any]]:
        """Search for media items with optional filters."""
        if not self.is_ready():
            return []
        body = {'pageSize': page_size}
        if filters:
            body['filters'] = filters
        result = self.service.mediaItems().search(body=body).execute()
        return result.get('mediaItems', [])
