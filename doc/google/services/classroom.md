# Google Classroom

## Overview

Education platform integration for Personal AI Infrastructure.

- **API**: `classroom`
- **Source**: [`src/google/classroom/client.py`](../../../src/google/classroom/client.py)
- **Test**: [`tests/test_google_classroom.py`](../../../tests/test_google_classroom.py)

## Quick Start

```python
from google.classroom.client import GoogleClassroomClient

client = GoogleClassroomClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_courses()`
- `get_course()`
- `list_students()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/classroom/)
