# Google Cloud Console

## Overview

Cloud Console integration integration for Personal AI Infrastructure.

- **API**: `cloud_console`
- **Source**: [`src/google/cloud_console/client.py`](../../../src/google/cloud_console/client.py)
- **Test**: [`tests/test_google_cloud_console.py`](../../../tests/test_google_cloud_console.py)

## Quick Start

```python
from google.cloud_console.client import GoogleCloudConsoleClient

client = GoogleCloudConsoleClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/cloud_console/)
