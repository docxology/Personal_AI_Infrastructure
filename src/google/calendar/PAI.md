# Calendar - PAI Integration

## PAI Context

This service module provides PAI with access to Google Calendar functionality.

## Client Access

```python
from google.calendar.client import CalendarClient
```

## Authentication

Uses PAI's centralized Google credentials at `~/.claude/google-calendar/`.

## Related

- [README.md](./README.md) - User documentation
- [AGENTS.md](./AGENTS.md) - Agent integration guide
- [../PAI.md](../PAI.md) - Google module overview
