"""Test Coda Account Operations"""
import unittest
from tests.coda import skip_without_token

@skip_without_token
class TestCodaAccountOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaAccountClient
        cls.client = CodaAccountClient()
    
    def test_whoami(self):
        result = self.client.whoami()
        self.assertIn("name", result)
        self.assertIn("loginId", result)
    
    def test_get_user_name(self):
        name = self.client.get_user_name()
        self.assertTrue(len(name) > 0)
    
    def test_get_user_email(self):
        email = self.client.get_user_email()
        self.assertIn("@", email)
    
    def test_get_workspace(self):
        workspace = self.client.get_workspace()
        self.assertIsInstance(workspace, dict)

if __name__ == '__main__':
    unittest.main()
