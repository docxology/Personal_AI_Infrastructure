from google.universal_client import UniversalGoogleClient

class GoogleAndroidStudioClient(UniversalGoogleClient):
    """
    Client for the Cloud IDS API (ids v1).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='ids', version='v1')
