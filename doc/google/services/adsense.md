# Google AdSense

## Overview

Ad monetization integration for Personal AI Infrastructure.

- **API**: `adsense`
- **Source**: [`src/google/adsense/client.py`](../../../src/google/adsense/client.py)
- **Test**: [`tests/test_google_adsense.py`](../../../tests/test_google_adsense.py)

## Quick Start

```python
from google.adsense.client import GoogleAdsenseClient

client = GoogleAdsenseClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_accounts()`
- `get_account()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/adsense/)
