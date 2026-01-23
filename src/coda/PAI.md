# Coda Module - PAI Integration

## PAI Context

The Coda module provides PAI with structured data management via Coda.io docs and tables. This enables persistent, collaborative data storage with real-time sync.

## PAI Use Cases

| Use Case | Client | Method |
|----------|--------|--------|
| Store structured data | `CodaRowsClient` | `insert_row()`, `upsert_rows()` |
| Query records | `CodaRowsClient` | `query_rows()`, `list_rows()` |
| Manage permissions | `CodaPermissionsClient` | `share_with_user()` |
| Export content | `CodaPagesClient` | `begin_page_export()` |

## PAI Document Controller

The primary PAI document is `NDxZHneeIw` - used for:
- Configuration storage
- Task tracking
- Integration state

## Authentication

Token stored at `~/.claude/coda/token.json` or `CODA_API_TOKEN` env.

## Related

- [README.md](./README.md) - User documentation
- [AGENTS.md](./AGENTS.md) - Agent integration guide
