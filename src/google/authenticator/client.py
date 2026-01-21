from google.universal_client import UniversalGoogleClient

class GoogleAuthenticatorClient(UniversalGoogleClient):
    """
    Client for authenticator.
    Note: Exact API match not found automatically. defaulting to generic configuration.
    User/Dev should verify 'service_name' and 'version'.
    """
    def __init__(self, service_name='authenticator', version='v1'):
        super().__init__(service_name=service_name, version=version)
