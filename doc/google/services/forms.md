# Google Forms

## Overview

Survey and form creation integration for Personal AI Infrastructure.

- **API**: `forms`
- **Source**: [`src/google/forms/client.py`](../../../src/google/forms/client.py)
- **Test**: [`tests/test_google_forms.py`](../../../tests/test_google_forms.py)

## Quick Start

```python
from google.forms.client import GoogleFormsClient

client = GoogleFormsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `get_form()`
- `list_responses()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/forms/)
