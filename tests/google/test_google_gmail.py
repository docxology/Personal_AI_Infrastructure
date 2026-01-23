import unittest
import os
import sys
import time

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from google.gmail.client import GoogleGmailClient

class TestGoogleGmailIntegration(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Starting Google Gmail Integration Tests...")
        cls.client = GoogleGmailClient()
        
    @classmethod
    def tearDownClass(cls):
        cls.client.close()
        print("\nTests Complete.")

    def test_01_list_emails(self):
        """Verify we can list emails."""
        print("\nTesting list_emails...")
        threads = self.client.list_emails(max_results=5)
        if isinstance(threads, str):
            self.assertGreater(len(threads), 0)
        else:
            self.assertIsInstance(threads, list)
        print(f"Found {len(threads)} threads.")
        
    def test_02_create_draft(self):
        """Verify we can create a draft."""
        print("\nTesting create_draft...")
        to = "test@example.com"
        subject = f"PAI Integration Test Draft {int(time.time())}"
        body = "This is a test draft created by the PAI automated test suite."
        
        draft = self.client.create_draft(to=to, subject=subject, body=body)
        print(f"Result type: {type(draft)}")
        print(f"Result content: {draft}")
        
        # The tool might return a string message or a dict
        if isinstance(draft, str):
            self.assertIn("Draft created", draft)
        else:
            self.assertIsInstance(draft, dict)
            self.assertIn("id", draft)
            print(f"Created draft: {draft.get('id')}")

if __name__ == '__main__':
    unittest.main()
