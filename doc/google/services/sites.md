# Google Sites

## Overview

Sites integration integration for Personal AI Infrastructure.

- **API**: `sites`
- **Source**: [`src/google/sites/client.py`](../../../src/google/sites/client.py)
- **Test**: [`tests/test_google_sites.py`](../../../tests/test_google_sites.py)

## Quick Start

```python
from google.sites.client import GoogleSitesClient

client = GoogleSitesClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/sites/)
