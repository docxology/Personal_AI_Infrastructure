# Coda Core

Core functionality and base implementations for the Coda API client.

## Contents

- Base REST client with Bearer authentication
- Pagination handling
- Rate limit detection and retry logic
- Error classes (`CodaAPIError`, `CodaRateLimitError`)

## Usage

```python
from coda.base_client import CodaClient
```

This module is typically used indirectly via the specialized clients in `coda/`.
