# Google Ai For Developers

## Overview

Ai For Developers integration integration for Personal AI Infrastructure.

- **API**: `ai_for_developers`
- **Source**: [`src/google/ai_for_developers/client.py`](../../../src/google/ai_for_developers/client.py)
- **Test**: [`tests/test_google_ai_for_developers.py`](../../../tests/test_google_ai_for_developers.py)

## Quick Start

```python
from google.ai_for_developers.client import GoogleAiForDevelopersClient

client = GoogleAiForDevelopersClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/ai_for_developers/)
