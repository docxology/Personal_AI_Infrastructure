# Tests

This directory contains the pytest test suites for PAI API clients.

## Structure

```
tests/
├── __init__.py
├── google/           # Google API client tests
│   ├── test_gmail.py
│   ├── test_calendar.py
│   ├── test_drive.py
│   └── ...
└── coda/             # Coda API client tests
    ├── test_docs.py
    ├── test_tables.py
    └── ...
```

## Running Tests

```bash
# All tests
pytest tests/

# Specific directory
pytest tests/google/
pytest tests/coda/

# Specific file
pytest tests/google/test_gmail.py

# With verbose output
pytest tests/ -v

# Stop on first failure
pytest tests/ -x
```

## Test Coverage

| Directory | Coverage | Notes |
|-----------|----------|-------|
| `google/` | 90+ services | MCP-proxied clients |
| `coda/` | Full | Docs, tables, permissions |

## Authentication

Tests require valid API credentials:
- Google: OAuth tokens at `~/.claude/google-calendar/`
- Coda: API key in environment

Some tests may skip if credentials are missing.

## Writing Tests

Tests follow pytest conventions:
- Test files: `test_*.py`
- Test functions: `test_*`
- Use fixtures for client setup

---

*Part of [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI)*
