"""Test GitHub Module"""
import unittest
import inspect


class TestGitHubClient(unittest.TestCase):
    """Tests for GitHubClient class."""
    
    def test_client_importable(self):
        """Verify GitHubClient is importable."""
        from git.github import GitHubClient
        self.assertTrue(callable(GitHubClient))
    
    def test_client_has_methods(self):
        """Verify GitHubClient has expected methods."""
        from git.github.client import GitHubClient
        methods = [
            'get_authenticated_user',
            'list_repos',
            'get_repo',
            'create_repo',
            'list_issues',
            'create_issue',
            'close_issue',
            'list_pull_requests',
            'create_pull_request',
        ]
        for method in methods:
            self.assertTrue(hasattr(GitHubClient, method), f"Missing method: {method}")
    
    def test_default_user(self):
        """Verify default user is GithubBlanket."""
        from git.github.client import GitHubClient
        self.assertEqual(GitHubClient.DEFAULT_USER, "GithubBlanket")
    
    def test_list_repos_signature(self):
        """Verify list_repos has correct parameters."""
        from git.github.client import GitHubClient
        sig = inspect.signature(GitHubClient.list_repos)
        params = list(sig.parameters.keys())
        self.assertIn('user', params)
        self.assertIn('type', params)
    
    def test_create_issue_signature(self):
        """Verify create_issue has correct parameters."""
        from git.github.client import GitHubClient
        sig = inspect.signature(GitHubClient.create_issue)
        params = list(sig.parameters.keys())
        self.assertIn('owner', params)
        self.assertIn('repo', params)
        self.assertIn('title', params)


class TestGitHubAuth(unittest.TestCase):
    """Tests for GitHub authentication."""
    
    def test_get_token_path(self):
        """Verify get_github_token_path returns expected path."""
        from git.github.auth import get_github_token_path
        path = get_github_token_path()
        self.assertTrue(str(path).endswith(".claude/github/token.json"))
    
    def test_save_token_callable(self):
        """Verify save_github_token is callable."""
        from git.github.auth import save_github_token
        self.assertTrue(callable(save_github_token))


class TestGitHubAPIError(unittest.TestCase):
    """Tests for GitHubAPIError exception."""
    
    def test_error_exists(self):
        """Verify GitHubAPIError is importable."""
        from git.github.client import GitHubAPIError
        error = GitHubAPIError("test", status_code=404)
        self.assertEqual(error.status_code, 404)


if __name__ == '__main__':
    unittest.main()
