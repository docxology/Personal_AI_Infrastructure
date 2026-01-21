# Marketing Platform

## Overview

Marketing tools integration for Personal AI Infrastructure.

- **API**: `marketingplatformadmin`
- **Source**: [`src/google/marketing_platform/client.py`](../../../src/google/marketing_platform/client.py)
- **Test**: [`tests/test_google_marketing_platform.py`](../../../tests/test_google_marketing_platform.py)

## Quick Start

```python
from google.marketing_platform.client import GoogleMarketingPlatformClient

client = GoogleMarketingPlatformClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_organizations()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/marketingplatformadmin/)
