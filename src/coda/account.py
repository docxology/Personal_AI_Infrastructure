"""
Coda Account Client

User account information.
"""

from typing import Dict, Any
from coda.base_client import CodaClient


class CodaAccountClient(CodaClient):
    """
    Client for Coda account operations.
    """
    
    # whoami() is inherited from CodaClient
    
    def get_user_name(self) -> str:
        """
        Get the current user's name.
        
        Returns:
            User name
        """
        return self.whoami().get("name", "")
    
    def get_user_email(self) -> str:
        """
        Get the current user's email (loginId).
        
        Returns:
            Email address
        """
        return self.whoami().get("loginId", "")
    
    def get_workspace(self) -> Dict[str, Any]:
        """
        Get the current workspace.
        
        Returns:
            Workspace info
        """
        return self.whoami().get("workspace", {})
    
    def get_token_name(self) -> str:
        """
        Get the name of the API token being used.
        
        Returns:
            Token name
        """
        return self.whoami().get("tokenName", "")
    
    def is_token_scoped(self) -> bool:
        """
        Check if the token has restricted API access.
        
        Returns:
            True if scoped/restricted
        """
        return self.whoami().get("scoped", False)
