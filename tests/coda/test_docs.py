"""Test Coda Document Operations"""
import unittest
from tests.coda import skip_without_token, PAI_DOC_ID

@skip_without_token
class TestCodaDocsClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaDocsClient
        cls.client = CodaDocsClient()
    
    def test_get_doc(self):
        doc = self.client.get_doc(PAI_DOC_ID)
        self.assertEqual(doc["id"], PAI_DOC_ID)
        self.assertIn("name", doc)
    
    def test_get_doc_size(self):
        size = self.client.get_doc_size(PAI_DOC_ID)
        self.assertIn("pageCount", size)

if __name__ == '__main__':
    unittest.main()
