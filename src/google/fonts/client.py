from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleFontsClient(UniversalGoogleClient):
    """
    Client for the Web Fonts Developer API (webfonts v1).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='webfonts', version='v1')

    def list_fonts(self, sort: str = 'alpha') -> List[Dict[str, Any]]:
        """List available Google Fonts. Sort options: alpha, date, popularity, style, trending."""
        if not self.is_ready():
            return []
        result = self.service.webfonts().list(sort=sort).execute()
        return result.get('items', [])

    def get_font(self, family: str) -> Optional[Dict[str, Any]]:
        """Get details for a specific font family."""
        fonts = self.list_fonts()
        for font in fonts:
            if font.get('family', '').lower() == family.lower():
                return font
        return None
