# Google Voice

## Overview

Voice integration integration for Personal AI Infrastructure.

- **API**: `voice`
- **Source**: [`src/google/voice/client.py`](../../../src/google/voice/client.py)
- **Test**: [`tests/test_google_voice.py`](../../../tests/test_google_voice.py)

## Quick Start

```python
from google.voice.client import GoogleVoiceClient

client = GoogleVoiceClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/voice/)
