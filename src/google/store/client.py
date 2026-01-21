from google.universal_client import UniversalGoogleClient

class GoogleStoreClient(UniversalGoogleClient):
    """
    Client for the Chrome Web Store API (chromewebstore v2).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='chromewebstore', version='v2')
