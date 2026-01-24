"""
GitHub Authentication

Token management for GitHub API.

Default account: @GithubBlanket (fristonblanket@gmail.com)
"""

import os
import json
from pathlib import Path
from typing import Optional


def get_github_token_path() -> Path:
    """
    Get the path to the GitHub token file.
    
    Returns:
        Path to ~/.claude/github/token.json
    """
    return Path.home() / ".claude" / "github" / "token.json"


def get_github_token(token_path: Optional[str] = None) -> str:
    """
    Get GitHub API token.
    
    Tries in order:
    1. GITHUB_TOKEN environment variable
    2. token.json file at specified or default path
    
    Args:
        token_path: Custom path to token file
        
    Returns:
        GitHub API token
        
    Raises:
        ValueError: If no token found
    """
    # Check environment variable first
    env_token = os.environ.get("GITHUB_TOKEN")
    if env_token:
        return env_token
    
    # Check token file
    path = Path(token_path) if token_path else get_github_token_path()
    if path.exists():
        with open(path) as f:
            data = json.load(f)
            if "token" in data:
                return data["token"]
    
    raise ValueError(
        "GitHub token not found. Set GITHUB_TOKEN env or create "
        f"{get_github_token_path()}"
    )


def save_github_token(token: str, token_path: Optional[str] = None) -> None:
    """
    Save GitHub token to file.
    
    Args:
        token: GitHub API token
        token_path: Custom path (default: ~/.claude/github/token.json)
    """
    path = Path(token_path) if token_path else get_github_token_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, "w") as f:
        json.dump({"token": token}, f, indent=2)
