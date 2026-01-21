# Google Images

## Overview

Images integration integration for Personal AI Infrastructure.

- **API**: `images`
- **Source**: [`src/google/images/client.py`](../../../src/google/images/client.py)
- **Test**: [`tests/test_google_images.py`](../../../tests/test_google_images.py)

## Quick Start

```python
from google.images.client import GoogleImagesClient

client = GoogleImagesClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/images/)
