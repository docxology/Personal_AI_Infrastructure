# Google Store

## Overview

Store integration integration for Personal AI Infrastructure.

- **API**: `store`
- **Source**: [`src/google/store/client.py`](../../../src/google/store/client.py)
- **Test**: [`tests/test_google_store.py`](../../../tests/test_google_store.py)

## Quick Start

```python
from google.store.client import GoogleStoreClient

client = GoogleStoreClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/store/)
