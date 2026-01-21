# Workspace Admin

## Overview

Workspace administration integration for Personal AI Infrastructure.

- **API**: `admin`
- **Source**: [`src/google/workspace_admin/client.py`](../../../src/google/workspace_admin/client.py)
- **Test**: [`tests/test_google_workspace_admin.py`](../../../tests/test_google_workspace_admin.py)

## Quick Start

```python
from google.workspace_admin.client import GoogleWorkspaceAdminClient

client = GoogleWorkspaceAdminClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_users()`
- `get_user()`
- `list_groups()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/admin/)
