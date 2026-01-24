"""Test Git Client Methods - Comprehensive"""
import unittest
import inspect


class TestGitClientMethods(unittest.TestCase):
    """Comprehensive tests for all GitClient methods."""
    
    @classmethod
    def setUpClass(cls):
        from git.core import GitClient
        cls.client = GitClient()
    
    def test_status_method(self):
        """Test status returns string output."""
        result = self.client.status()
        self.assertIsInstance(result, str)
    
    def test_status_short(self):
        """Test status with short format."""
        result = self.client.status(short=True)
        self.assertIsInstance(result, str)
    
    def test_log_method(self):
        """Test log returns commit history."""
        result = self.client.log(n=5)
        self.assertIsInstance(result, str)
    
    def test_log_oneline(self):
        """Test log with oneline format."""
        result = self.client.log(n=3, oneline=True)
        self.assertIsInstance(result, str)
    
    def test_diff_method(self):
        """Test diff returns changes."""
        result = self.client.diff()
        self.assertIsInstance(result, str)
    
    def test_branch_method(self):
        """Test branch lists branches."""
        result = self.client.branch()
        self.assertIsInstance(result, str)
        # Current branch should be marked
        self.assertIn("*", result)
    
    def test_remote_method(self):
        """Test remote lists remotes."""
        result = self.client.remote()
        self.assertIsInstance(result, str)
    
    def test_remote_verbose(self):
        """Test remote with verbose flag."""
        result = self.client.remote(verbose=True)
        self.assertIsInstance(result, str)
        # Should contain URLs when verbose
    
    def test_rev_parse_method(self):
        """Test rev_parse resolves HEAD."""
        result = self.client.rev_parse("HEAD")
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 40)  # SHA-1 hash length


class TestGitClientSignatures(unittest.TestCase):
    """Test all GitClient method signatures."""
    
    @classmethod
    def setUpClass(cls):
        from git.core.client import GitClient
        cls.GitClient = GitClient
    
    def test_checkout_signature(self):
        """Verify checkout has correct parameters."""
        sig = inspect.signature(self.GitClient.checkout)
        params = list(sig.parameters.keys())
        self.assertIn('ref', params)
        self.assertIn('create', params)
    
    def test_add_signature(self):
        """Verify add has correct parameters."""
        sig = inspect.signature(self.GitClient.add)
        params = list(sig.parameters.keys())
        self.assertIn('paths', params)
        self.assertIn('all', params)
    
    def test_commit_signature(self):
        """Verify commit has correct parameters."""
        sig = inspect.signature(self.GitClient.commit)
        params = list(sig.parameters.keys())
        self.assertIn('message', params)
        self.assertIn('all', params)
    
    def test_push_signature(self):
        """Verify push has correct parameters."""
        sig = inspect.signature(self.GitClient.push)
        params = list(sig.parameters.keys())
        self.assertIn('remote', params)
        self.assertIn('branch', params)
        self.assertIn('force', params)
    
    def test_pull_signature(self):
        """Verify pull has correct parameters."""
        sig = inspect.signature(self.GitClient.pull)
        params = list(sig.parameters.keys())
        self.assertIn('remote', params)
        self.assertIn('branch', params)
    
    def test_fetch_signature(self):
        """Verify fetch has correct parameters."""
        sig = inspect.signature(self.GitClient.fetch)
        params = list(sig.parameters.keys())
        self.assertIn('remote', params)
        self.assertIn('prune', params)


if __name__ == '__main__':
    unittest.main()
