from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleMerchantCenterClient(UniversalGoogleClient):
    """
    Client for the content API (v2.1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='content', version='v2.1')

    def list_products(self, merchant_id: str) -> List[Dict[str, Any]]:
        """List products."""
        if not self.is_ready():
            return []
        result = self.service.products().list(merchantId=merchant_id).execute()
        return result.get("resources", [])

    def get_product(self, merchant_id: str, product_id: str) -> Optional[Dict[str, Any]]:
        """Get a product."""
        if not self.is_ready():
            return None
        return self.service.products().get(merchantId=merchant_id, productId=product_id).execute()

