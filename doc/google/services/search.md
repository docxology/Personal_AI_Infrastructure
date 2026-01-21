# Google Search

## Overview

Search integration integration for Personal AI Infrastructure.

- **API**: `search`
- **Source**: [`src/google/search/client.py`](../../../src/google/search/client.py)
- **Test**: [`tests/test_google_search.py`](../../../tests/test_google_search.py)

## Quick Start

```python
from google.search.client import GoogleSearchClient

client = GoogleSearchClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/search/)
