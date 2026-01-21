from google.universal_client import UniversalGoogleClient

class GoogleAiForDevelopersClient(UniversalGoogleClient):
    """
    Client for ai_for_developers.
    Note: Exact API match not found automatically. defaulting to generic configuration.
    User/Dev should verify 'service_name' and 'version'.
    """
    def __init__(self, service_name='aifordevelopers', version='v1'):
        super().__init__(service_name=service_name, version=version)
