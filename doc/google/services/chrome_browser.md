# Google Chrome Browser

## Overview

Chrome Browser integration integration for Personal AI Infrastructure.

- **API**: `chrome_browser`
- **Source**: [`src/google/chrome_browser/client.py`](../../../src/google/chrome_browser/client.py)
- **Test**: [`tests/test_google_chrome_browser.py`](../../../tests/test_google_chrome_browser.py)

## Quick Start

```python
from google.chrome_browser.client import GoogleChromeBrowserClient

client = GoogleChromeBrowserClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/chrome_browser/)
