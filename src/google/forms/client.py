from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleFormsClient(UniversalGoogleClient):
    """
    Client for the forms API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='forms', version='v1')

    def get_form(self, form_id: str) -> Optional[Dict[str, Any]]:
        """Get a form by ID."""
        if not self.is_ready():
            return None
        return self.service.forms().get(formId=form_id).execute()

    def list_responses(self, form_id: str) -> List[Dict[str, Any]]:
        """List form responses."""
        if not self.is_ready():
            return []
        result = self.service.forms().responses().list(formId=form_id).execute()
        return result.get("responses", [])

