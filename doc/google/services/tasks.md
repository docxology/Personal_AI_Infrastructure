# Google Tasks

## Overview

Task management integration for Personal AI Infrastructure.

- **API**: `tasks`
- **Source**: [`src/google/tasks/client.py`](../../../src/google/tasks/client.py)
- **Test**: [`tests/test_google_tasks.py`](../../../tests/test_google_tasks.py)

## Quick Start

```python
from google.tasks.client import GoogleTasksClient

client = GoogleTasksClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_tasklists()`
- `list_tasks()`
- `create_task()`
- `complete_task()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/tasks/)
