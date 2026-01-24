"""Test Git Core Module"""
import unittest
from pathlib import Path


class TestGitClient(unittest.TestCase):
    """Tests for GitClient class."""
    
    def test_client_importable(self):
        """Verify GitClient is importable."""
        from git.core import GitClient
        self.assertTrue(callable(GitClient))
    
    def test_client_has_methods(self):
        """Verify GitClient has expected methods."""
        from git.core import GitClient
        client = GitClient()
        self.assertTrue(hasattr(client, 'status'))
        self.assertTrue(hasattr(client, 'log'))
        self.assertTrue(hasattr(client, 'diff'))
        self.assertTrue(hasattr(client, 'commit'))
        self.assertTrue(hasattr(client, 'push'))
        self.assertTrue(hasattr(client, 'pull'))
    
    def test_status(self):
        """Test status method works in current repo."""
        from git.core import GitClient
        client = GitClient()
        status = client.status()
        self.assertIsInstance(status, str)
    
    def test_log(self):
        """Test log method works."""
        from git.core import GitClient
        client = GitClient()
        log = client.log(n=5, oneline=True)
        self.assertIsInstance(log, str)
    
    def test_branch(self):
        """Test branch method."""
        from git.core import GitClient
        client = GitClient()
        branches = client.branch()
        self.assertIsInstance(branches, str)


class TestGitUtils(unittest.TestCase):
    """Tests for git utility functions."""
    
    def test_is_git_repo(self):
        """Test is_git_repo function."""
        from git.core import is_git_repo
        # Current directory should be a git repo
        self.assertTrue(is_git_repo())
    
    def test_get_current_branch(self):
        """Test get_current_branch function."""
        from git.core import get_current_branch
        branch = get_current_branch()
        self.assertIsInstance(branch, (str, type(None)))
    
    def test_get_repo_root(self):
        """Test get_repo_root function."""
        from git.core import get_repo_root
        root = get_repo_root()
        self.assertIsInstance(root, str)
        self.assertTrue(Path(root).exists())


class TestGitError(unittest.TestCase):
    """Tests for GitError exception."""
    
    def test_git_error_exists(self):
        """Verify GitError is importable."""
        from git.core.client import GitError
        error = GitError("test", returncode=1, stderr="error")
        self.assertEqual(error.returncode, 1)


if __name__ == '__main__':
    unittest.main()
