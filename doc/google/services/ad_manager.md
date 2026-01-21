# Ad Manager

## Overview

Ad exchange integration for Personal AI Infrastructure.

- **API**: `adexchangebuyer`
- **Source**: [`src/google/ad_manager/client.py`](../../../src/google/ad_manager/client.py)
- **Test**: [`tests/test_google_ad_manager.py`](../../../tests/test_google_ad_manager.py)

## Quick Start

```python
from google.ad_manager.client import GoogleAdManagerClient

client = GoogleAdManagerClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_accounts()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/adexchangebuyer/)
