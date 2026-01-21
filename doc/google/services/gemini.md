# Gemini

## Overview

Generative AI integration for Personal AI Infrastructure.

- **API**: `generativelanguage`
- **Source**: [`src/google/gemini/client.py`](../../../src/google/gemini/client.py)
- **Test**: [`tests/test_google_gemini.py`](../../../tests/test_google_gemini.py)

## Quick Start

```python
from google.gemini.client import GoogleGeminiClient

client = GoogleGeminiClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_models()`
- `generate_content()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/generativelanguage/)
