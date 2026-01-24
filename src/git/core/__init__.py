"""
Git Core Module

Local git CLI wrapper and utilities.
"""

from git.core.client import GitClient
from git.core.utils import is_git_repo, get_current_branch, get_repo_root

__all__ = [
    "GitClient",
    "is_git_repo",
    "get_current_branch",
    "get_repo_root",
]
