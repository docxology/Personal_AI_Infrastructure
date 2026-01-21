# Google Maps

## Overview

Maps integration integration for Personal AI Infrastructure.

- **API**: `maps`
- **Source**: [`src/google/maps/client.py`](../../../src/google/maps/client.py)
- **Test**: [`tests/test_google_maps.py`](../../../tests/test_google_maps.py)

## Quick Start

```python
from google.maps.client import GoogleMapsClient

client = GoogleMapsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/maps/)
