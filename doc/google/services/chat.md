# Google Chat

## Overview

Team messaging integration for Personal AI Infrastructure.

- **API**: `chat`
- **Source**: [`src/google/chat/client.py`](../../../src/google/chat/client.py)
- **Test**: [`tests/test_google_chat.py`](../../../tests/test_google_chat.py)

## Quick Start

```python
from google.chat.client import GoogleChatClient

client = GoogleChatClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_spaces()`
- `get_space()`
- `create_message()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/chat/)
