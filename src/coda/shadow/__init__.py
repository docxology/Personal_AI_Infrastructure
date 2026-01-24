"""
Coda Shadow Sync Module

Local-first discovery layer for Coda documents.
Implements the "Chroma" pattern for sub-second agent discovery.
"""

from coda.shadow.shadow_config import ShadowConfig
from coda.shadow.shadow_sync import ShadowSync
from coda.shadow.shadow_index import ShadowIndex
from coda.shadow.shadow_search import shadow_search, ShadowSearchResult

# PAI utilities
from coda.shadow.pai_utils import (
    PAI_DOC_ID,
    get_default_config,
    sync_pai_shadows,
    generate_shadow_summary,
    generate_daily_digest_content,
    generate_weekly_report_content,
    send_shadow_digest_email,
    quick_search,
    get_shadow_stats,
)

__all__ = [
    # Core
    "ShadowConfig",
    "ShadowSync",
    "ShadowIndex",
    "shadow_search",
    "ShadowSearchResult",
    # PAI Utilities
    "PAI_DOC_ID",
    "get_default_config",
    "sync_pai_shadows",
    "generate_shadow_summary",
    "generate_daily_digest_content",
    "generate_weekly_report_content",
    "send_shadow_digest_email",
    "quick_search",
    "get_shadow_stats",
]
