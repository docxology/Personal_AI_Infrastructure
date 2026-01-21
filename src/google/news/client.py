from google.universal_client import UniversalGoogleClient

class GoogleNewsClient(UniversalGoogleClient):
    """
    Client for civicinfo (v2).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='civicinfo', version='v2')
