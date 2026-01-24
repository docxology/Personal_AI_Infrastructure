# Coda Shadow Sync Module

A **local-first discovery layer** for Coda documents, implementing the "Chroma" pattern for sub-second agent discovery.

## Core Concept

Shadow Sync creates local Markdown "shadow" files with YAML frontmatter for fast grep searches (~6ms) instead of cloud API calls (~500ms+).

## Quick Start

```python
from coda.shadow import ShadowConfig, ShadowSync, shadow_search

# Sync docs to local shadows
config = ShadowConfig(
    shadow_dir=Path("/tmp/shadows"),
    doc_ids=["NDxZHneeIw"]
)
ShadowSync(config).run()

# Fast local search
results = shadow_search(config.shadow_dir, "infrastructure")
```

## PAI Integration

```python
from coda.shadow import (
    sync_pai_shadows,           # Sync PAI Document Controller
    generate_daily_digest_content,  # HTML for daily emails
    generate_weekly_report_content, # HTML for weekly emails
    send_shadow_digest_email,   # Send via Gmail
    quick_search,               # Search default shadows
    get_shadow_stats,           # Get index statistics
)

# Daily/Weekly digest workflow
sync_pai_shadows()
send_shadow_digest_email("user@example.com", digest_type="daily")
```

## Components

| Component | Description |
|-----------|-------------|
| `ShadowConfig` | Configuration dataclass |
| `ShadowSync` | Core sync engine |
| `ShadowIndex` | In-memory index |
| `shadow_search` | Grep-based search |
| `pai_utils` | PAI integration utilities |

## Testing

```bash
pytest tests/coda/test_shadow_sync.py -v  # 17 tests
pytest tests/coda/test_pai_utils.py -v     # 9 tests
```
