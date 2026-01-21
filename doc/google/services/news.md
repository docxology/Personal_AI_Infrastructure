# Google News

## Overview

News integration integration for Personal AI Infrastructure.

- **API**: `news`
- **Source**: [`src/google/news/client.py`](../../../src/google/news/client.py)
- **Test**: [`tests/test_google_news.py`](../../../tests/test_google_news.py)

## Quick Start

```python
from google.news.client import GoogleNewsClient

client = GoogleNewsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/news/)
