# Coda Module - Agent Guide

## Purpose

Interact with Coda.io documents, tables, and rows via REST API. Includes a **Shadow Sync** module for local-first discovery.

## Module Structure

- **coda.core** - Base client, errors, utilities
- **coda.clients** - Specialized API clients (13 total)
- **coda.shadow** - Local-first discovery layer

## Key Entry Points

| Task | Client/Component |
|------|------------------|
| Read/write rows | `CodaRowsClient` |
| Manage tables | `CodaTablesClient` |
| Share documents | `CodaPermissionsClient` |
| Account info | `CodaAccountClient` |
| **Local search** | `shadow_search()` |
| **Sync to local** | `ShadowSync` |

## Patterns

### API Client

```python
from coda import CodaRowsClient

client = CodaRowsClient()
rows = client.list_rows(doc_id, table_id)
client.insert_row(doc_id, table_id, values={"Name": "Test"})
```

### Shadow Sync (Local-First)

```python
from coda.shadow import ShadowConfig, ShadowSync, shadow_search

# Sync once
config = ShadowConfig(doc_ids=["NDxZHneeIw"])
ShadowSync(config).run()

# Search locally first (Cartographer's Oath)
results = shadow_search(config.shadow_dir, "query")
```

## Testing

```bash
pytest tests/coda/ -v
# Expected: 49+ passed
```

## Authentication

Uses `~/.claude/coda/token.json` or `CODA_API_TOKEN` env.

## Related Files

- [core/](./core/) - Base infrastructure
- [clients/](./clients/) - API clients
- [shadow/](./shadow/) - Local-first discovery
