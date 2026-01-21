# Google Android Studio

## Overview

Android Studio integration integration for Personal AI Infrastructure.

- **API**: `android_studio`
- **Source**: [`src/google/android_studio/client.py`](../../../src/google/android_studio/client.py)
- **Test**: [`tests/test_google_android_studio.py`](../../../tests/test_google_android_studio.py)

## Quick Start

```python
from google.android_studio.client import GoogleAndroidStudioClient

client = GoogleAndroidStudioClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/android_studio/)
