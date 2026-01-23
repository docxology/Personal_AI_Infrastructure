"""
Coda API Utilities

Token and configuration management for Coda.io API access.
"""

import os
import json
from typing import Optional


def get_coda_token_path() -> str:
    """Get the default path for Coda API token storage."""
    return os.path.expanduser("~/.claude/coda/token.json")


def get_coda_token(token_path: Optional[str] = None) -> str:
    """
    Retrieve the Coda API token.
    
    Priority:
    1. CODA_API_TOKEN environment variable
    2. Token file at token_path or default location
    
    Args:
        token_path: Optional path to token.json file
        
    Returns:
        The API token string
        
    Raises:
        ValueError: If no token is found
    """
    # Check environment variable first
    env_token = os.environ.get("CODA_API_TOKEN")
    if env_token:
        return env_token
    
    # Check token file
    path = token_path or get_coda_token_path()
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict) and "token" in data:
                return data["token"]
            elif isinstance(data, str):
                return data
    
    raise ValueError(
        f"No Coda API token found. Set CODA_API_TOKEN environment variable "
        f"or create {get_coda_token_path()} with format: {{\"token\": \"your_token\"}}"
    )


def save_coda_token(token: str, token_path: Optional[str] = None) -> str:
    """
    Save a Coda API token to the token file.
    
    Args:
        token: The API token to save
        token_path: Optional custom path
        
    Returns:
        Path where token was saved
    """
    path = token_path or get_coda_token_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, 'w') as f:
        json.dump({"token": token}, f, indent=2)
    
    # Set restrictive permissions
    os.chmod(path, 0o600)
    
    return path


def extract_doc_id_from_url(url: str) -> Optional[str]:
    """
    Extract doc ID from a Coda browser URL.
    
    The doc ID is the alphanumeric string after '_d' in the URL.
    Examples: 
      - https://coda.io/d/_dAbCDeFGH/... -> AbCDeFGH
      - https://coda.io/d/PAI_dNDxZHneeIw/... -> NDxZHneeIw
    
    Args:
        url: Coda document URL
        
    Returns:
        Doc ID or None if not found
    """
    import re
    # Match both /_d and name_d patterns
    match = re.search(r'_d([A-Za-z0-9]+)', url)
    if match:
        return match.group(1)
    return None
