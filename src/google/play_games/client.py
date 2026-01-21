from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GooglePlayGamesClient(UniversalGoogleClient):
    """
    Client for the games API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='games', version='v1')

    def list_achievements(self, app_id: str) -> List[Dict[str, Any]]:
        """List achievements for an app."""
        if not self.is_ready():
            return []
        result = self.service.achievementDefinitions().list(applicationId=app_id).execute()
        return result.get("items", [])

    def list_leaderboards(self, app_id: str) -> List[Dict[str, Any]]:
        """List leaderboards."""
        if not self.is_ready():
            return []
        result = self.service.leaderboards().list(applicationId=app_id).execute()
        return result.get("items", [])

