# Coda API Module - Agent Documentation

## Purpose

This module provides programmatic access to the Coda.io REST API v1.5.0, enabling document management, table operations, and automation triggering.

## Architecture

```
src/coda/
├── __init__.py          # Package exports
├── base_client.py       # REST client with auth, pagination, rate limiting
├── utils.py             # Token management
├── docs.py              # Document operations
├── pages.py             # Page operations
├── tables.py            # Table/view operations
├── columns.py           # Column operations
├── rows.py              # Row CRUD
├── formulas.py          # Named formula access
├── controls.py          # UI control access
├── permissions.py       # ACL/sharing
├── publishing.py        # Doc publishing
├── automations.py       # Webhook triggers
├── account.py           # User info
├── analytics.py         # Analytics data
└── misc.py              # URL resolution, mutation status
```

## Key Patterns

### Authentication
- Bearer token via `Authorization` header
- Token loaded from `CODA_API_TOKEN` env var or `~/.claude/coda/token.json`

### Pagination
- Uses `items[]`, `nextPageToken`, `nextPageLink` pattern
- `_paginate()` yields items, `_collect_pages()` returns list

### Rate Limiting
- HTTP 429 triggers exponential backoff retry
- Configurable via `max_retries` and `retry_delay`

## Entry Points

| Use Case | Client |
|----------|--------|
| General doc operations | `CodaClient` |
| Table data read/write | `CodaRowsClient` |
| Sharing/permissions | `CodaPermissionsClient` |
| Automation triggers | `CodaAutomationsClient` |

## Testing

```bash
# Requires CODA_API_TOKEN set
cd /Users/4d/Documents/GitHub/Personal_AI_Infrastructure
python -m pytest tests/test_coda_*.py -v
```

## Related Files

- [README.md](file:///Users/4d/Documents/GitHub/Personal_AI_Infrastructure/src/coda/README.md) - User documentation
- [tests/test_coda_integration.py](file:///Users/4d/Documents/GitHub/Personal_AI_Infrastructure/tests/test_coda_integration.py) - Integration tests
