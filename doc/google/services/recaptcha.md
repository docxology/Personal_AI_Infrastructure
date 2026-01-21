# reCAPTCHA

## Overview

Bot protection integration for Personal AI Infrastructure.

- **API**: `recaptchaenterprise`
- **Source**: [`src/google/recaptcha/client.py`](../../../src/google/recaptcha/client.py)
- **Test**: [`tests/test_google_recaptcha.py`](../../../tests/test_google_recaptcha.py)

## Quick Start

```python
from google.recaptcha.client import GoogleRecaptchaClient

client = GoogleRecaptchaClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_keys()`
- `create_assessment()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/recaptchaenterprise/)
