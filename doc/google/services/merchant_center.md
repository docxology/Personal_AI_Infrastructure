# Merchant Center

## Overview

E-commerce management integration for Personal AI Infrastructure.

- **API**: `content`
- **Source**: [`src/google/merchant_center/client.py`](../../../src/google/merchant_center/client.py)
- **Test**: [`tests/test_google_merchant_center.py`](../../../tests/test_google_merchant_center.py)

## Quick Start

```python
from google.merchant_center.client import GoogleMerchantCenterClient

client = GoogleMerchantCenterClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_products()`
- `get_product()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/content/)
