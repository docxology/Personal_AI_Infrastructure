"""Test Coda Permissions"""
import unittest
from tests.coda import skip_without_token, PAI_DOC_ID

@skip_without_token
class TestCodaPermissionsClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaPermissionsClient
        cls.client = CodaPermissionsClient()
    
    def test_get_sharing_metadata(self):
        metadata = self.client.get_sharing_metadata(PAI_DOC_ID)
        self.assertIsInstance(metadata, dict)
    
    def test_share_with_user_exists(self):
        self.assertTrue(hasattr(self.client, 'share_with_user'))

if __name__ == '__main__':
    unittest.main()
