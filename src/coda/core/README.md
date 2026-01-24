# Coda Core - README

Infrastructure module containing base client, errors, and utilities.

## Contents

| File | Purpose |
|------|---------|
| `base_client.py` | REST client with auth, pagination, rate limiting |
| `errors.py` | Exception classes (`CodaAPIError`, `CodaRateLimitError`) |
| `utils.py` | Token management and URL parsing utilities |

## Usage

```python
from coda.core import CodaClient, CodaAPIError, get_coda_token

# Direct access to base client
client = CodaClient()

# Error handling
try:
    docs = client.list_docs()
except CodaAPIError as e:
    print(f"Error: {e.status_code}")
```

## Related

- [../README.md](../README.md) - Main coda module
- [../clients/README.md](../clients/README.md) - Specialized clients
