# Google Analytics

## Overview

Website analytics integration for Personal AI Infrastructure.

- **API**: `analytics`
- **Source**: [`src/google/analytics/client.py`](../../../src/google/analytics/client.py)
- **Test**: [`tests/test_google_analytics.py`](../../../tests/test_google_analytics.py)

## Quick Start

```python
from google.analytics.client import GoogleAnalyticsClient

client = GoogleAnalyticsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_accounts()`
- `list_properties()`
- `list_profiles()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/analytics/)
