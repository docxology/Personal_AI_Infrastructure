# Google Colab

## Overview

Colab integration integration for Personal AI Infrastructure.

- **API**: `colab`
- **Source**: [`src/google/colab/client.py`](../../../src/google/colab/client.py)
- **Test**: [`tests/test_google_colab.py`](../../../tests/test_google_colab.py)

## Quick Start

```python
from google.colab.client import GoogleColabClient

client = GoogleColabClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/colab/)
