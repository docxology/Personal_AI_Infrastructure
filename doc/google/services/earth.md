# Google Earth

## Overview

Earth integration integration for Personal AI Infrastructure.

- **API**: `earth`
- **Source**: [`src/google/earth/client.py`](../../../src/google/earth/client.py)
- **Test**: [`tests/test_google_earth.py`](../../../tests/test_google_earth.py)

## Quick Start

```python
from google.earth.client import GoogleEarthClient

client = GoogleEarthClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/earth/)
