# Google Shopping

## Overview

Shopping listings integration for Personal AI Infrastructure.

- **API**: `content`
- **Source**: [`src/google/shopping/client.py`](../../../src/google/shopping/client.py)
- **Test**: [`tests/test_google_shopping.py`](../../../tests/test_google_shopping.py)

## Quick Start

```python
from google.shopping.client import GoogleShoppingClient

client = GoogleShoppingClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_products()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/content/)
