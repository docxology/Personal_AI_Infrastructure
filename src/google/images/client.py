from google.universal_client import UniversalGoogleClient

class GoogleImagesClient(UniversalGoogleClient):
    """
    Client for images.
    Note: Exact API match not found automatically. defaulting to generic configuration.
    User/Dev should verify 'service_name' and 'version'.
    """
    def __init__(self, service_name='images', version='v1'):
        super().__init__(service_name=service_name, version=version)
