# Google Maps Platform

## Overview

Maps Platform integration integration for Personal AI Infrastructure.

- **API**: `maps_platform`
- **Source**: [`src/google/maps_platform/client.py`](../../../src/google/maps_platform/client.py)
- **Test**: [`tests/test_google_maps_platform.py`](../../../tests/test_google_maps_platform.py)

## Quick Start

```python
from google.maps_platform.client import GoogleMapsPlatformClient

client = GoogleMapsPlatformClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/maps_platform/)
