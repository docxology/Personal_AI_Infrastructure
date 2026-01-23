# Google Services Integration

This directory contains the Python client implementations for various Google Services, bridging the Personal AI Infrastructure (PAI) with Google Workspace via Model Context Protocol (MCP) servers.

## Architecture

All clients inherit from a common `GoogleMCPClient` (in `base_client.py`) which manages the MCP server subprocess and JSON-RPC communication. For services without MCP support, use `UniversalGoogleClient` for direct REST API access.

## Available Services

- **Calendar** (`src/google/calendar`): Manage events and calendars.
- **Gmail** (`src/google/gmail`): List threads, read emails, create drafts.
- **Drive** (`src/google/drive`): Manage files and folders.
- **Tasks** (`src/google/tasks`): Manage task lists and tasks.

## Usage

Each service provides a client class (e.g., `GoogleCalendarClient`, `GoogleGmailClient`) that can be instantiated and used to call methods directly.

```python
from google.calendar import GoogleCalendarClient
from google.gmail import GoogleGmailClient

# Calendar
with GoogleCalendarClient() as client:
    events = client.list_events()

# Gmail
with GoogleGmailClient() as client:
    threads = client.list_threads()
```

## Testing

```bash
# Run Google service tests
pytest tests/google/ -v

# Run specific service test
pytest tests/google/test_google_gmail.py -v
```

## Agent Guide

For agent integration patterns, see [AGENTS.md](./AGENTS.md).

