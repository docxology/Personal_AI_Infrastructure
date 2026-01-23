# Coda.io API Client

A comprehensive Python client for the [Coda.io REST API v1.5.0](https://coda.io/developers/apis/v1).

## Features

- **Bearer Token Authentication** - Secure API token management
- **Automatic Pagination** - Iterator and collection methods for paginated endpoints
- **Rate Limit Handling** - Automatic retry with exponential backoff on HTTP 429
- **Full API Coverage** - 50+ methods across 12 specialized modules

## Installation

The client uses only Python standard library (`urllib`, `json`). No additional dependencies required.

## Configuration

### API Token Setup

1. Go to [Coda Account Settings](https://coda.io/account) → API settings
2. Generate an API token
3. Save it in one of these locations:

**Option A: Environment Variable**
```bash
export CODA_API_TOKEN="your_token_here"
```

**Option B: Token File**
```bash
mkdir -p ~/.claude/coda
echo '{"token": "your_token_here"}' > ~/.claude/coda/token.json
chmod 600 ~/.claude/coda/token.json
```

## Quick Start

```python
from coda import CodaClient

# Initialize client (auto-loads token)
client = CodaClient()

# Verify connection
user = client.whoami()
print(f"Connected as: {user['name']}")

# List your docs
docs = client.list_docs(is_owner=True)
for doc in docs:
    print(f"- {doc['name']} ({doc['id']})")
```

## Usage Examples

### Working with Docs

```python
from coda import CodaDocsClient

client = CodaDocsClient()

# Create a new doc
doc = client.create_doc(title="My New Doc")
print(f"Created: {doc['id']}")

# Search docs
results = client.search_docs("project tracker")

# Get doc info
info = client.get_doc("AbCDeFGH")
print(f"Rows: {info['docSize']['totalRowCount']}")
```

### Working with Tables and Rows

```python
from coda import CodaRowsClient

client = CodaRowsClient()
doc_id = "AbCDeFGH"
table_id = "grid-pqRst-U"

# List rows
rows = client.list_rows(doc_id, table_id)

# Insert a row
result = client.insert_row(doc_id, table_id, {
    "c-name": "John Doe",
    "c-email": "john@example.com",
    "c-status": "Active"
})

# Query rows
active_users = client.query_rows(doc_id, table_id, "c-status", "Active")

# Update a row
client.update_row(doc_id, table_id, "i-rowId", {"c-status": "Inactive"})
```

### Sharing and Permissions

```python
from coda import CodaPermissionsClient

client = CodaPermissionsClient()

# Share with a user
client.share_with_user(doc_id, "colleague@company.com", access="write")

# List permissions
perms = client.list_permissions(doc_id)
```

### Triggering Automations

```python
from coda import CodaAutomationsClient

client = CodaAutomationsClient()

# Trigger a webhook automation
client.trigger_automation(doc_id, "grid-auto-ruleId", {
    "message": "Hello from API!"
})
```

## Available Clients

| Client | Description |
|--------|-------------|
| `CodaClient` | Base client with core doc operations |
| `CodaDocsClient` | Document management |
| `CodaPagesClient` | Page operations and export |
| `CodaTablesClient` | Table/view listing |
| `CodaColumnsClient` | Column metadata |
| `CodaRowsClient` | Row CRUD and querying |
| `CodaFormulasClient` | Named formulas |
| `CodaControlsClient` | UI controls |
| `CodaPermissionsClient` | Sharing and ACLs |
| `CodaPublishingClient` | Publishing to gallery |
| `CodaAutomationsClient` | Webhook triggers |
| `CodaAccountClient` | User info |
| `CodaAnalyticsClient` | Analytics data |
| `CodaMiscClient` | URL resolution, mutation status |

## Rate Limits

The client automatically handles rate limiting. Current Coda limits:

- **Reading**: 100 requests per 6 seconds
- **Writing**: 10 requests per 6 seconds  
- **Content writes**: 5 requests per 10 seconds
- **Listing docs**: 4 requests per 6 seconds

## Error Handling

```python
from coda.base_client import CodaAPIError, CodaRateLimitError

try:
    doc = client.get_doc("invalid-id")
except CodaAPIError as e:
    print(f"API Error {e.status_code}: {e}")
except CodaRateLimitError:
    print("Rate limited - retry later")
```

## Links

- [Coda API Documentation](https://coda.io/developers/apis/v1)
- [Generate API Token](https://coda.io/account)
- [OpenAPI Spec (YAML)](https://coda.io/apis/v1/openapi.yaml)
