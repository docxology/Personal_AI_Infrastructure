from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GooglePublicDnsClient(UniversalGoogleClient):
    """
    Client for the dns API (v1).
    Enhanced with real functional methods.
    """
    def __init__(self):
        super().__init__(service_name='dns', version='v1')

    def list_managed_zones(self, project_id: str) -> List[Dict[str, Any]]:
        """List managed DNS zones."""
        if not self.is_ready():
            return []
        result = self.service.managedZones().list(project=project_id).execute()
        return result.get("managedZones", [])

    def list_records(self, project_id: str, zone_name: str) -> List[Dict[str, Any]]:
        """List DNS records in a zone."""
        if not self.is_ready():
            return []
        result = self.service.resourceRecordSets().list(project=project_id, managedZone=zone_name).execute()
        return result.get("rrsets", [])

