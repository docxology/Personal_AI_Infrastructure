from google.universal_client import UniversalGoogleClient

class GooglePlayClient(UniversalGoogleClient):
    """
    Client for the Display & Video 360 API (displayvideo v4).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='displayvideo', version='v4')
