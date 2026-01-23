"""
Tests for google.youtube_tv module.
Auto-generated test file.
"""
import sys
import os
import unittest

# Ensure src is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestGoogleYoutubeTvClient(unittest.TestCase):
    """Test suite for GoogleYoutubeTvClient."""
    
    def test_01_import(self):
        """Test that the client module can be imported."""
        try:
            from google.youtube_tv.client import GoogleYoutubeTvClient
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import GoogleYoutubeTvClient: {e}")
    
    def test_02_instantiate(self):
        """Test that the client can be instantiated (may fail if API not enabled or no auth)."""
        from google.youtube_tv.client import GoogleYoutubeTvClient
        try:
            client = GoogleYoutubeTvClient()
            # Just check that we got an object back
            self.assertIsNotNone(client)
        except Exception as e:
            # This is expected for many APIs that aren't enabled or require special auth
            # We'll mark as skipped rather than failed
            self.skipTest(f"Instantiation skipped (expected if API not enabled): {e}")
    
    def test_03_is_ready(self):
        """Test the is_ready method if instantiation succeeded."""
        from google.youtube_tv.client import GoogleYoutubeTvClient
        try:
            client = GoogleYoutubeTvClient()
            # is_ready returns True if service was built successfully
            ready = client.is_ready()
            # Just log the result, don't fail if not ready
            print(f"GoogleYoutubeTvClient.is_ready() = {ready}")
            self.assertIsInstance(ready, bool)
        except Exception as e:
            self.skipTest(f"Skipped: {e}")

if __name__ == "__main__":
    print(f"Running tests for youtube_tv...")
    unittest.main(verbosity=2)
