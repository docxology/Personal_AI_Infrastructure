# Coda Clients - README

Specialized API clients for different Coda operations.

## Available Clients

| Client | Purpose |
|--------|---------|
| `CodaDocsClient` | Document management |
| `CodaPagesClient` | Page operations |
| `CodaTablesClient` | Table operations |
| `CodaColumnsClient` | Column operations |
| `CodaRowsClient` | Row CRUD operations |
| `CodaFormulasClient` | Formula access |
| `CodaControlsClient` | UI controls |
| `CodaPermissionsClient` | ACL and sharing |
| `CodaPublishingClient` | Doc publishing |
| `CodaAutomationsClient` | Automation triggers |
| `CodaAccountClient` | User account info |
| `CodaAnalyticsClient` | Doc and Pack analytics |
| `CodaMiscClient` | Browser link resolution |

## Usage

```python
from coda.clients import CodaRowsClient, CodaPermissionsClient

# Row operations
rows = CodaRowsClient()
data = rows.list_rows(doc_id, table_id)

# Permission management
perms = CodaPermissionsClient()
perms.share_with_user(doc_id, email="user@example.com")
```

## Related

- [../README.md](../README.md) - Main coda module
- [../core/README.md](../core/README.md) - Core infrastructure
