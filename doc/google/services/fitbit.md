# Fitbit

## Overview

Fitness tracking integration for Personal AI Infrastructure.

- **API**: `fitness`
- **Source**: [`src/google/fitbit/client.py`](../../../src/google/fitbit/client.py)
- **Test**: [`tests/test_google_fitbit.py`](../../../tests/test_google_fitbit.py)

## Quick Start

```python
from google.fitbit.client import GoogleFitbitClient

client = GoogleFitbitClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_data_sources()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/fitness/)
