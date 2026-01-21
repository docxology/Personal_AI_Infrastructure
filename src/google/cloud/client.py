from google.universal_client import UniversalGoogleClient
from typing import List, Dict, Any, Optional

class GoogleCloudClient(UniversalGoogleClient):
    """
    Client for the Cloud Resource Manager API (cloudresourcemanager v1).
    Enhanced with convenience methods.
    """
    def __init__(self):
        super().__init__(service_name='cloudresourcemanager', version='v1')

    def list_projects(self, filter: str = None) -> List[Dict[str, Any]]:
        """List all projects accessible by the user."""
        if not self.is_ready():
            return []
        kwargs = {}
        if filter:
            kwargs['filter'] = filter
        result = self.service.projects().list(**kwargs).execute()
        return result.get('projects', [])

    def get_project(self, project_id: str) -> Optional[Dict[str, Any]]:
        """Get project details by ID."""
        if not self.is_ready():
            return None
        return self.service.projects().get(projectId=project_id).execute()
