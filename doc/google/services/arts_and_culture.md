# Google Arts And Culture

## Overview

Arts And Culture integration integration for Personal AI Infrastructure.

- **API**: `arts_and_culture`
- **Source**: [`src/google/arts_and_culture/client.py`](../../../src/google/arts_and_culture/client.py)
- **Test**: [`tests/test_google_arts_and_culture.py`](../../../tests/test_google_arts_and_culture.py)

## Quick Start

```python
from google.arts_and_culture.client import GoogleArtsAndCultureClient

client = GoogleArtsAndCultureClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/arts_and_culture/)
