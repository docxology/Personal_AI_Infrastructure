# Google Family Link

## Overview

Family Link integration integration for Personal AI Infrastructure.

- **API**: `family_link`
- **Source**: [`src/google/family_link/client.py`](../../../src/google/family_link/client.py)
- **Test**: [`tests/test_google_family_link.py`](../../../tests/test_google_family_link.py)

## Quick Start

```python
from google.family_link.client import GoogleFamilyLinkClient

client = GoogleFamilyLinkClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/family_link/)
