# Source Code

This directory contains Python API clients for external service integrations.

## Contents

| Directory | Description |
|-----------|-------------|
| `google/` | Google Workspace API clients (Calendar, Gmail, Drive, Tasks, etc.) |
| `coda/` | Coda API client for doc and table operations |

## Architecture

All clients follow the same pattern:

1. **MCP-Based Clients** (`GoogleMCPClient`) - Proxy through Model Context Protocol servers
2. **REST-Based Clients** (`UniversalGoogleClient`) - Direct REST API access for services without MCP

### Google Services

The `google/` directory contains 90+ service subdirectories, each with:
- `client.py` - Service-specific client implementation
- `README.md` - Human documentation
- `AGENTS.md` - Agent integration guide

Key files:
- `base_client.py` - Base class for MCP communication
- `universal_client.py` - REST fallback for non-MCP services
- `setup_auth.py` - OAuth authentication setup

### Coda Client

The `coda/` directory provides:
- Doc operations (list, get, create)
- Table operations (rows, columns, insert, update, delete)
- Permission and sharing management

## Usage

```python
from src.google.gmail.client import GmailClient
from src.google.calendar.client import CalendarClient
from src.coda.client import CodaClient

# Clients handle authentication automatically via MCP
gmail = GmailClient()
messages = gmail.list_messages(max_results=10)
```

## Testing

```bash
pytest tests/google/    # Google client tests
pytest tests/coda/      # Coda client tests
```

---

*Part of [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI)*
