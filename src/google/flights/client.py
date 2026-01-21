from google.universal_client import UniversalGoogleClient

class GoogleFlightsClient(UniversalGoogleClient):
    """
    Client for flights.
    Note: Exact API match not found automatically. defaulting to generic configuration.
    User/Dev should verify 'service_name' and 'version'.
    """
    def __init__(self, service_name='flights', version='v1'):
        super().__init__(service_name=service_name, version=version)
