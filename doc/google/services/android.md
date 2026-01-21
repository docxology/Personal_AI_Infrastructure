# Android Publisher

## Overview

App publishing integration for Personal AI Infrastructure.

- **API**: `androidpublisher`
- **Source**: [`src/google/android/client.py`](../../../src/google/android/client.py)
- **Test**: [`tests/test_google_android.py`](../../../tests/test_google_android.py)

## Quick Start

```python
from google.android.client import GoogleAndroidClient

client = GoogleAndroidClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_apks()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/androidpublisher/)
