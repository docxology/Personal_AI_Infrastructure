# Google For Education

## Overview

For Education integration integration for Personal AI Infrastructure.

- **API**: `for_education`
- **Source**: [`src/google/for_education/client.py`](../../../src/google/for_education/client.py)
- **Test**: [`tests/test_google_for_education.py`](../../../tests/test_google_for_education.py)

## Quick Start

```python
from google.for_education.client import GoogleForEducationClient

client = GoogleForEducationClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/for_education/)
