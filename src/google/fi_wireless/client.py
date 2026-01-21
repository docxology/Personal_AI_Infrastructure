from google.universal_client import UniversalGoogleClient

class GoogleFiWirelessClient(UniversalGoogleClient):
    """
    Client for fi_wireless.
    Note: Exact API match not found automatically. defaulting to generic configuration.
    User/Dev should verify 'service_name' and 'version'.
    """
    def __init__(self, service_name='fiwireless', version='v1'):
        super().__init__(service_name=service_name, version=version)
