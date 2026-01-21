# Google Podcasts

## Overview

Podcasts integration integration for Personal AI Infrastructure.

- **API**: `podcasts`
- **Source**: [`src/google/podcasts/client.py`](../../../src/google/podcasts/client.py)
- **Test**: [`tests/test_google_podcasts.py`](../../../tests/test_google_podcasts.py)

## Quick Start

```python
from google.podcasts.client import GooglePodcastsClient

client = GooglePodcastsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/podcasts/)
