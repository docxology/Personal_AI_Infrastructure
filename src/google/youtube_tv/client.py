from google.universal_client import UniversalGoogleClient

class GoogleYoutubeTvClient(UniversalGoogleClient):
    """
    Client for the YouTube Data API v3 (youtube v3).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='youtube', version='v3')
