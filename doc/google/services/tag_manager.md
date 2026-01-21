# Google Tag Manager

## Overview

Tag management integration for Personal AI Infrastructure.

- **API**: `tagmanager`
- **Source**: [`src/google/tag_manager/client.py`](../../../src/google/tag_manager/client.py)
- **Test**: [`tests/test_google_tag_manager.py`](../../../tests/test_google_tag_manager.py)

## Quick Start

```python
from google.tag_manager.client import GoogleTagManagerClient

client = GoogleTagManagerClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_accounts()`
- `list_containers()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/tagmanager/)
