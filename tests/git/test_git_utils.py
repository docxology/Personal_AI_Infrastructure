"""Test Git Utilities - Comprehensive"""
import unittest
from pathlib import Path


class TestGitUtilityFunctions(unittest.TestCase):
    """Comprehensive tests for git utility functions."""
    
    def test_is_git_repo_current(self):
        """Test is_git_repo on current directory."""
        from git.core.utils import is_git_repo
        self.assertTrue(is_git_repo())
    
    def test_is_git_repo_with_path(self):
        """Test is_git_repo with explicit path."""
        from git.core.utils import is_git_repo
        result = is_git_repo(str(Path.cwd()))
        self.assertTrue(result)
    
    def test_is_git_repo_invalid(self):
        """Test is_git_repo returns False for non-repo."""
        from git.core.utils import is_git_repo
        result = is_git_repo("/tmp")
        self.assertFalse(result)
    
    def test_get_current_branch(self):
        """Test get_current_branch returns branch name."""
        from git.core.utils import get_current_branch
        branch = get_current_branch()
        self.assertIsInstance(branch, (str, type(None)))
    
    def test_get_repo_root(self):
        """Test get_repo_root returns valid path."""
        from git.core.utils import get_repo_root
        root = get_repo_root()
        self.assertIsNotNone(root)
        self.assertTrue(Path(root).exists())
        self.assertTrue(Path(root).is_dir())
    
    def test_get_remote_url(self):
        """Test get_remote_url returns origin URL."""
        from git.core.utils import get_remote_url
        url = get_remote_url()
        self.assertIsInstance(url, (str, type(None)))


class TestGitUtilsImports(unittest.TestCase):
    """Test git utils are properly exported."""
    
    def test_import_from_core(self):
        """Test imports from git.core work."""
        from git.core import is_git_repo, get_current_branch, get_repo_root
        self.assertTrue(callable(is_git_repo))
        self.assertTrue(callable(get_current_branch))
        self.assertTrue(callable(get_repo_root))
    
    def test_import_from_main(self):
        """Test imports from git module work."""
        from git import is_git_repo, get_current_branch, get_repo_root
        self.assertTrue(callable(is_git_repo))


if __name__ == '__main__':
    unittest.main()
