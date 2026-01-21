# Google Scholar

## Overview

Scholar integration integration for Personal AI Infrastructure.

- **API**: `scholar`
- **Source**: [`src/google/scholar/client.py`](../../../src/google/scholar/client.py)
- **Test**: [`tests/test_google_scholar.py`](../../../tests/test_google_scholar.py)

## Quick Start

```python
from google.scholar.client import GoogleScholarClient

client = GoogleScholarClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/scholar/)
