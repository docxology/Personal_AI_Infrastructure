# Street View

## Overview

Street imagery integration for Personal AI Infrastructure.

- **API**: `streetviewpublish`
- **Source**: [`src/google/street_view/client.py`](../../../src/google/street_view/client.py)
- **Test**: [`tests/test_google_street_view.py`](../../../tests/test_google_street_view.py)

## Quick Start

```python
from google.street_view.client import GoogleStreetViewClient

client = GoogleStreetViewClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_photos()`
- `get_photo()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/streetviewpublish/)
