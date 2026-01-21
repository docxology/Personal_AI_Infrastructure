# Google Cloud

## Overview

Cloud resource management integration for Personal AI Infrastructure.

- **API**: `cloudresourcemanager`
- **Source**: [`src/google/cloud/client.py`](../../../src/google/cloud/client.py)
- **Test**: [`tests/test_google_cloud.py`](../../../tests/test_google_cloud.py)

## Quick Start

```python
from google.cloud.client import GoogleCloudClient

client = GoogleCloudClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_projects()`
- `get_project()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/cloudresourcemanager/)
