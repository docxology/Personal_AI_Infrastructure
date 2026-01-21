import os
import json
from typing import Dict

def get_base_credentials_path() -> str:
    return os.path.expanduser("~/.claude/google-calendar/credentials.json")

def get_base_token_path() -> str:
    return os.path.expanduser("~/.claude/google-calendar/token.json")

def get_google_services_token_path() -> str:
    return os.path.expanduser("~/.claude/google-calendar/google_services_token.json")

def load_google_credentials_env() -> Dict[str, str]:
    """
    Parses credentials.json and returns a dictionary of environment variables
    expected by @dav23/google-mcp.
    """
    creds_path = get_base_credentials_path()
    token_path = get_google_services_token_path()
    
    if not os.path.exists(creds_path):
        raise FileNotFoundError(f"Credentials file not found at {creds_path}")
        
    with open(creds_path, 'r') as f:
        data = json.load(f)
        
    # Handle 'installed' or 'web' keys
    creds = data.get('installed') or data.get('web')
    if not creds:
        raise ValueError("Invalid credentials.json format: missing 'installed' or 'web' key")
        
    return {
        "GOOGLE_OAUTH_CLIENT_ID": creds.get('client_id', ''),
        "GOOGLE_OAUTH_CLIENT_SECRET": creds.get('client_secret', ''),
        "GOOGLE_OAUTH_TOKEN_PATH": token_path,
        "GOOGLE_OAUTH_REDIRECT_URI": list(creds.get('redirect_uris', ['http://localhost:3001']))[0]
    }

def get_google_credentials_object():
    """
    Returns a google.oauth2.credentials.Credentials object
    constructed from the flattened google_services_token.json.
    """
    from google.oauth2.credentials import Credentials
    
    token_path = get_google_services_token_path()
    if not os.path.exists(token_path):
        raise FileNotFoundError(f"Google services token not found at {token_path}")
        
    with open(token_path, 'r') as f:
        data = json.load(f)
        
    # Construct Credentials object
    # The JSON usually contains: token, refresh_token, token_uri, client_id, client_secret, scopes
    creds = Credentials(
        token=data.get("token"),
        refresh_token=data.get("refresh_token"),
        token_uri=data.get("token_uri", "https://oauth2.googleapis.com/token"),
        client_id=data.get("client_id"),
        client_secret=data.get("client_secret"),
        scopes=data.get("scopes")
    )
    return creds
