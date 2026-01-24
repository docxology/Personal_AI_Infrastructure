"""
GitHub REST API Client

Client for GitHub API operations.

Default account: @GithubBlanket (fristonblanket@gmail.com)
"""

import json
import logging
from typing import Any, Dict, List, Optional
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from git.github.auth import get_github_token

logger = logging.getLogger(__name__)


class GitHubAPIError(Exception):
    """Exception raised for GitHub API errors."""
    
    def __init__(self, message: str, status_code: Optional[int] = None, response: Optional[Dict] = None):
        self.status_code = status_code
        self.response = response
        super().__init__(message)


class GitHubClient:
    """
    REST API client for GitHub.
    
    Default account: @GithubBlanket (fristonblanket@gmail.com)
    
    Usage:
        client = GitHubClient()
        repos = client.list_repos()
        client.create_issue("owner/repo", "Bug title", "Description")
    """
    
    BASE_URL = "https://api.github.com"
    DEFAULT_USER = "GithubBlanket"
    
    def __init__(self, token: Optional[str] = None, user: Optional[str] = None):
        """
        Initialize GitHub client.
        
        Args:
            token: GitHub API token (default: from env/file)
            user: GitHub username (default: GithubBlanket)
        """
        self.token = token or get_github_token()
        self.user = user or self.DEFAULT_USER
        logger.debug(f"GitHubClient initialized for @{self.user}")
    
    def _get_headers(self) -> Dict[str, str]:
        """Get request headers with authorization."""
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    
    def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Make GitHub API request.
        
        Args:
            method: HTTP method
            endpoint: API endpoint
            data: Request body
            
        Returns:
            Parsed JSON response
        """
        url = f"{self.BASE_URL}{endpoint}"
        body = json.dumps(data).encode("utf-8") if data else None
        
        try:
            request = Request(url, data=body, headers=self._get_headers(), method=method)
            logger.debug(f"GitHub API {method} {url}")
            
            with urlopen(request, timeout=30) as response:
                response_data = response.read().decode("utf-8")
                if response_data:
                    return json.loads(response_data)
                return {}
                
        except HTTPError as e:
            response_body = e.read().decode("utf-8") if e.fp else ""
            try:
                error_data = json.loads(response_body)
                message = error_data.get("message", str(e))
            except json.JSONDecodeError:
                message = response_body or str(e)
            
            raise GitHubAPIError(message, status_code=e.code)
            
        except URLError as e:
            raise GitHubAPIError(f"Connection error: {e.reason}")
    
    def _get(self, endpoint: str) -> Any:
        """Make GET request."""
        return self._request("GET", endpoint)
    
    def _post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Make POST request."""
        return self._request("POST", endpoint, data=data)
    
    def _patch(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Any:
        """Make PATCH request."""
        return self._request("PATCH", endpoint, data=data)
    
    def _delete(self, endpoint: str) -> Any:
        """Make DELETE request."""
        return self._request("DELETE", endpoint)
    
    # -------------------------------------------------------------------------
    # User Operations
    # -------------------------------------------------------------------------
    
    def get_authenticated_user(self) -> Dict[str, Any]:
        """
        Get authenticated user info.
        
        Returns:
            User data
        """
        return self._get("/user")
    
    # -------------------------------------------------------------------------
    # Repository Operations
    # -------------------------------------------------------------------------
    
    def list_repos(
        self,
        user: Optional[str] = None,
        type: str = "all",
        sort: str = "updated",
        per_page: int = 30
    ) -> List[Dict[str, Any]]:
        """
        List repositories for a user.
        
        Args:
            user: GitHub username (default: authenticated user)
            type: all, owner, member
            sort: created, updated, pushed, full_name
            per_page: Results per page
            
        Returns:
            List of repositories
        """
        if user:
            return self._get(f"/users/{user}/repos?type={type}&sort={sort}&per_page={per_page}")
        return self._get(f"/user/repos?type={type}&sort={sort}&per_page={per_page}")
    
    def get_repo(self, owner: str, repo: str) -> Dict[str, Any]:
        """
        Get repository details.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Repository data
        """
        return self._get(f"/repos/{owner}/{repo}")
    
    def create_repo(
        self,
        name: str,
        description: Optional[str] = None,
        private: bool = False,
        auto_init: bool = True
    ) -> Dict[str, Any]:
        """
        Create a new repository.
        
        Args:
            name: Repository name
            description: Repository description
            private: Create as private repo
            auto_init: Initialize with README
            
        Returns:
            Created repository data
        """
        data = {
            "name": name,
            "private": private,
            "auto_init": auto_init,
        }
        if description:
            data["description"] = description
        
        return self._post("/user/repos", data=data)
    
    # -------------------------------------------------------------------------
    # Issue Operations
    # -------------------------------------------------------------------------
    
    def list_issues(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        per_page: int = 30
    ) -> List[Dict[str, Any]]:
        """
        List issues for a repository.
        
        Args:
            owner: Repository owner
            repo: Repository name
            state: open, closed, all
            per_page: Results per page
            
        Returns:
            List of issues
        """
        return self._get(f"/repos/{owner}/{repo}/issues?state={state}&per_page={per_page}")
    
    def create_issue(
        self,
        owner: str,
        repo: str,
        title: str,
        body: Optional[str] = None,
        labels: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Create an issue.
        
        Args:
            owner: Repository owner
            repo: Repository name
            title: Issue title
            body: Issue body
            labels: Issue labels
            
        Returns:
            Created issue data
        """
        data = {"title": title}
        if body:
            data["body"] = body
        if labels:
            data["labels"] = labels
        
        return self._post(f"/repos/{owner}/{repo}/issues", data=data)
    
    def close_issue(self, owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
        """
        Close an issue.
        
        Args:
            owner: Repository owner
            repo: Repository name
            issue_number: Issue number
            
        Returns:
            Updated issue data
        """
        return self._patch(f"/repos/{owner}/{repo}/issues/{issue_number}", data={"state": "closed"})
    
    # -------------------------------------------------------------------------
    # Pull Request Operations
    # -------------------------------------------------------------------------
    
    def list_pull_requests(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        per_page: int = 30
    ) -> List[Dict[str, Any]]:
        """
        List pull requests.
        
        Args:
            owner: Repository owner
            repo: Repository name
            state: open, closed, all
            per_page: Results per page
            
        Returns:
            List of pull requests
        """
        return self._get(f"/repos/{owner}/{repo}/pulls?state={state}&per_page={per_page}")
    
    def create_pull_request(
        self,
        owner: str,
        repo: str,
        title: str,
        head: str,
        base: str,
        body: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a pull request.
        
        Args:
            owner: Repository owner
            repo: Repository name
            title: PR title
            head: Branch with changes
            base: Target branch
            body: PR description
            
        Returns:
            Created PR data
        """
        data = {
            "title": title,
            "head": head,
            "base": base,
        }
        if body:
            data["body"] = body
        
        return self._post(f"/repos/{owner}/{repo}/pulls", data=data)
