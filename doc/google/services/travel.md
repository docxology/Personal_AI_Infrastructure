# Travel Impact

## Overview

Travel emissions integration for Personal AI Infrastructure.

- **API**: `travelimpactmodel`
- **Source**: [`src/google/travel/client.py`](../../../src/google/travel/client.py)
- **Test**: [`tests/test_google_travel.py`](../../../tests/test_google_travel.py)

## Quick Start

```python
from google.travel.client import GoogleTravelClient

client = GoogleTravelClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `compute_flight_emissions()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/travelimpactmodel/)
