# Workspace Events

## Overview

Workspace events integration for Personal AI Infrastructure.

- **API**: `workspaceevents`
- **Source**: [`src/google/workspace/client.py`](../../../src/google/workspace/client.py)
- **Test**: [`tests/test_google_workspace.py`](../../../tests/test_google_workspace.py)

## Quick Start

```python
from google.workspace.client import GoogleWorkspaceClient

client = GoogleWorkspaceClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_subscriptions()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/workspaceevents/)
