# Google Slides

## Overview

Presentation creation and editing integration for Personal AI Infrastructure.

- **API**: `slides`
- **Source**: [`src/google/slides/client.py`](../../../src/google/slides/client.py)
- **Test**: [`tests/test_google_slides.py`](../../../tests/test_google_slides.py)

## Quick Start

```python
from google.slides.client import GoogleSlidesClient

client = GoogleSlidesClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `get_presentation()`
- `create_presentation()`
- `batch_update()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/slides/)
