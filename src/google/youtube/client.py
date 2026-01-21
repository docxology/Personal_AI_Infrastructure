from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleYoutubeClient(UniversalGoogleClient):
    """
    Client for the YouTube Data API v3 (youtube v3).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='youtube', version='v3')

    def search(self, query: str, max_results: int = 10, type: str = 'video') -> List[Dict[str, Any]]:
        """Search YouTube for videos, channels, or playlists."""
        if not self.is_ready():
            return []
        response = self.service.search().list(
            q=query,
            part='snippet',
            maxResults=max_results,
            type=type
        ).execute()
        return response.get('items', [])

    def get_video(self, video_id: str) -> Optional[Dict[str, Any]]:
        """Get details for a specific video."""
        if not self.is_ready():
            return None
        response = self.service.videos().list(
            id=video_id,
            part='snippet,contentDetails,statistics'
        ).execute()
        items = response.get('items', [])
        return items[0] if items else None

    def list_channels(self, channel_ids: List[str]) -> List[Dict[str, Any]]:
        """Get channel details for given channel IDs."""
        if not self.is_ready():
            return []
        response = self.service.channels().list(
            id=','.join(channel_ids),
            part='snippet,statistics'
        ).execute()
        return response.get('items', [])

    def list_playlists(self, channel_id: str, max_results: int = 25) -> List[Dict[str, Any]]:
        """List playlists for a channel."""
        if not self.is_ready():
            return []
        response = self.service.playlists().list(
            channelId=channel_id,
            part='snippet',
            maxResults=max_results
        ).execute()
        return response.get('items', [])
