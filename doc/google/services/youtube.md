# YouTube

## Overview

Video sharing and streaming integration for Personal AI Infrastructure.

- **API**: `youtube`
- **Source**: [`src/google/youtube/client.py`](../../../src/google/youtube/client.py)
- **Test**: [`tests/test_google_youtube.py`](../../../tests/test_google_youtube.py)

## Quick Start

```python
from google.youtube.client import GoogleYoutubeClient

client = GoogleYoutubeClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `search()`
- `get_video()`
- `list_channels()`
- `list_playlists()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/youtube/)
