# Google Public DNS

## Overview

DNS management integration for Personal AI Infrastructure.

- **API**: `dns`
- **Source**: [`src/google/public_dns/client.py`](../../../src/google/public_dns/client.py)
- **Test**: [`tests/test_google_public_dns.py`](../../../tests/test_google_public_dns.py)

## Quick Start

```python
from google.public_dns.client import GooglePublicDnsClient

client = GooglePublicDnsClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_managed_zones()`
- `list_records()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/dns/)
