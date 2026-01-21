# Google Wallet

## Overview

Digital wallet integration for Personal AI Infrastructure.

- **API**: `walletobjects`
- **Source**: [`src/google/wallet/client.py`](../../../src/google/wallet/client.py)
- **Test**: [`tests/test_google_wallet.py`](../../../tests/test_google_wallet.py)

## Quick Start

```python
from google.wallet.client import GoogleWalletClient

client = GoogleWalletClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_loyalty_classes()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/walletobjects/)
