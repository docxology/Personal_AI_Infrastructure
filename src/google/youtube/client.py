from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional
import logging

class GoogleYoutubeClient(UniversalGoogleClient):
    """
    Client for the YouTube Data API v3 (youtube v3).
    Enhanced with comprehensive convenience methods for:
    - Video search and retrieval
    - Playlist management
    - Channel operations
    - Comments and subscriptions
    - Captions and statistics
    """
    def __init__(self):
        super().__init__(service_name='youtube', version='v3')

    # =====================
    # Search & Videos
    # =====================

    def search(self, query: str, max_results: int = 10, 
               type: str = 'video', order: str = 'relevance') -> List[Dict[str, Any]]:
        """
        Search YouTube for videos, channels, or playlists.
        
        Args:
            query: Search query string
            max_results: Maximum number of results (1-50)
            type: Content type - 'video', 'channel', 'playlist', or comma-separated combo
            order: Result ordering - 'relevance', 'date', 'rating', 'viewCount', 'title'
        """
        if not self.is_ready():
            return []
        response = self.service.search().list(
            q=query,
            part='snippet',
            maxResults=max_results,
            type=type,
            order=order
        ).execute()
        return response.get('items', [])

    def get_video(self, video_id: str) -> Optional[Dict[str, Any]]:
        """Get full details for a specific video including snippet, content details, and statistics."""
        if not self.is_ready():
            return None
        response = self.service.videos().list(
            id=video_id,
            part='snippet,contentDetails,statistics,status'
        ).execute()
        items = response.get('items', [])
        return items[0] if items else None

    def get_videos_batch(self, video_ids: List[str]) -> List[Dict[str, Any]]:
        """Get details for multiple videos in a single request (max 50)."""
        if not self.is_ready():
            return []
        response = self.service.videos().list(
            id=','.join(video_ids[:50]),
            part='snippet,contentDetails,statistics'
        ).execute()
        return response.get('items', [])

    def get_video_statistics(self, video_ids: List[str]) -> List[Dict[str, Any]]:
        """Get statistics (views, likes, comments) for multiple videos."""
        if not self.is_ready():
            return []
        response = self.service.videos().list(
            id=','.join(video_ids[:50]),
            part='statistics'
        ).execute()
        return response.get('items', [])

    # =====================
    # Channels
    # =====================

    def list_channels(self, channel_ids: List[str]) -> List[Dict[str, Any]]:
        """Get channel details for given channel IDs."""
        if not self.is_ready():
            return []
        response = self.service.channels().list(
            id=','.join(channel_ids),
            part='snippet,statistics,contentDetails'
        ).execute()
        return response.get('items', [])

    def get_channel_by_username(self, username: str) -> Optional[Dict[str, Any]]:
        """Get channel details by username/handle."""
        if not self.is_ready():
            return None
        response = self.service.channels().list(
            forHandle=username,
            part='snippet,statistics,contentDetails'
        ).execute()
        items = response.get('items', [])
        return items[0] if items else None

    def get_my_channel(self) -> Optional[Dict[str, Any]]:
        """Get the authenticated user's channel."""
        if not self.is_ready():
            return None
        response = self.service.channels().list(
            mine=True,
            part='snippet,statistics,contentDetails'
        ).execute()
        items = response.get('items', [])
        return items[0] if items else None

    def list_channel_videos(self, channel_id: str, max_results: int = 25,
                            order: str = 'date') -> List[Dict[str, Any]]:
        """List videos from a specific channel."""
        if not self.is_ready():
            return []
        response = self.service.search().list(
            channelId=channel_id,
            type='video',
            part='snippet',
            maxResults=max_results,
            order=order
        ).execute()
        return response.get('items', [])

    # =====================
    # Playlists
    # =====================

    def list_playlists(self, channel_id: str, max_results: int = 25) -> List[Dict[str, Any]]:
        """List playlists for a channel."""
        if not self.is_ready():
            return []
        response = self.service.playlists().list(
            channelId=channel_id,
            part='snippet,contentDetails',
            maxResults=max_results
        ).execute()
        return response.get('items', [])

    def get_my_playlists(self, max_results: int = 25) -> List[Dict[str, Any]]:
        """List the authenticated user's playlists."""
        if not self.is_ready():
            return []
        response = self.service.playlists().list(
            mine=True,
            part='snippet,contentDetails',
            maxResults=max_results
        ).execute()
        return response.get('items', [])

    def create_playlist(self, title: str, description: str = '',
                        privacy_status: str = 'private') -> Optional[Dict[str, Any]]:
        """
        Create a new playlist.
        
        Args:
            title: Playlist title
            description: Playlist description
            privacy_status: 'public', 'private', or 'unlisted'
        """
        if not self.is_ready():
            return None
        body = {
            'snippet': {
                'title': title,
                'description': description
            },
            'status': {
                'privacyStatus': privacy_status
            }
        }
        response = self.service.playlists().insert(
            part='snippet,status',
            body=body
        ).execute()
        return response

    def delete_playlist(self, playlist_id: str) -> bool:
        """Delete a playlist."""
        if not self.is_ready():
            return False
        try:
            self.service.playlists().delete(id=playlist_id).execute()
            return True
        except Exception:
            return False

    def list_playlist_items(self, playlist_id: str, max_results: int = 50) -> List[Dict[str, Any]]:
        """List all items in a playlist."""
        if not self.is_ready():
            return []
        response = self.service.playlistItems().list(
            playlistId=playlist_id,
            part='snippet,contentDetails',
            maxResults=max_results
        ).execute()
        return response.get('items', [])

    def add_to_playlist(self, playlist_id: str, video_id: str,
                        position: Optional[int] = None) -> Optional[Dict[str, Any]]:
        """Add a video to a playlist."""
        if not self.is_ready():
            return None
        body = {
            'snippet': {
                'playlistId': playlist_id,
                'resourceId': {
                    'kind': 'youtube#video',
                    'videoId': video_id
                }
            }
        }
        if position is not None:
            body['snippet']['position'] = position
        
        response = self.service.playlistItems().insert(
            part='snippet',
            body=body
        ).execute()
        return response

    def remove_from_playlist(self, playlist_item_id: str) -> bool:
        """Remove an item from a playlist by its playlist item ID."""
        if not self.is_ready():
            return False
        try:
            self.service.playlistItems().delete(id=playlist_item_id).execute()
            return True
        except Exception:
            return False

    # =====================
    # Subscriptions
    # =====================

    def list_subscriptions(self, channel_id: Optional[str] = None, 
                           max_results: int = 25) -> List[Dict[str, Any]]:
        """
        List subscriptions. If channel_id is None, lists authenticated user's subscriptions.
        """
        if not self.is_ready():
            return []
        params = {
            'part': 'snippet',
            'maxResults': max_results
        }
        if channel_id:
            params['channelId'] = channel_id
        else:
            params['mine'] = True
        
        response = self.service.subscriptions().list(**params).execute()
        return response.get('items', [])

    def subscribe(self, channel_id: str) -> Optional[Dict[str, Any]]:
        """Subscribe to a channel."""
        if not self.is_ready():
            return None
        body = {
            'snippet': {
                'resourceId': {
                    'kind': 'youtube#channel',
                    'channelId': channel_id
                }
            }
        }
        response = self.service.subscriptions().insert(
            part='snippet',
            body=body
        ).execute()
        return response

    def unsubscribe(self, subscription_id: str) -> bool:
        """Unsubscribe by subscription ID."""
        if not self.is_ready():
            return False
        try:
            self.service.subscriptions().delete(id=subscription_id).execute()
            return True
        except Exception:
            return False

    # =====================
    # Comments
    # =====================

    def list_comments(self, video_id: str, max_results: int = 20,
                      order: str = 'relevance') -> List[Dict[str, Any]]:
        """
        List top-level comment threads for a video.
        
        Args:
            order: 'time' or 'relevance'
        """
        if not self.is_ready():
            return []
        response = self.service.commentThreads().list(
            videoId=video_id,
            part='snippet',
            maxResults=max_results,
            order=order
        ).execute()
        return response.get('items', [])

    def get_comment_threads(self, video_id: str, max_results: int = 20) -> List[Dict[str, Any]]:
        """Get comment threads including replies for a video."""
        if not self.is_ready():
            return []
        response = self.service.commentThreads().list(
            videoId=video_id,
            part='snippet,replies',
            maxResults=max_results
        ).execute()
        return response.get('items', [])

    def add_comment(self, video_id: str, text: str) -> Optional[Dict[str, Any]]:
        """Add a top-level comment to a video."""
        if not self.is_ready():
            return None
        body = {
            'snippet': {
                'videoId': video_id,
                'topLevelComment': {
                    'snippet': {
                        'textOriginal': text
                    }
                }
            }
        }
        response = self.service.commentThreads().insert(
            part='snippet',
            body=body
        ).execute()
        return response

    def reply_to_comment(self, parent_id: str, text: str) -> Optional[Dict[str, Any]]:
        """Reply to an existing comment."""
        if not self.is_ready():
            return None
        body = {
            'snippet': {
                'parentId': parent_id,
                'textOriginal': text
            }
        }
        response = self.service.comments().insert(
            part='snippet',
            body=body
        ).execute()
        return response

    # =====================
    # Captions
    # =====================

    def list_captions(self, video_id: str) -> List[Dict[str, Any]]:
        """List available captions/subtitles for a video."""
        if not self.is_ready():
            return []
        response = self.service.captions().list(
            videoId=video_id,
            part='snippet'
        ).execute()
        return response.get('items', [])

    def download_caption(self, caption_id: str, tfmt: str = 'srt') -> Optional[str]:
        """
        Download caption content.
        
        Args:
            caption_id: The caption track ID
            tfmt: Format - 'sbv', 'scc', 'srt', 'ttml', 'vtt'
        
        Note: Requires caption owner or authorized credentials.
        """
        if not self.is_ready():
            return None
        try:
            response = self.service.captions().download(
                id=caption_id,
                tfmt=tfmt
            ).execute()
            return response.decode('utf-8') if isinstance(response, bytes) else response
        except Exception as e:
            logging.error(f"Caption download error: {e}")
            return None

