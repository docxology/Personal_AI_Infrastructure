from google.universal_client import UniversalGoogleClient

class GooglePodcastsClient(UniversalGoogleClient):
    """
    Client for the Security Token Service API (sts v1).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='sts', version='v1')
