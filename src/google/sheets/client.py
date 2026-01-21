from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleSheetsClient(UniversalGoogleClient):
    """
    Client for the Google Sheets API (sheets v4).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='sheets', version='v4')

    def get_values(self, spreadsheet_id: str, range: str) -> List[List[Any]]:
        """Get values from a spreadsheet range."""
        if not self.is_ready():
            return []
        result = self.service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range
        ).execute()
        return result.get('values', [])

    def update_values(self, spreadsheet_id: str, range: str, values: List[List[Any]]) -> Dict[str, Any]:
        """Update values in a spreadsheet range."""
        if not self.is_ready():
            return {}
        body = {'values': values}
        result = self.service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range,
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()
        return result

    def append_values(self, spreadsheet_id: str, range: str, values: List[List[Any]]) -> Dict[str, Any]:
        """Append values to a spreadsheet range."""
        if not self.is_ready():
            return {}
        body = {'values': values}
        result = self.service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range,
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()
        return result

    def create_spreadsheet(self, title: str) -> Optional[Dict[str, Any]]:
        """Create a new spreadsheet."""
        if not self.is_ready():
            return None
        spreadsheet = {'properties': {'title': title}}
        result = self.service.spreadsheets().create(body=spreadsheet).execute()
        return result

    def get_spreadsheet(self, spreadsheet_id: str) -> Optional[Dict[str, Any]]:
        """Get spreadsheet metadata."""
        if not self.is_ready():
            return None
        return self.service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
