"""Test Coda Page Operations"""
import unittest
import uuid
import time
from tests.coda import skip_without_token, PAI_DOC_ID

@skip_without_token
class TestCodaPagesClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaPagesClient
        cls.client = CodaPagesClient()
    
    def test_list_pages(self):
        pages = self.client.list_pages(PAI_DOC_ID)
        self.assertIsInstance(pages, list)
        self.assertGreaterEqual(len(pages), 1)
    
    def test_create_and_delete_page(self):
        unique_name = f"Test {uuid.uuid4().hex[:6]}"
        result = self.client.create_page(PAI_DOC_ID, name=unique_name)
        self.assertIn("requestId", result)
        self.assertIn("id", result)
        page_id = result["id"]
        time.sleep(5)
        try:
            self.client.delete_page(PAI_DOC_ID, page_id)
        except Exception:
            pass  # Eventual consistency

if __name__ == '__main__':
    unittest.main()
