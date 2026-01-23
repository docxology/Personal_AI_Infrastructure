"""Test Coda Formulas and Controls"""
import unittest
from tests.coda import skip_without_token, PAI_DOC_ID

@skip_without_token
class TestCodaFormulasClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaFormulasClient
        cls.client = CodaFormulasClient()
    
    def test_list_formulas(self):
        formulas = self.client.list_formulas(PAI_DOC_ID)
        self.assertIsInstance(formulas, list)

@skip_without_token
class TestCodaControlsClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from coda import CodaControlsClient
        cls.client = CodaControlsClient()
    
    def test_list_controls(self):
        controls = self.client.list_controls(PAI_DOC_ID)
        self.assertIsInstance(controls, list)

if __name__ == '__main__':
    unittest.main()
