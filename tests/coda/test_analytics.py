"""Test Coda Analytics"""
import unittest
from tests.coda import skip_without_token

@skip_without_token
class TestCodaAnalyticsClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaAnalyticsClient
        cls.client = CodaAnalyticsClient()
    
    def test_get_analytics_last_updated(self):
        result = self.client.get_analytics_last_updated()
        self.assertIn("docAnalyticsLastUpdated", result)

if __name__ == '__main__':
    unittest.main()
