from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleKeepClient(UniversalGoogleClient):
    """
    Client for the Google Keep API (keep v1).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='keep', version='v1')

    def list_notes(self, page_size: int = 100) -> List[Dict[str, Any]]:
        """List all notes."""
        if not self.is_ready():
            return []
        result = self.service.notes().list(pageSize=page_size).execute()
        return result.get('notes', [])

    def get_note(self, note_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific note by ID."""
        if not self.is_ready():
            return None
        return self.service.notes().get(name=f'notes/{note_id}').execute()

    def create_note(self, title: str, body_text: str) -> Optional[Dict[str, Any]]:
        """Create a new note."""
        if not self.is_ready():
            return None
        body = {
            'title': title,
            'body': {'text': {'text': body_text}}
        }
        return self.service.notes().create(body=body).execute()

    def delete_note(self, note_id: str) -> Dict[str, Any]:
        """Delete a note."""
        if not self.is_ready():
            return {}
        return self.service.notes().delete(name=f'notes/{note_id}').execute()
