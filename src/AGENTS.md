# Source Code - Agents Guide

## Overview

This directory contains Python API clients that enable PAI to interact with external services.

## Client Architecture

### Two Client Patterns

1. **MCP Clients** - Proxy through Model Context Protocol servers
   - Used for: Calendar, Gmail, Drive, Tasks
   - Base class: `GoogleMCPClient` in `google/base_client.py`

2. **REST Clients** - Direct HTTP API access
   - Used for: Services without MCP support
   - Base class: `UniversalGoogleClient` in `google/universal_client.py`

## Integration Points

| Service | Client Location | MCP Tool Prefix |
|---------|-----------------|-----------------|
| Calendar | `google/calendar/client.py` | `mcp__google-calendar__` |
| Gmail | `google/gmail/client.py` | `mcp__gmail__` |
| Drive | `google/drive/client.py` | `mcp__google-drive__` |
| Tasks | `google/tasks/client.py` | `mcp__google-tasks__` |
| Coda | `coda/client.py` | Direct REST |

## Adding a New Service

1. Create directory: `google/{service_name}/`
2. Create `client.py` extending `GoogleMCPClient` or `UniversalGoogleClient`
3. Add `README.md` and `AGENTS.md`
4. Add tests in `tests/google/test_{service}.py`

## Common Operations

### Read client state
```python
client = GmailClient()
# Clients auto-initialize MCP connection
```

### Handle errors
```python
try:
    result = client.some_method()
except Exception as e:
    # All clients log errors and raise
    pass
```

## Testing

```bash
pytest tests/google/                    # All Google tests
pytest tests/google/test_gmail.py       # Specific service
pytest tests/coda/                      # Coda tests
```

## Key Files

| File | Purpose |
|------|---------|
| `google/base_client.py` | MCP client base class |
| `google/universal_client.py` | REST client for non-MCP services |
| `google/setup_auth.py` | OAuth flow setup |
| `coda/base_client.py` | Coda REST API base client |
| `coda/utils.py` | Coda token management |

---

*Part of [PAI (Personal AI Infrastructure)](../README.md)*
