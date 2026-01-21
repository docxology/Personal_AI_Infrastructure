from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleBooksClient(UniversalGoogleClient):
    """
    Client for the Books API (books v1).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='books', version='v1')

    def search_volumes(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Search for books/volumes."""
        if not self.is_ready():
            return []
        result = self.service.volumes().list(q=query, maxResults=max_results).execute()
        return result.get('items', [])

    def get_volume(self, volume_id: str) -> Optional[Dict[str, Any]]:
        """Get details for a specific volume."""
        if not self.is_ready():
            return None
        return self.service.volumes().get(volumeId=volume_id).execute()

    def list_bookshelves(self, user_id: str = 'me') -> List[Dict[str, Any]]:
        """List bookshelves for a user."""
        if not self.is_ready():
            return []
        result = self.service.mylibrary().bookshelves().list().execute()
        return result.get('items', [])
