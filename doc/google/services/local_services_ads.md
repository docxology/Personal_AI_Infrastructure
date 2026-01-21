# Local Services Ads

## Overview

Local advertising integration for Personal AI Infrastructure.

- **API**: `localservices`
- **Source**: [`src/google/local_services_ads/client.py`](../../../src/google/local_services_ads/client.py)
- **Test**: [`tests/test_google_local_services_ads.py`](../../../tests/test_google_local_services_ads.py)

## Quick Start

```python
from google.local_services_ads.client import GoogleLocalServicesAdsClient

client = GoogleLocalServicesAdsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `search_leads()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/localservices/)
