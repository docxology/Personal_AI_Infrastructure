"""Test Coda Row Operations"""
import unittest
import inspect
from tests.coda import skip_without_token

@skip_without_token
class TestCodaRowsClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaRowsClient
        cls.client = CodaRowsClient()
    
    def test_list_rows_signature(self):
        """Verify list_rows has correct parameters."""
        sig = inspect.signature(self.client.list_rows)
        params = list(sig.parameters.keys())
        self.assertIn('doc_id', params)
        self.assertIn('table_id_or_name', params)
    
    def test_insert_row_signature(self):
        """Verify insert_row has correct parameters."""
        sig = inspect.signature(self.client.insert_row)
        params = list(sig.parameters.keys())
        self.assertIn('doc_id', params)
        self.assertIn('values', params)
    
    def test_update_row_signature(self):
        """Verify update_row has correct parameters."""
        sig = inspect.signature(self.client.update_row)
        params = list(sig.parameters.keys())
        self.assertIn('row_id_or_name', params)
        self.assertIn('values', params)
    
    def test_delete_row_signature(self):
        """Verify delete_row has correct parameters."""
        sig = inspect.signature(self.client.delete_row)
        params = list(sig.parameters.keys())
        self.assertIn('doc_id', params)
        self.assertIn('row_id_or_name', params)
    
    def test_query_rows_signature(self):
        """Verify query_rows has correct parameters."""
        sig = inspect.signature(self.client.query_rows)
        params = list(sig.parameters.keys())
        self.assertIn('column', params)
        self.assertIn('value', params)

if __name__ == '__main__':
    unittest.main()
