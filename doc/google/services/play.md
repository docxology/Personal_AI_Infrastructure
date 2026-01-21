# Google Play

## Overview

Play integration integration for Personal AI Infrastructure.

- **API**: `play`
- **Source**: [`src/google/play/client.py`](../../../src/google/play/client.py)
- **Test**: [`tests/test_google_play.py`](../../../tests/test_google_play.py)

## Quick Start

```python
from google.play.client import GooglePlayClient

client = GooglePlayClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/play/)
