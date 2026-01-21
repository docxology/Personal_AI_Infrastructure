# Google Fonts

## Overview

Web fonts library integration for Personal AI Infrastructure.

- **API**: `webfonts`
- **Source**: [`src/google/fonts/client.py`](../../../src/google/fonts/client.py)
- **Test**: [`tests/test_google_fonts.py`](../../../tests/test_google_fonts.py)

## Quick Start

```python
from google.fonts.client import GoogleFontsClient

client = GoogleFontsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_fonts()`
- `get_font()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/webfonts/)
