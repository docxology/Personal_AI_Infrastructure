from google.universal_client import UniversalGoogleClient

class GoogleMapsClient(UniversalGoogleClient):
    """
    Client for googlemaps (v1).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='googlemaps', version='v1')
