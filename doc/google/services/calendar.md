# Google Calendar

## Overview

Calendar and event management integration for Personal AI Infrastructure.

- **API**: `calendar`
- **Source**: [`src/google/calendar/client.py`](../../../src/google/calendar/client.py)
- **Test**: [`tests/test_google_calendar.py`](../../../tests/test_google_calendar.py)

## Quick Start

```python
from google.calendar.client import GoogleCalendarClient

client = GoogleCalendarClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_calendars()`
- `create_event()`
- `list_events()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/calendar/)
