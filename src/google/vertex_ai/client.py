from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleVertexAiClient(UniversalGoogleClient):
    """
    Client for the aiplatform API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='aiplatform', version='v1')

    def list_models(self, parent: str) -> List[Dict[str, Any]]:
        """List models in a project."""
        if not self.is_ready():
            return []
        result = self.service.projects().locations().models().list(parent=parent).execute()
        return result.get("models", [])

    def list_endpoints(self, parent: str) -> List[Dict[str, Any]]:
        """List endpoints."""
        if not self.is_ready():
            return []
        result = self.service.projects().locations().endpoints().list(parent=parent).execute()
        return result.get("endpoints", [])

    def predict(self, endpoint: str, instances: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Make a prediction."""
        if not self.is_ready():
            return None
        return self.service.projects().locations().endpoints().predict(endpoint=endpoint, body={"instances": instances}).execute()

