# Chrome Web Store

## Overview

Extension publishing integration for Personal AI Infrastructure.

- **API**: `chromewebstore`
- **Source**: [`src/google/chrome_web_store/client.py`](../../../src/google/chrome_web_store/client.py)
- **Test**: [`tests/test_google_chrome_web_store.py`](../../../tests/test_google_chrome_web_store.py)

## Quick Start

```python
from google.chrome_web_store.client import GoogleChromeWebStoreClient

client = GoogleChromeWebStoreClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `get_item()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/chromewebstore/)
