# Classroom - PAI Integration

## PAI Context

This service module provides PAI with access to Google Classroom functionality.

## Client Access

```python
from google.classroom.client import ClassroomClient
```

## Authentication

Uses PAI's centralized Google credentials at `~/.claude/google-calendar/`.

## Related

- [README.md](./README.md) - User documentation
- [AGENTS.md](./AGENTS.md) - Agent integration guide
- [../PAI.md](../PAI.md) - Google module overview
