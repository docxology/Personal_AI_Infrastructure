# Google Groups

## Overview

Group management integration for Personal AI Infrastructure.

- **API**: `groupssettings`
- **Source**: [`src/google/groups/client.py`](../../../src/google/groups/client.py)
- **Test**: [`tests/test_google_groups.py`](../../../tests/test_google_groups.py)

## Quick Start

```python
from google.groups.client import GoogleGroupsClient

client = GoogleGroupsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `get_group()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/groupssettings/)
