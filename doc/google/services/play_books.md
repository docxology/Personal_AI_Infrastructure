# Play Books

## Overview

E-book platform integration for Personal AI Infrastructure.

- **API**: `books`
- **Source**: [`src/google/play_books/client.py`](../../../src/google/play_books/client.py)
- **Test**: [`tests/test_google_play_books.py`](../../../tests/test_google_play_books.py)

## Quick Start

```python
from google.play_books.client import GooglePlayBooksClient

client = GooglePlayBooksClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `search()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/books/)
