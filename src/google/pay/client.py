from google.universal_client import UniversalGoogleClient

class GooglePayClient(UniversalGoogleClient):
    """
    Client for the Payments Reseller Subscription API (paymentsresellersubscription v1).
    Auto-generated.
    """
    def __init__(self):
        super().__init__(service_name='paymentsresellersubscription', version='v1')
