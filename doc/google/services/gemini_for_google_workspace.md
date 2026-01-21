# Google Gemini For Google Workspace

## Overview

Gemini For Google Workspace integration integration for Personal AI Infrastructure.

- **API**: `gemini_for_google_workspace`
- **Source**: [`src/google/gemini_for_google_workspace/client.py`](../../../src/google/gemini_for_google_workspace/client.py)
- **Test**: [`tests/test_google_gemini_for_google_workspace.py`](../../../tests/test_google_gemini_for_google_workspace.py)

## Quick Start

```python
from google.gemini_for_google_workspace.client import GoogleGeminiForGoogleWorkspaceClient

client = GoogleGeminiForGoogleWorkspaceClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- Access via `client.service`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/gemini_for_google_workspace/)
