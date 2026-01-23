from typing import Any, Optional
import logging
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
            logging.warning(f"Warning: Failed to load credentials for {self.service_name}: {e}")
            return None

    def _build_service(self) -> Any:
        """Builds and returns the Google API service resource."""
        if not self.credentials:
            return None
        
        try:
            return build(self.service_name, self.version, credentials=self.credentials)
        except Exception as e:
            logging.error(f"Error building service {self.service_name} ({self.version}): {e}")
            return None
            
    def is_ready(self) -> bool:
        """Checks if the service is successfully initialized."""
        return self.service is not None

    def close(self):
        """Clean up resources. The google-api-python-client doesn't require explicit cleanup,
        but this method exists for consistency with MCP clients and future resource management."""
        self.service = None
        self.credentials = None

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit with cleanup."""
        self.close()
        return False
