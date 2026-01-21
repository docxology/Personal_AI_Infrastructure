# Google Meet

## Overview

Video conferencing integration for Personal AI Infrastructure.

- **API**: `meet`
- **Source**: [`src/google/meet/client.py`](../../../src/google/meet/client.py)
- **Test**: [`tests/test_google_meet.py`](../../../tests/test_google_meet.py)

## Quick Start

```python
from google.meet.client import GoogleMeetClient

client = GoogleMeetClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `get_space()`
- `create_space()`
- `end_active_conference()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/meet/)
