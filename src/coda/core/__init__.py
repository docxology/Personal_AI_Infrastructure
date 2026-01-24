"""
Coda Core Module

Contains base client infrastructure, errors, and utilities.
"""

from coda.core.base_client import CodaClient
from coda.core.errors import CodaAPIError, CodaRateLimitError
from coda.core.utils import (
    get_coda_token,
    get_coda_token_path,
    save_coda_token,
    extract_doc_id_from_url,
)

__all__ = [
    "CodaClient",
    "CodaAPIError",
    "CodaRateLimitError",
    "get_coda_token",
    "get_coda_token_path",
    "save_coda_token",
    "extract_doc_id_from_url",
]
