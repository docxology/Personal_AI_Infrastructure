# Google Youtube Music

## Overview

Youtube Music integration integration for Personal AI Infrastructure.

- **API**: `youtube_music`
- **Source**: [`src/google/youtube_music/client.py`](../../../src/google/youtube_music/client.py)
- **Test**: [`tests/test_google_youtube_music.py`](../../../tests/test_google_youtube_music.py)

## Quick Start

```python
from google.youtube_music.client import GoogleYoutubeMusicClient

client = GoogleYoutubeMusicClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/youtube_music/)
