# Coda Module - PAI Integration

## PAI Context

The Coda module provides PAI with structured data management via Coda.io docs and tables.

## PAI Document Controller

Primary document: `NDxZHneeIw` (PAI Controller)

## Key Operations

| Use Case | Client | Method |
|----------|--------|--------|
| Store data | `CodaRowsClient` | `insert_row()` |
| Query records | `CodaRowsClient` | `query_rows()` |
| Manage sharing | `CodaPermissionsClient` | `share_with_user()` |

## Authentication

Token at `~/.claude/coda/token.json` or `CODA_API_TOKEN` env.

## Related

- [README.md](./README.md) - User documentation
- [AGENTS.md](./AGENTS.md) - Agent guide
