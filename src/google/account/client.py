from google.universal_client import UniversalGoogleClient

class GoogleAccountClient(UniversalGoogleClient):
    """
    Client for the My Business Account Management API (mybusinessaccountmanagement v1).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='mybusinessaccountmanagement', version='v1')
