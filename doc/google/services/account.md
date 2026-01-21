# Google Account

## Overview

Account integration integration for Personal AI Infrastructure.

- **API**: `account`
- **Source**: [`src/google/account/client.py`](../../../src/google/account/client.py)
- **Test**: [`tests/test_google_account.py`](../../../tests/test_google_account.py)

## Quick Start

```python
from google.account.client import GoogleAccountClient

client = GoogleAccountClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/account/)
