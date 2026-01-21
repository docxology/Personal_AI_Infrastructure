# Google Web Designer

## Overview

Web Designer integration integration for Personal AI Infrastructure.

- **API**: `web_designer`
- **Source**: [`src/google/web_designer/client.py`](../../../src/google/web_designer/client.py)
- **Test**: [`tests/test_google_web_designer.py`](../../../tests/test_google_web_designer.py)

## Quick Start

```python
from google.web_designer.client import GoogleWebDesignerClient

client = GoogleWebDesignerClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/web_designer/)
