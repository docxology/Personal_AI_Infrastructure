from google.universal_client import UniversalGoogleClient

class GoogleSearchClient(UniversalGoogleClient):
    """
    Client for the Cloud Search API (cloudsearch v1).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='cloudsearch', version='v1')
