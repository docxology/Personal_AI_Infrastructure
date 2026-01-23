"""
Coda Clients Module

Contains all specialized API client classes.
"""

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
