"""
Coda.io API Client Package

A comprehensive REST API client for Coda.io v1.5.0.
"""

from coda.base_client import CodaClient
from coda.docs import CodaDocsClient
from coda.pages import CodaPagesClient
from coda.tables import CodaTablesClient
from coda.columns import CodaColumnsClient
from coda.rows import CodaRowsClient
from coda.formulas import CodaFormulasClient
from coda.controls import CodaControlsClient
from coda.permissions import CodaPermissionsClient
from coda.publishing import CodaPublishingClient
from coda.automations import CodaAutomationsClient
from coda.account import CodaAccountClient
from coda.analytics import CodaAnalyticsClient
from coda.misc import CodaMiscClient

__all__ = [
    "CodaClient",
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
]

__version__ = "1.0.0"
