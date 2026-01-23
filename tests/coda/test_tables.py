"""Test Coda Table Operations"""
import unittest
import inspect
from tests.coda import skip_without_token, PAI_DOC_ID

@skip_without_token
class TestCodaTablesClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaTablesClient
        cls.client = CodaTablesClient()
    
    def test_list_tables(self):
        tables = self.client.list_tables(PAI_DOC_ID)
        self.assertIsInstance(tables, list)

@skip_without_token
class TestCodaColumnsClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaColumnsClient
        cls.client = CodaColumnsClient()
    
    def test_list_columns_signature(self):
        """Verify list_columns has correct parameters."""
        sig = inspect.signature(self.client.list_columns)
        params = list(sig.parameters.keys())
        self.assertIn('doc_id', params)
        self.assertIn('table_id_or_name', params)

if __name__ == '__main__':
    unittest.main()
