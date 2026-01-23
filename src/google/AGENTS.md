# Google Services Agents Guide

## Overview
This directory allows your AI agents to interact with Google Workspace services.

## Capabilities
- **Calendar**: Schedule, update, and delete events.
- **Gmail**: Read emails, search threads, create drafts.
- **Drive**: List, create, upload, and delete files/folders.
- **Tasks**: manage to-do lists.

## Integration Pattern
When adding new features or debugging:
1. **Check `base_client.py`**: This handles the core MCP connection.
2. **Check specific service client**: Ensure it calls the correct MCP tool name.
3. **Run Tests**: Always run `tests/test_google_{service}.py` to verify.

## Authentication
All services rely on shared credentials at `~/.claude/google-calendar/` directory including `credentials.json`, `token.json`, and `google_services_token.json`. See `setup_auth.py` for OAuth flow.
