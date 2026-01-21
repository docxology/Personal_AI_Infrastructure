# Vertex AI

## Overview

AI/ML platform integration for Personal AI Infrastructure.

- **API**: `aiplatform`
- **Source**: [`src/google/vertex_ai/client.py`](../../../src/google/vertex_ai/client.py)
- **Test**: [`tests/test_google_vertex_ai.py`](../../../tests/test_google_vertex_ai.py)

## Quick Start

```python
from google.vertex_ai.client import GoogleVertexAiClient

client = GoogleVertexAiClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_models()`
- `list_endpoints()`
- `predict()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/aiplatform/)
