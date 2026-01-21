# Google Manufacturer Center

## Overview

Manufacturer Center integration integration for Personal AI Infrastructure.

- **API**: `manufacturer_center`
- **Source**: [`src/google/manufacturer_center/client.py`](../../../src/google/manufacturer_center/client.py)
- **Test**: [`tests/test_google_manufacturer_center.py`](../../../tests/test_google_manufacturer_center.py)

## Quick Start

```python
from google.manufacturer_center.client import GoogleManufacturerCenterClient

client = GoogleManufacturerCenterClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/manufacturer_center/)
