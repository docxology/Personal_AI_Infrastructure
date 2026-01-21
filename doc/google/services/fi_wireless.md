# Google Fi Wireless

## Overview

Fi Wireless integration integration for Personal AI Infrastructure.

- **API**: `fi_wireless`
- **Source**: [`src/google/fi_wireless/client.py`](../../../src/google/fi_wireless/client.py)
- **Test**: [`tests/test_google_fi_wireless.py`](../../../tests/test_google_fi_wireless.py)

## Quick Start

```python
from google.fi_wireless.client import GoogleFiWirelessClient

client = GoogleFiWirelessClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/fi_wireless/)
