# Google Chromebook Chromeos

## Overview

Chromebook Chromeos integration integration for Personal AI Infrastructure.

- **API**: `chromebook_chromeos`
- **Source**: [`src/google/chromebook_chromeos/client.py`](../../../src/google/chromebook_chromeos/client.py)
- **Test**: [`tests/test_google_chromebook_chromeos.py`](../../../tests/test_google_chromebook_chromeos.py)

## Quick Start

```python
from google.chromebook_chromeos.client import GoogleChromebookChromeosClient

client = GoogleChromebookChromeosClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/chromebook_chromeos/)
