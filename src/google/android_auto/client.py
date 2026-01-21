from google.universal_client import UniversalGoogleClient

class GoogleAndroidAutoClient(UniversalGoogleClient):
    """
    Client for android_auto.
    Note: Exact API match not found automatically. defaulting to generic configuration.
    User/Dev should verify 'service_name' and 'version'.
    """
    def __init__(self, service_name='androidauto', version='v1'):
        super().__init__(service_name=service_name, version=version)
