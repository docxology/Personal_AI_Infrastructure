# Google Youtube Kids

## Overview

Youtube Kids integration integration for Personal AI Infrastructure.

- **API**: `youtube_kids`
- **Source**: [`src/google/youtube_kids/client.py`](../../../src/google/youtube_kids/client.py)
- **Test**: [`tests/test_google_youtube_kids.py`](../../../tests/test_google_youtube_kids.py)

## Quick Start

```python
from google.youtube_kids.client import GoogleYoutubeKidsClient

client = GoogleYoutubeKidsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/youtube_kids/)
