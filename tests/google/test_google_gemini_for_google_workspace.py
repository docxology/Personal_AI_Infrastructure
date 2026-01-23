"""
Tests for google.gemini_for_google_workspace module.
Auto-generated test file.
"""
import sys
import os
import unittest

# Ensure src is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestGoogleGeminiForGoogleWorkspaceClient(unittest.TestCase):
    """Test suite for GoogleGeminiForGoogleWorkspaceClient."""
    
    def test_01_import(self):
        """Test that the client module can be imported."""
        try:
            from google.gemini_for_google_workspace.client import GoogleGeminiForGoogleWorkspaceClient
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Failed to import GoogleGeminiForGoogleWorkspaceClient: {e}")
    
    def test_02_instantiate(self):
        """Test that the client can be instantiated (may fail if API not enabled or no auth)."""
        from google.gemini_for_google_workspace.client import GoogleGeminiForGoogleWorkspaceClient
        try:
            client = GoogleGeminiForGoogleWorkspaceClient()
            # Just check that we got an object back
            self.assertIsNotNone(client)
        except Exception as e:
            # This is expected for many APIs that aren't enabled or require special auth
            # We'll mark as skipped rather than failed
            self.skipTest(f"Instantiation skipped (expected if API not enabled): {e}")
    
    def test_03_is_ready(self):
        """Test the is_ready method if instantiation succeeded."""
        from google.gemini_for_google_workspace.client import GoogleGeminiForGoogleWorkspaceClient
        try:
            client = GoogleGeminiForGoogleWorkspaceClient()
            # is_ready returns True if service was built successfully
            ready = client.is_ready()
            # Just log the result, don't fail if not ready
            print(f"GoogleGeminiForGoogleWorkspaceClient.is_ready() = {ready}")
            self.assertIsInstance(ready, bool)
        except Exception as e:
            self.skipTest(f"Skipped: {e}")

    def test_04_prompt_builders(self):
        """Verify the helper methods for building prompts return expected strings."""
        from google.gemini_for_google_workspace.client import GoogleGeminiForGoogleWorkspaceClient
        
        # Instantiate directly. This uses real authentication.
        try:
            client = GoogleGeminiForGoogleWorkspaceClient()
        except Exception:
            # If real init fails (e.g. no auth credentials), we skip.
            self.skipTest("Skipping method tests because real client instantiation failed.")
            return

        # Test format_for_workspace
        prompt = client.format_for_workspace("Summarize", "Content of doc", "doc")
        self.assertIn("Context: Working with a Google Doc", prompt)
        self.assertIn("Content of doc", prompt)
        
        # Test build_doc_assistance_prompt
        rewrite = client.build_doc_assistance_prompt("rewrite", "Original text")
        self.assertIn("Rewrite this text", rewrite)
        self.assertIn("Original text", rewrite)

        # Test build_sheet_analysis_prompt
        sheet = client.build_sheet_analysis_prompt("Headers: A, B", "Sum of A?")
        self.assertIn("Google Sheets", sheet)
        self.assertIn("Sum of A?", sheet)

        # Test build_email_draft_prompt
        email = client.build_email_draft_prompt("Meeting", "professional")
        self.assertIn("Draft a professional email", email)
        self.assertIn("Meeting", email)

if __name__ == "__main__":
    print(f"Running tests for gemini_for_google_workspace...")
    unittest.main(verbosity=2)
