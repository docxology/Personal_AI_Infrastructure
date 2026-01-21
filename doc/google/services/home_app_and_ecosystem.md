# Google Home App And Ecosystem

## Overview

Home App And Ecosystem integration integration for Personal AI Infrastructure.

- **API**: `home_app_and_ecosystem`
- **Source**: [`src/google/home_app_and_ecosystem/client.py`](../../../src/google/home_app_and_ecosystem/client.py)
- **Test**: [`tests/test_google_home_app_and_ecosystem.py`](../../../tests/test_google_home_app_and_ecosystem.py)

## Quick Start

```python
from google.home_app_and_ecosystem.client import GoogleHomeAppAndEcosystemClient

client = GoogleHomeAppAndEcosystemClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/home_app_and_ecosystem/)
