# Google Photos

## Overview

Photo storage and sharing integration for Personal AI Infrastructure.

- **API**: `photoslibrary`
- **Source**: [`src/google/photos/client.py`](../../../src/google/photos/client.py)
- **Test**: [`tests/test_google_photos.py`](../../../tests/test_google_photos.py)

## Quick Start

```python
from google.photos.client import GooglePhotosClient

client = GooglePhotosClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_albums()`
- `get_album()`
- `search_media()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/photoslibrary/)
