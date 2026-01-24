# Coda.io API Client

A modular REST API client for Coda.io v1.5.0 with local-first Shadow Sync.

## Structure

```
coda/
├── core/           # Infrastructure
│   ├── base_client.py   # REST client with auth/pagination
│   ├── errors.py        # CodaAPIError, CodaRateLimitError
│   └── utils.py         # Token management
├── clients/        # Specialized API clients (13 total)
│   ├── docs.py, pages.py, tables.py, columns.py, rows.py
│   ├── formulas.py, controls.py, permissions.py
│   ├── publishing.py, automations.py, account.py
│   ├── analytics.py, misc.py
├── shadow/         # Local-first discovery layer
│   ├── shadow_config.py  # Configuration
│   ├── shadow_sync.py    # Sync engine
│   ├── shadow_index.py   # In-memory index
│   └── shadow_search.py  # Grep-based search
└── __init__.py     # Package exports
```

## Quick Start

### API Client Usage

```python
from coda import CodaRowsClient, CodaPermissionsClient

# Row operations
client = CodaRowsClient()
rows = client.list_rows(doc_id="NDxZHneeIw", table_id_or_name="Tasks")

# Permissions
perms = CodaPermissionsClient()
perms.share_with_user(doc_id, email="user@example.com")
```

### Shadow Sync Usage

```python
from pathlib import Path
from coda.shadow import ShadowConfig, ShadowSync, shadow_search

# Sync Coda docs to local shadows
config = ShadowConfig(
    shadow_dir=Path("/tmp/shadows"),
    doc_ids=["NDxZHneeIw"]
)
ShadowSync(config).run()

# Fast local search (~50ms)
results = shadow_search(config.shadow_dir, "infrastructure")
for r in results:
    print(f"{r.page_name}: {r.browser_link}")
```

## Authentication

Token loaded from `CODA_API_TOKEN` env variable or `~/.claude/coda/token.json`.

## Testing

```bash
pytest tests/coda/ -v
```

## Related

- [AGENTS.md](./AGENTS.md) - Agent integration guide
- [PAI.md](./PAI.md) - PAI integration context
- [shadow/README.md](./shadow/README.md) - Shadow Sync details
