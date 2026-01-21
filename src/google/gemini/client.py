from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleGeminiClient(UniversalGoogleClient):
    """
    Client for the generativelanguage API (v1beta).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='generativelanguage', version='v1beta')

    def list_models(self) -> List[Dict[str, Any]]:
        """List available Gemini models."""
        if not self.is_ready():
            return []
        result = self.service.models().list().execute()
        return result.get("models", [])

    def generate_content(self, model: str, contents: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """Generate content with Gemini."""
        if not self.is_ready():
            return None
        return self.service.models().generateContent(model=model, body={"contents": contents}).execute()

