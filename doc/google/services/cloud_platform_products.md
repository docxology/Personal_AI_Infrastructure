# Google Cloud Platform Products

## Overview

Cloud Platform Products integration integration for Personal AI Infrastructure.

- **API**: `cloud_platform_products`
- **Source**: [`src/google/cloud_platform_products/client.py`](../../../src/google/cloud_platform_products/client.py)
- **Test**: [`tests/test_google_cloud_platform_products.py`](../../../tests/test_google_cloud_platform_products.py)

## Quick Start

```python
from google.cloud_platform_products.client import GoogleCloudPlatformProductsClient

client = GoogleCloudPlatformProductsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/cloud_platform_products/)
