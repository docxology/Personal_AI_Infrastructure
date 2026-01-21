# Google Flights

## Overview

Flights integration integration for Personal AI Infrastructure.

- **API**: `flights`
- **Source**: [`src/google/flights/client.py`](../../../src/google/flights/client.py)
- **Test**: [`tests/test_google_flights.py`](../../../tests/test_google_flights.py)

## Quick Start

```python
from google.flights.client import GoogleFlightsClient

client = GoogleFlightsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/flights/)
