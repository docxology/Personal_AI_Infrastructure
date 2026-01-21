# Google Sheets

## Overview

Spreadsheet creation and editing integration for Personal AI Infrastructure.

- **API**: `sheets`
- **Source**: [`src/google/sheets/client.py`](../../../src/google/sheets/client.py)
- **Test**: [`tests/test_google_sheets.py`](../../../tests/test_google_sheets.py)

## Quick Start

```python
from google.sheets.client import GoogleSheetsClient

client = GoogleSheetsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `get_values()`
- `update_values()`
- `append_values()`
- `create_spreadsheet()`
- `get_spreadsheet()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/sheets/)
