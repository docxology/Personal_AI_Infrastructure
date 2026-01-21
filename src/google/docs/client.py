from google.universal_client import UniversalGoogleClient
from typing import Dict, Any, Optional, List

class GoogleDocsClient(UniversalGoogleClient):
    """
    Client for the Google Docs API (docs v1).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='docs', version='v1')

    def get_document(self, document_id: str) -> Optional[Dict[str, Any]]:
        """Get a document by ID."""
        if not self.is_ready():
            return None
        return self.service.documents().get(documentId=document_id).execute()

    def create_document(self, title: str) -> Optional[Dict[str, Any]]:
        """Create a new document."""
        if not self.is_ready():
            return None
        body = {'title': title}
        return self.service.documents().create(body=body).execute()

    def batch_update(self, document_id: str, requests: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Apply batch updates to a document."""
        if not self.is_ready():
            return {}
        body = {'requests': requests}
        return self.service.documents().batchUpdate(documentId=document_id, body=body).execute()
