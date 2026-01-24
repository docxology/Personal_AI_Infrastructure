"""
Git Module

Local git operations and GitHub API client for PAI.

Structure:
- git.core: Local git CLI wrapper
- git.github: GitHub REST API client
"""

from git.core import GitClient, is_git_repo, get_current_branch, get_repo_root
from git.github import GitHubClient, get_github_token

__all__ = [
    # Core
    "GitClient",
    "is_git_repo",
    "get_current_branch",
    "get_repo_root",
    # GitHub
    "GitHubClient",
    "get_github_token",
]

__version__ = "1.0.0"
