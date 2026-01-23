from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleSheetsClient(UniversalGoogleClient):
    """
    Client for the Google Sheets API (sheets v4).
    Enhanced with comprehensive convenience methods for:
    - Basic read/write operations
    - Batch operations
    - Sheet management
    - Cell formatting
    - Named ranges
    """
    def __init__(self):
        super().__init__(service_name='sheets', version='v4')

    # =====================
    # Basic Operations
    # =====================
    
    def get_values(self, spreadsheet_id: str, range: str) -> List[List[Any]]:
        """Get values from a spreadsheet range."""
        if not self.is_ready():
            return []
        result = self.service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range
        ).execute()
        return result.get('values', [])

    def update_values(self, spreadsheet_id: str, range: str, values: List[List[Any]], 
                      value_input_option: str = 'USER_ENTERED') -> Dict[str, Any]:
        """Update values in a spreadsheet range."""
        if not self.is_ready():
            return {}
        body = {'values': values}
        result = self.service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range,
            valueInputOption=value_input_option,
            body=body
        ).execute()
        return result

    def append_values(self, spreadsheet_id: str, range: str, values: List[List[Any]],
                      value_input_option: str = 'USER_ENTERED') -> Dict[str, Any]:
        """Append values to a spreadsheet range."""
        if not self.is_ready():
            return {}
        body = {'values': values}
        result = self.service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range,
            valueInputOption=value_input_option,
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
        """Get spreadsheet metadata including sheets, properties, and named ranges."""
        if not self.is_ready():
            return None
        return self.service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

    # =====================
    # Batch Operations
    # =====================

    def batch_get_values(self, spreadsheet_id: str, ranges: List[str]) -> Dict[str, Any]:
        """Get values from multiple ranges in a single request."""
        if not self.is_ready():
            return {}
        result = self.service.spreadsheets().values().batchGet(
            spreadsheetId=spreadsheet_id,
            ranges=ranges
        ).execute()
        return result

    def batch_update_values(self, spreadsheet_id: str, data: List[Dict[str, Any]],
                            value_input_option: str = 'USER_ENTERED') -> Dict[str, Any]:
        """
        Update multiple ranges in a single request.
        
        Args:
            spreadsheet_id: The spreadsheet ID
            data: List of dicts with 'range' and 'values' keys
                  e.g., [{'range': 'Sheet1!A1', 'values': [[1,2,3]]}]
            value_input_option: How input data should be interpreted
        """
        if not self.is_ready():
            return {}
        body = {
            'valueInputOption': value_input_option,
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()
        return result

    def batch_clear(self, spreadsheet_id: str, ranges: List[str]) -> Dict[str, Any]:
        """Clear values from multiple ranges in a single request."""
        if not self.is_ready():
            return {}
        body = {'ranges': ranges}
        result = self.service.spreadsheets().values().batchClear(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()
        return result

    def clear_values(self, spreadsheet_id: str, range: str) -> Dict[str, Any]:
        """Clear values from a single range."""
        if not self.is_ready():
            return {}
        result = self.service.spreadsheets().values().clear(
            spreadsheetId=spreadsheet_id,
            range=range,
            body={}
        ).execute()
        return result

    # =====================
    # Sheet Management
    # =====================

    def get_sheet_id(self, spreadsheet_id: str, sheet_title: str) -> Optional[int]:
        """Get the sheet ID for a sheet by its title."""
        spreadsheet = self.get_spreadsheet(spreadsheet_id)
        if not spreadsheet:
            return None
        for sheet in spreadsheet.get('sheets', []):
            if sheet.get('properties', {}).get('title') == sheet_title:
                return sheet['properties']['sheetId']
        return None

    def add_sheet(self, spreadsheet_id: str, title: str, 
                  rows: int = 1000, cols: int = 26) -> Dict[str, Any]:
        """Add a new sheet to a spreadsheet."""
        if not self.is_ready():
            return {}
        request = {
            'requests': [{
                'addSheet': {
                    'properties': {
                        'title': title,
                        'gridProperties': {
                            'rowCount': rows,
                            'columnCount': cols
                        }
                    }
                }
            }]
        }
        result = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=request
        ).execute()
        return result

    def delete_sheet(self, spreadsheet_id: str, sheet_id: int) -> Dict[str, Any]:
        """Delete a sheet from a spreadsheet by sheet ID."""
        if not self.is_ready():
            return {}
        request = {
            'requests': [{
                'deleteSheet': {
                    'sheetId': sheet_id
                }
            }]
        }
        result = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=request
        ).execute()
        return result

    def copy_sheet(self, source_spreadsheet_id: str, sheet_id: int, 
                   destination_spreadsheet_id: str) -> Dict[str, Any]:
        """Copy a sheet to another spreadsheet."""
        if not self.is_ready():
            return {}
        result = self.service.spreadsheets().sheets().copyTo(
            spreadsheetId=source_spreadsheet_id,
            sheetId=sheet_id,
            body={'destinationSpreadsheetId': destination_spreadsheet_id}
        ).execute()
        return result

    def rename_sheet(self, spreadsheet_id: str, sheet_id: int, new_title: str) -> Dict[str, Any]:
        """Rename a sheet."""
        if not self.is_ready():
            return {}
        request = {
            'requests': [{
                'updateSheetProperties': {
                    'properties': {
                        'sheetId': sheet_id,
                        'title': new_title
                    },
                    'fields': 'title'
                }
            }]
        }
        result = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=request
        ).execute()
        return result

    # =====================
    # Cell Formatting
    # =====================

    def format_cells(self, spreadsheet_id: str, sheet_id: int, 
                     start_row: int, end_row: int, start_col: int, end_col: int,
                     format_options: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply formatting to a range of cells.
        
        Args:
            format_options: Dict with formatting properties like:
                - 'backgroundColor': {'red': 1.0, 'green': 0.0, 'blue': 0.0}
                - 'textFormat': {'bold': True, 'italic': False, 'fontSize': 12}
                - 'horizontalAlignment': 'CENTER'
        """
        if not self.is_ready():
            return {}
        request = {
            'requests': [{
                'repeatCell': {
                    'range': {
                        'sheetId': sheet_id,
                        'startRowIndex': start_row,
                        'endRowIndex': end_row,
                        'startColumnIndex': start_col,
                        'endColumnIndex': end_col
                    },
                    'cell': {
                        'userEnteredFormat': format_options
                    },
                    'fields': 'userEnteredFormat(' + ','.join(format_options.keys()) + ')'
                }
            }]
        }
        result = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=request
        ).execute()
        return result

    def set_column_width(self, spreadsheet_id: str, sheet_id: int,
                         start_col: int, end_col: int, width: int) -> Dict[str, Any]:
        """Set the width of columns in pixels."""
        if not self.is_ready():
            return {}
        request = {
            'requests': [{
                'updateDimensionProperties': {
                    'range': {
                        'sheetId': sheet_id,
                        'dimension': 'COLUMNS',
                        'startIndex': start_col,
                        'endIndex': end_col
                    },
                    'properties': {
                        'pixelSize': width
                    },
                    'fields': 'pixelSize'
                }
            }]
        }
        result = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=request
        ).execute()
        return result

    def merge_cells(self, spreadsheet_id: str, sheet_id: int,
                    start_row: int, end_row: int, 
                    start_col: int, end_col: int,
                    merge_type: str = 'MERGE_ALL') -> Dict[str, Any]:
        """
        Merge a range of cells.
        
        Args:
            merge_type: 'MERGE_ALL', 'MERGE_COLUMNS', or 'MERGE_ROWS'
        """
        if not self.is_ready():
            return {}
        request = {
            'requests': [{
                'mergeCells': {
                    'range': {
                        'sheetId': sheet_id,
                        'startRowIndex': start_row,
                        'endRowIndex': end_row,
                        'startColumnIndex': start_col,
                        'endColumnIndex': end_col
                    },
                    'mergeType': merge_type
                }
            }]
        }
        result = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=request
        ).execute()
        return result

    # =====================
    # Find and Replace
    # =====================

    def find_and_replace(self, spreadsheet_id: str, find: str, replacement: str,
                         sheet_id: Optional[int] = None,
                         match_case: bool = False,
                         match_entire_cell: bool = False) -> Dict[str, Any]:
        """Find and replace text across a spreadsheet or specific sheet."""
        if not self.is_ready():
            return {}
        find_replace = {
            'find': find,
            'replacement': replacement,
            'matchCase': match_case,
            'matchEntireCell': match_entire_cell,
            'allSheets': sheet_id is None
        }
        if sheet_id is not None:
            find_replace['sheetId'] = sheet_id
            find_replace['allSheets'] = False
        
        request = {
            'requests': [{
                'findReplace': find_replace
            }]
        }
        result = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=request
        ).execute()
        return result

    # =====================
    # Named Ranges
    # =====================

    def get_named_ranges(self, spreadsheet_id: str) -> List[Dict[str, Any]]:
        """Get all named ranges in a spreadsheet."""
        spreadsheet = self.get_spreadsheet(spreadsheet_id)
        if not spreadsheet:
            return []
        return spreadsheet.get('namedRanges', [])

    def add_named_range(self, spreadsheet_id: str, name: str, sheet_id: int,
                        start_row: int, end_row: int,
                        start_col: int, end_col: int) -> Dict[str, Any]:
        """Create a named range."""
        if not self.is_ready():
            return {}
        request = {
            'requests': [{
                'addNamedRange': {
                    'namedRange': {
                        'name': name,
                        'range': {
                            'sheetId': sheet_id,
                            'startRowIndex': start_row,
                            'endRowIndex': end_row,
                            'startColumnIndex': start_col,
                            'endColumnIndex': end_col
                        }
                    }
                }
            }]
        }
        result = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=request
        ).execute()
        return result

    def delete_named_range(self, spreadsheet_id: str, named_range_id: str) -> Dict[str, Any]:
        """Delete a named range by its ID."""
        if not self.is_ready():
            return {}
        request = {
            'requests': [{
                'deleteNamedRange': {
                    'namedRangeId': named_range_id
                }
            }]
        }
        result = self.service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=request
        ).execute()
        return result
