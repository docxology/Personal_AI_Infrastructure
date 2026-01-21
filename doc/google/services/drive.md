# Google Drive

## Overview

Cloud file storage integration for Personal AI Infrastructure.

- **API**: `drive`
- **Source**: [`src/google/drive/client.py`](../../../src/google/drive/client.py)
- **Test**: [`tests/test_google_drive.py`](../../../tests/test_google_drive.py)

## Quick Start

```python
from google.drive.client import GoogleDriveClient

client = GoogleDriveClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_files()`
- `upload_file()`
- `create_folder()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/drive/)
