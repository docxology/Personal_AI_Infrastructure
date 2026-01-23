# Source Code - PAI Integration

## PAI Context

This directory contains Python API clients that enable PAI to interact with external services. These clients form the **data plane** of PAI, providing programmatic access to Google Workspace and Coda.io APIs.

## Integration Role

| Component | PAI Function |
|-----------|--------------|
| `google/` | Access to 90+ Google services via MCP or REST |
| `coda/` | Structured data management via Coda docs/tables |

## Usage in PAI

```python
# Import from src modules
from src.google.gmail.client import GmailClient
from src.coda import CodaClient

# Clients auto-authenticate via PAI credential stores
```

## Authentication

All clients use PAI's centralized credential management:
- **Google**: `~/.claude/google-calendar/` directory
- **Coda**: `CODA_API_TOKEN` env or `~/.claude/coda/token.json`

## Related

- [README.md](./README.md) - User documentation
- [AGENTS.md](./AGENTS.md) - Agent integration guide
