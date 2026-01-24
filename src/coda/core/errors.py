"""
Coda API Errors

Custom exception classes for Coda API operations.
"""

from typing import Dict, Optional


class CodaAPIError(Exception):
    """Exception raised for Coda API errors."""
    
    def __init__(self, message: str, status_code: Optional[int] = None, response: Optional[Dict] = None):
        self.status_code = status_code
        self.response = response
        super().__init__(message)


class CodaRateLimitError(CodaAPIError):
    """Exception raised when rate limited (HTTP 429)."""
    pass
