# Google Pay

## Overview

Pay integration integration for Personal AI Infrastructure.

- **API**: `pay`
- **Source**: [`src/google/pay/client.py`](../../../src/google/pay/client.py)
- **Test**: [`tests/test_google_pay.py`](../../../tests/test_google_pay.py)

## Quick Start

```python
from google.pay.client import GooglePayClient

client = GooglePayClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/pay/)
