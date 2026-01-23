# Tests - Agents Guide

## Overview

This directory contains pytest test suites for PAI's API clients.

## Test Organization

| Directory | Tests For | Count |
|-----------|-----------|-------|
| `google/` | Google Workspace API clients | ~100 |
| `coda/` | Coda API client | ~20 |

## Running Tests

```bash
# Full suite
pytest tests/

# By service
pytest tests/google/
pytest tests/coda/

# Single file
pytest tests/google/test_gmail.py

# With coverage
pytest tests/ --cov=src/
```

## Test Patterns

### Client Tests
```python
def test_list_messages():
    client = GmailClient()
    result = client.list_messages(max_results=5)
    assert isinstance(result, list)
```

### Error Handling
```python
def test_invalid_id():
    client = CalendarClient()
    with pytest.raises(Exception):
        client.get_event("nonexistent")
```

## Expected Results

| Status | Meaning |
|--------|---------|
| `passed` | Test succeeded |
| `failed` | Test failed (bug or regression) |
| `skipped` | Missing credentials or prerequisites |

## Adding Tests

1. Create `tests/{service}/test_{feature}.py`
2. Import the client from `src/`
3. Write `test_*` functions
4. Run with `pytest tests/{service}/test_{feature}.py`

## Known Issues

- Some tests require specific API permissions
- OAuth token expiration may cause transient failures
- Rate limiting may affect test reliability

---

*Part of [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI)*
