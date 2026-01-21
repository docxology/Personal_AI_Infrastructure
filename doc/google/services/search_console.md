# Search Console

## Overview

Search performance integration for Personal AI Infrastructure.

- **API**: `searchconsole`
- **Source**: [`src/google/search_console/client.py`](../../../src/google/search_console/client.py)
- **Test**: [`tests/test_google_search_console.py`](../../../tests/test_google_search_console.py)

## Quick Start

```python
from google.search_console.client import GoogleSearchConsoleClient

client = GoogleSearchConsoleClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_sites()`
- `search_analytics()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/searchconsole/)
