# Google Ads

## Overview

Advertising platform integration for Personal AI Infrastructure.

- **API**: `adsense`
- **Source**: [`src/google/ads/client.py`](../../../src/google/ads/client.py)
- **Test**: [`tests/test_google_ads.py`](../../../tests/test_google_ads.py)

## Quick Start

```python
from google.ads.client import GoogleAdsClient

client = GoogleAdsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_accounts()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/adsense/)
