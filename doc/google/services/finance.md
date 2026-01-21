# Google Finance

## Overview

Finance integration integration for Personal AI Infrastructure.

- **API**: `finance`
- **Source**: [`src/google/finance/client.py`](../../../src/google/finance/client.py)
- **Test**: [`tests/test_google_finance.py`](../../../tests/test_google_finance.py)

## Quick Start

```python
from google.finance.client import GoogleFinanceClient

client = GoogleFinanceClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/finance/)
