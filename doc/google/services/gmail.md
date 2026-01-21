# Gmail

## Overview

Email service integration for Personal AI Infrastructure.

- **API**: `gmail`
- **Source**: [`src/google/gmail/client.py`](../../../src/google/gmail/client.py)
- **Test**: [`tests/test_google_gmail.py`](../../../tests/test_google_gmail.py)

## Quick Start

```python
from google.gmail.client import GoogleGmailClient

client = GoogleGmailClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_messages()`
- `send_email()`
- `get_message()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/gmail/)
