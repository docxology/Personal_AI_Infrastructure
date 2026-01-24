"""Test Coda Misc and Utils"""
import unittest
from tests.coda import skip_without_token, PAI_DOC_ID

@skip_without_token
class TestCodaMiscClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaMiscClient
        cls.client = CodaMiscClient()
    
    def test_resolve_browser_link(self):
        url = f"https://coda.io/d/_d{PAI_DOC_ID}"
        result = self.client.resolve_browser_link(url)
        self.assertIn("resource", result)

class TestCodaUtils(unittest.TestCase):
    def test_extract_doc_id_standard(self):
        from coda.core.utils import extract_doc_id_from_url
        doc_id = extract_doc_id_from_url("https://coda.io/d/_dAbCDeFGH/Page")
        self.assertEqual(doc_id, "AbCDeFGH")
    
    def test_extract_doc_id_named(self):
        from coda.core.utils import extract_doc_id_from_url
        doc_id = extract_doc_id_from_url("https://coda.io/d/PAI_dNDxZHneeIw/PAI_su")
        self.assertEqual(doc_id, "NDxZHneeIw")

class TestCodaBaseClient(unittest.TestCase):
    def test_base_url(self):
        from coda.core.base_client import CodaClient
        self.assertEqual(CodaClient.BASE_URL, "https://coda.io/apis/v1")
    
    def test_error_hierarchy(self):
        from coda.core.errors import CodaAPIError, CodaRateLimitError
        self.assertTrue(issubclass(CodaRateLimitError, CodaAPIError))

if __name__ == '__main__':
    unittest.main()

