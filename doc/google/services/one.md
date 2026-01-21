# Google One

## Overview

One integration integration for Personal AI Infrastructure.

- **API**: `one`
- **Source**: [`src/google/one/client.py`](../../../src/google/one/client.py)
- **Test**: [`tests/test_google_one.py`](../../../tests/test_google_one.py)

## Quick Start

```python
from google.one.client import GoogleOneClient

client = GoogleOneClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/one/)
