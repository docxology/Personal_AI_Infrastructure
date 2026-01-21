# Google Docs

## Overview

Document creation and editing integration for Personal AI Infrastructure.

- **API**: `docs`
- **Source**: [`src/google/docs/client.py`](../../../src/google/docs/client.py)
- **Test**: [`tests/test_google_docs.py`](../../../tests/test_google_docs.py)

## Quick Start

```python
from google.docs.client import GoogleDocsClient

client = GoogleDocsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `get_document()`
- `create_document()`
- `batch_update()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/docs/)
