# Google Youtube Tv

## Overview

Youtube Tv integration integration for Personal AI Infrastructure.

- **API**: `youtube_tv`
- **Source**: [`src/google/youtube_tv/client.py`](../../../src/google/youtube_tv/client.py)
- **Test**: [`tests/test_google_youtube_tv.py`](../../../tests/test_google_youtube_tv.py)

## Quick Start

```python
from google.youtube_tv.client import GoogleYoutubeTvClient

client = GoogleYoutubeTvClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/youtube_tv/)
