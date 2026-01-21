from typing import Any, Optional
from googleapiclient.discovery import build
from google.utils import get_google_credentials_object

class UniversalGoogleClient:
    """
    A generic client for any Google API service using the official google-api-python-client.
    
    Usage:
        client = UniversalGoogleClient(service_name='youtube', version='v3')
        response = client.service.search().list(part='snippet', q='test').execute()
    """
    
    def __init__(self, service_name: str, version: str):
        self.service_name = service_name
        self.version = version
        self.credentials = self._load_credentials()
        self.service = self._build_service()
        
    def _load_credentials(self):
        """Loads credentials from the centralized token store."""
        try:
            return get_google_credentials_object()
        except Exception as e:
            print(f"Warning: Failed to load credentials for {self.service_name}: {e}")
            return None

    def _build_service(self) -> Any:
        """Builds and returns the Google API service resource."""
        if not self.credentials:
            return None
        
        try:
            return build(self.service_name, self.version, credentials=self.credentials)
        except Exception as e:
            print(f"Error building service {self.service_name} ({self.version}): {e}")
            return None
            
    def is_ready(self) -> bool:
        """Checks if the service is successfully initialized."""
        return self.service is not None
