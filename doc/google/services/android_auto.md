# Google Android Auto

## Overview

Android Auto integration integration for Personal AI Infrastructure.

- **API**: `android_auto`
- **Source**: [`src/google/android_auto/client.py`](../../../src/google/android_auto/client.py)
- **Test**: [`tests/test_google_android_auto.py`](../../../tests/test_google_android_auto.py)

## Quick Start

```python
from google.android_auto.client import GoogleAndroidAutoClient

client = GoogleAndroidAutoClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/android_auto/)
