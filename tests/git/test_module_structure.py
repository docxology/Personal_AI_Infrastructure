"""Test Git Module Imports and Structure"""
import unittest


class TestGitModuleImports(unittest.TestCase):
    """Test all imports from git module work correctly."""
    
    def test_import_git_client(self):
        """Test importing GitClient from main module."""
        from git import GitClient
        self.assertTrue(callable(GitClient))
    
    def test_import_github_client(self):
        """Test importing GitHubClient from main module."""
        from git import GitHubClient
        self.assertTrue(callable(GitHubClient))
    
    def test_import_utilities(self):
        """Test importing utility functions from main module."""
        from git import is_git_repo, get_current_branch, get_repo_root
        self.assertTrue(callable(is_git_repo))
        self.assertTrue(callable(get_current_branch))
        self.assertTrue(callable(get_repo_root))
    
    def test_import_github_token(self):
        """Test importing GitHub token function."""
        from git import get_github_token
        self.assertTrue(callable(get_github_token))


class TestGitCoreImports(unittest.TestCase):
    """Test imports from git.core submodule."""
    
    def test_import_from_core(self):
        """Test importing from git.core."""
        from git.core import GitClient, is_git_repo
        self.assertTrue(callable(GitClient))
        self.assertTrue(callable(is_git_repo))
    
    def test_import_git_error(self):
        """Test importing GitError exception."""
        from git.core.client import GitError
        self.assertTrue(issubclass(GitError, Exception))


class TestGitHubImports(unittest.TestCase):
    """Test imports from git.github submodule."""
    
    def test_import_from_github(self):
        """Test importing from git.github."""
        from git.github import GitHubClient, get_github_token
        self.assertTrue(callable(GitHubClient))
        self.assertTrue(callable(get_github_token))
    
    def test_import_github_error(self):
        """Test importing GitHubAPIError exception."""
        from git.github.client import GitHubAPIError
        self.assertTrue(issubclass(GitHubAPIError, Exception))


class TestModuleVersion(unittest.TestCase):
    """Test module version is set."""
    
    def test_version_exists(self):
        """Verify __version__ is defined."""
        import git
        self.assertTrue(hasattr(git, '__version__'))
        self.assertIsInstance(git.__version__, str)


if __name__ == '__main__':
    unittest.main()
