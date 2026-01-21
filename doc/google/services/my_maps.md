# Google My Maps

## Overview

My Maps integration integration for Personal AI Infrastructure.

- **API**: `my_maps`
- **Source**: [`src/google/my_maps/client.py`](../../../src/google/my_maps/client.py)
- **Test**: [`tests/test_google_my_maps.py`](../../../tests/test_google_my_maps.py)

## Quick Start

```python
from google.my_maps.client import GoogleMyMapsClient

client = GoogleMyMapsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/my_maps/)
