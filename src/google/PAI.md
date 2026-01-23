# Google Services - PAI Integration

## PAI Context

The Google module provides PAI with access to 90+ Google Workspace and Cloud services via MCP (Model Context Protocol) or direct REST APIs.

## PAI Use Cases

| Use Case | Service | Client Pattern |
|----------|---------|----------------|
| Calendar management | Calendar | `GoogleMCPClient` |
| Email operations | Gmail | `GoogleMCPClient` |
| File storage | Drive | `GoogleMCPClient` |
| Task management | Tasks | `GoogleMCPClient` |
| Video platform | YouTube | `UniversalGoogleClient` |

## Client Patterns

1. **MCP Clients** (`GoogleMCPClient`) - For services with MCP server support
2. **REST Clients** (`UniversalGoogleClient`) - Direct API access

## Authentication

Centralized at `~/.claude/google-calendar/`:
- `credentials.json` - OAuth client config
- `token.json` - Current OAuth token
- `google_services_token.json` - Expanded scopes token

## Related

- [README.md](./README.md) - User documentation
- [AGENTS.md](./AGENTS.md) - Agent integration guide
