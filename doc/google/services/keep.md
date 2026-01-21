# Google Keep

## Overview

Note-taking integration for Personal AI Infrastructure.

- **API**: `keep`
- **Source**: [`src/google/keep/client.py`](../../../src/google/keep/client.py)
- **Test**: [`tests/test_google_keep.py`](../../../tests/test_google_keep.py)

## Quick Start

```python
from google.keep.client import GoogleKeepClient

client = GoogleKeepClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_notes()`
- `get_note()`
- `create_note()`
- `delete_note()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/keep/)
