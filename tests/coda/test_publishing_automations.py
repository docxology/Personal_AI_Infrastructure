"""Test Coda Publishing and Automations"""
import unittest
from tests.coda import skip_without_token

@skip_without_token
class TestCodaPublishingClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaPublishingClient
        cls.client = CodaPublishingClient()
    
    def test_get_categories(self):
        categories = self.client.get_categories()
        self.assertIsInstance(categories, list)

@skip_without_token
class TestCodaAutomationsClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaAutomationsClient
        cls.client = CodaAutomationsClient()
    
    def test_trigger_automation_exists(self):
        self.assertTrue(hasattr(self.client, 'trigger_automation'))

if __name__ == '__main__':
    unittest.main()
