"""Test GitHub Client Methods - Comprehensive"""
import unittest
import inspect


class TestGitHubClientSignatures(unittest.TestCase):
    """Comprehensive signature tests for all GitHubClient methods."""
    
    @classmethod
    def setUpClass(cls):
        from git.github.client import GitHubClient
        cls.GitHubClient = GitHubClient
    
    def test_get_authenticated_user_exists(self):
        """Verify get_authenticated_user method exists."""
        self.assertTrue(hasattr(self.GitHubClient, 'get_authenticated_user'))
    
    def test_list_repos_signature(self):
        """Verify list_repos has correct parameters."""
        sig = inspect.signature(self.GitHubClient.list_repos)
        params = list(sig.parameters.keys())
        self.assertIn('user', params)
        self.assertIn('type', params)
        self.assertIn('sort', params)
        self.assertIn('per_page', params)
    
    def test_get_repo_signature(self):
        """Verify get_repo has correct parameters."""
        sig = inspect.signature(self.GitHubClient.get_repo)
        params = list(sig.parameters.keys())
        self.assertIn('owner', params)
        self.assertIn('repo', params)
    
    def test_create_repo_signature(self):
        """Verify create_repo has correct parameters."""
        sig = inspect.signature(self.GitHubClient.create_repo)
        params = list(sig.parameters.keys())
        self.assertIn('name', params)
        self.assertIn('description', params)
        self.assertIn('private', params)
        self.assertIn('auto_init', params)
    
    def test_list_issues_signature(self):
        """Verify list_issues has correct parameters."""
        sig = inspect.signature(self.GitHubClient.list_issues)
        params = list(sig.parameters.keys())
        self.assertIn('owner', params)
        self.assertIn('repo', params)
        self.assertIn('state', params)
    
    def test_create_issue_signature(self):
        """Verify create_issue has correct parameters."""
        sig = inspect.signature(self.GitHubClient.create_issue)
        params = list(sig.parameters.keys())
        self.assertIn('owner', params)
        self.assertIn('repo', params)
        self.assertIn('title', params)
        self.assertIn('body', params)
        self.assertIn('labels', params)
    
    def test_close_issue_signature(self):
        """Verify close_issue has correct parameters."""
        sig = inspect.signature(self.GitHubClient.close_issue)
        params = list(sig.parameters.keys())
        self.assertIn('owner', params)
        self.assertIn('repo', params)
        self.assertIn('issue_number', params)
    
    def test_list_pull_requests_signature(self):
        """Verify list_pull_requests has correct parameters."""
        sig = inspect.signature(self.GitHubClient.list_pull_requests)
        params = list(sig.parameters.keys())
        self.assertIn('owner', params)
        self.assertIn('repo', params)
        self.assertIn('state', params)
    
    def test_create_pull_request_signature(self):
        """Verify create_pull_request has correct parameters."""
        sig = inspect.signature(self.GitHubClient.create_pull_request)
        params = list(sig.parameters.keys())
        self.assertIn('owner', params)
        self.assertIn('repo', params)
        self.assertIn('title', params)
        self.assertIn('head', params)
        self.assertIn('base', params)


class TestGitHubClientConstants(unittest.TestCase):
    """Test GitHubClient class constants."""
    
    def test_base_url(self):
        """Verify BASE_URL is correct."""
        from git.github.client import GitHubClient
        self.assertEqual(GitHubClient.BASE_URL, "https://api.github.com")
    
    def test_default_user(self):
        """Verify DEFAULT_USER is GithubBlanket."""
        from git.github.client import GitHubClient
        self.assertEqual(GitHubClient.DEFAULT_USER, "GithubBlanket")


class TestGitHubAuthModule(unittest.TestCase):
    """Test GitHub authentication module."""
    
    def test_get_github_token_path(self):
        """Verify token path is correct."""
        from git.github.auth import get_github_token_path
        path = get_github_token_path()
        self.assertTrue(str(path).endswith(".claude/github/token.json"))
    
    def test_save_github_token_exists(self):
        """Verify save_github_token function exists."""
        from git.github.auth import save_github_token
        self.assertTrue(callable(save_github_token))
    
    def test_get_github_token_exists(self):
        """Verify get_github_token function exists."""
        from git.github.auth import get_github_token
        self.assertTrue(callable(get_github_token))


class TestGitHubAPIError(unittest.TestCase):
    """Test GitHubAPIError exception class."""
    
    def test_error_creation(self):
        """Test creating GitHubAPIError."""
        from git.github.client import GitHubAPIError
        error = GitHubAPIError("Not found", status_code=404)
        self.assertEqual(error.status_code, 404)
        self.assertEqual(str(error), "Not found")
    
    def test_error_with_response(self):
        """Test GitHubAPIError with response data."""
        from git.github.client import GitHubAPIError
        response = {"message": "Not found", "documentation_url": "https://docs.github.com"}
        error = GitHubAPIError("Not found", status_code=404, response=response)
        self.assertEqual(error.response, response)


if __name__ == '__main__':
    unittest.main()
