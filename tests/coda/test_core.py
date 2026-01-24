"""Test Coda Core Module"""
import unittest


class TestCodaCoreModule(unittest.TestCase):
    """Tests for the core module structure."""
    
    def test_base_client_importable(self):
        """Verify CodaClient is importable from core."""
        from coda.core import CodaClient
        self.assertTrue(hasattr(CodaClient, 'BASE_URL'))
    
    def test_errors_importable(self):
        """Verify error classes are importable from core."""
        from coda.core import CodaAPIError, CodaRateLimitError
        self.assertTrue(issubclass(CodaRateLimitError, CodaAPIError))
    
    def test_utils_importable(self):
        """Verify utility functions are importable from core."""
        from coda.core import get_coda_token, extract_doc_id_from_url
        self.assertTrue(callable(get_coda_token))
        self.assertTrue(callable(extract_doc_id_from_url))
    
    def test_direct_error_import(self):
        """Verify direct import from errors module works."""
        from coda.core.errors import CodaAPIError, CodaRateLimitError
        error = CodaAPIError("test", status_code=400)
        self.assertEqual(error.status_code, 400)


class TestCodaClientsModule(unittest.TestCase):
    """Tests for the clients module structure."""
    
    def test_all_clients_importable(self):
        """Verify all client classes are importable from clients."""
        from coda.clients import (
            CodaDocsClient,
            CodaPagesClient,
            CodaTablesClient,
            CodaColumnsClient,
            CodaRowsClient,
            CodaFormulasClient,
            CodaControlsClient,
            CodaPermissionsClient,
            CodaPublishingClient,
            CodaAutomationsClient,
            CodaAccountClient,
            CodaAnalyticsClient,
            CodaMiscClient,
        )
        # All imports successful
        self.assertEqual(len(dir(CodaDocsClient)), len(dir(CodaDocsClient)))


class TestCodaBackwardCompatibility(unittest.TestCase):
    """Tests for backward compatibility of main coda module imports."""
    
    def test_main_module_imports(self):
        """Verify imports from main coda module still work."""
        from coda import (
            CodaClient,
            CodaAPIError,
            CodaRateLimitError,
            CodaRowsClient,
            get_coda_token,
        )
        self.assertTrue(callable(CodaClient))
        self.assertTrue(issubclass(CodaRateLimitError, CodaAPIError))


if __name__ == '__main__':
    unittest.main()
