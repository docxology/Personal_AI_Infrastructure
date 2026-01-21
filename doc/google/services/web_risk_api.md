# Web Risk API

## Overview

Threat detection integration for Personal AI Infrastructure.

- **API**: `webrisk`
- **Source**: [`src/google/web_risk_api/client.py`](../../../src/google/web_risk_api/client.py)
- **Test**: [`tests/test_google_web_risk_api.py`](../../../tests/test_google_web_risk_api.py)

## Quick Start

```python
from google.web_risk_api.client import GoogleWebRiskApiClient

client = GoogleWebRiskApiClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `search_uris()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/webrisk/)
