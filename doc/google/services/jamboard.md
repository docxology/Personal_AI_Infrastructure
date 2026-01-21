# Google Jamboard

## Overview

Jamboard integration integration for Personal AI Infrastructure.

- **API**: `jamboard`
- **Source**: [`src/google/jamboard/client.py`](../../../src/google/jamboard/client.py)
- **Test**: [`tests/test_google_jamboard.py`](../../../tests/test_google_jamboard.py)

## Quick Start

```python
from google.jamboard.client import GoogleJamboardClient

client = GoogleJamboardClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/jamboard/)
