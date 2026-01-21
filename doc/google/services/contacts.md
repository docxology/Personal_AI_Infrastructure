# Google Contacts

## Overview

Contact management integration for Personal AI Infrastructure.

- **API**: `people`
- **Source**: [`src/google/contacts/client.py`](../../../src/google/contacts/client.py)
- **Test**: [`tests/test_google_contacts.py`](../../../tests/test_google_contacts.py)

## Quick Start

```python
from google.contacts.client import GoogleContactsClient

client = GoogleContactsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_connections()`
- `get_person()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/people/)
