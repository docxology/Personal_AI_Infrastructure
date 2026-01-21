# Google Nest

## Overview

Smart home devices integration for Personal AI Infrastructure.

- **API**: `smartdevicemanagement`
- **Source**: [`src/google/nest/client.py`](../../../src/google/nest/client.py)
- **Test**: [`tests/test_google_nest.py`](../../../tests/test_google_nest.py)

## Quick Start

```python
from google.nest.client import GoogleNestClient

client = GoogleNestClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_devices()`
- `get_device()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/smartdevicemanagement/)
