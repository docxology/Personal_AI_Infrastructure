# Google Alerts

## Overview

Alerts integration integration for Personal AI Infrastructure.

- **API**: `alerts`
- **Source**: [`src/google/alerts/client.py`](../../../src/google/alerts/client.py)
- **Test**: [`tests/test_google_alerts.py`](../../../tests/test_google_alerts.py)

## Quick Start

```python
from google.alerts.client import GoogleAlertsClient

client = GoogleAlertsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/alerts/)
