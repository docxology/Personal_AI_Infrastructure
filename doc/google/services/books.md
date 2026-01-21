# Google Books

## Overview

Book search and library integration for Personal AI Infrastructure.

- **API**: `books`
- **Source**: [`src/google/books/client.py`](../../../src/google/books/client.py)
- **Test**: [`tests/test_google_books.py`](../../../tests/test_google_books.py)

## Quick Start

```python
from google.books.client import GoogleBooksClient

client = GoogleBooksClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `search_volumes()`
- `get_volume()`
- `list_bookshelves()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/books/)
