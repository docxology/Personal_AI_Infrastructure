"""
Coda.io API Client Package

A comprehensive REST API client for Coda.io v1.5.0.

Structure:
- coda.core: Base client, errors, and utilities
- coda.clients: Specialized API clients
- coda.shadow: Local-first discovery layer
"""

# Core exports
from coda.core import (
    CodaClient,
    CodaAPIError,
    CodaRateLimitError,
    get_coda_token,
    get_coda_token_path,
    save_coda_token,
    extract_doc_id_from_url,
)

# Client exports
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

# Shadow module exports
from coda.shadow import (
    ShadowConfig,
    ShadowSync,
    ShadowIndex,
    shadow_search,
    ShadowSearchResult,
)

__all__ = [
    # Core
    "CodaClient",
    "CodaAPIError",
    "CodaRateLimitError",
    "get_coda_token",
    "get_coda_token_path",
    "save_coda_token",
    "extract_doc_id_from_url",
    # Clients
    "CodaDocsClient",
    "CodaPagesClient",
    "CodaTablesClient",
    "CodaColumnsClient",
    "CodaRowsClient",
    "CodaFormulasClient",
    "CodaControlsClient",
    "CodaPermissionsClient",
    "CodaPublishingClient",
    "CodaAutomationsClient",
    "CodaAccountClient",
    "CodaAnalyticsClient",
    "CodaMiscClient",
    # Shadow
    "ShadowConfig",
    "ShadowSync",
    "ShadowIndex",
    "shadow_search",
    "ShadowSearchResult",
]

__version__ = "2.1.0"
