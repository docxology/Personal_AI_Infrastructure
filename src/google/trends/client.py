from google.universal_client import UniversalGoogleClient

class GoogleTrendsClient(UniversalGoogleClient):
    """
    Client for trends.
    Note: Exact API match not found automatically. defaulting to generic configuration.
    User/Dev should verify 'service_name' and 'version'.
    """
    def __init__(self, service_name='trends', version='v1'):
        super().__init__(service_name=service_name, version=version)
