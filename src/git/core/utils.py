"""
Git Utilities

Helper functions for git operations.
"""

import subprocess
from pathlib import Path
from typing import Optional


def is_git_repo(path: Optional[str] = None) -> bool:
    """
    Check if path is inside a git repository.
    
    Args:
        path: Path to check (default: current directory)
        
    Returns:
        True if inside git repo
    """
    cwd = Path(path) if path else Path.cwd()
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=cwd,
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def get_current_branch(path: Optional[str] = None) -> Optional[str]:
    """
    Get the current branch name.
    
    Args:
        path: Repository path (default: current directory)
        
    Returns:
        Branch name or None if not on branch
    """
    cwd = Path(path) if path else Path.cwd()
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        branch = result.stdout.strip()
        return branch if branch != "HEAD" else None
    except subprocess.CalledProcessError:
        return None


def get_repo_root(path: Optional[str] = None) -> Optional[str]:
    """
    Get the repository root directory.
    
    Args:
        path: Path inside repository (default: current directory)
        
    Returns:
        Absolute path to repo root or None
    """
    cwd = Path(path) if path else Path.cwd()
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def get_remote_url(remote: str = "origin", path: Optional[str] = None) -> Optional[str]:
    """
    Get the URL for a remote.
    
    Args:
        remote: Remote name
        path: Repository path
        
    Returns:
        Remote URL or None
    """
    cwd = Path(path) if path else Path.cwd()
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", remote],
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None
