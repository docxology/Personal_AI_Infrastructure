from google.universal_client import UniversalGoogleClient

class GoogleOneClient(UniversalGoogleClient):
    """
    Client for the Recommendations AI (Beta) (recommendationengine v1beta1).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='recommendationengine', version='v1beta1')
