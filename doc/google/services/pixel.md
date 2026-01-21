# Google Pixel

## Overview

Pixel integration integration for Personal AI Infrastructure.

- **API**: `pixel`
- **Source**: [`src/google/pixel/client.py`](../../../src/google/pixel/client.py)
- **Test**: [`tests/test_google_pixel.py`](../../../tests/test_google_pixel.py)

## Quick Start

```python
from google.pixel.client import GooglePixelClient

client = GooglePixelClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/pixel/)
