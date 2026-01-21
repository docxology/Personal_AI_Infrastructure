# Google Cloud Apis List

## Overview

Cloud Apis List integration integration for Personal AI Infrastructure.

- **API**: `cloud_apis_list`
- **Source**: [`src/google/cloud_apis_list/client.py`](../../../src/google/cloud_apis_list/client.py)
- **Test**: [`tests/test_google_cloud_apis_list.py`](../../../tests/test_google_cloud_apis_list.py)

## Quick Start

```python
from google.cloud_apis_list.client import GoogleCloudApisListClient

client = GoogleCloudApisListClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/cloud_apis_list/)
