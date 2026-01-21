# Architecture

## Overview

The Google services module uses a three-tier architecture:

```
┌─────────────────────────────────────────────┐
│           Application Layer                  │
│  (Your code using Google service clients)    │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│        Service Client Layer                  │
│  (GoogleYoutubeClient, GoogleSheetsClient)   │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│       UniversalGoogleClient                  │
│  (Authentication, API discovery)             │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│      google-api-python-client               │
│  (Official Google API library)              │
└─────────────────────────────────────────────┘
```

## Core Components

### UniversalGoogleClient (`src/google/universal_client.py`)

The base class for all service clients. Handles:
- Loading OAuth credentials from `google_services_token.json`
- Building the API service object via `googleapiclient.discovery.build`
- Providing `is_ready()` status check

```python
class UniversalGoogleClient:
    def __init__(self, service_name: str, version: str):
        self.service_name = service_name
        self.version = version
        self.credentials = self._load_credentials()
        self.service = self._build_service()
```

### Service Clients (`src/google/<service>/client.py`)

Each service has its own client class that:
1. Inherits from `UniversalGoogleClient`
2. Configures the correct API name and version
3. Provides domain-specific convenience methods

Example:
```python
class GoogleYoutubeClient(UniversalGoogleClient):
    def __init__(self):
        super().__init__(service_name='youtube', version='v3')
    
    def search(self, query: str, max_results: int = 10):
        return self.service.search().list(q=query, part='snippet', maxResults=max_results).execute()
```

### Utilities (`src/google/utils.py`)

Shared utilities including:
- `get_google_credentials_object()`: Loads OAuth token as Credentials object
- `get_google_services_token_path()`: Returns path to token file
- `load_google_credentials_env()`: Loads credentials for MCP servers

## Data Flow

```
1. Client Initialization
   └── UniversalGoogleClient.__init__()
       ├── _load_credentials() → Read google_services_token.json
       └── _build_service() → googleapiclient.discovery.build()

2. API Call
   └── client.search("query")
       └── self.service.search().list(...).execute()
           └── HTTP request to Google API

3. Response
   └── JSON response parsed and returned
```

## Directory Structure

```
src/google/
├── __init__.py
├── universal_client.py      # Base client class
├── utils.py                 # Shared utilities
├── setup_auth.py            # OAuth flow
├── base_client.py           # Legacy MCP client
└── <service>/               # Service modules (91 total)
    ├── __init__.py
    ├── client.py            # Service client
    ├── README.md            # Service overview
    ├── AGENTS.md            # Agent capabilities
    └── SPEC.md              # Technical spec
```

## Testing

Each service has a corresponding test file:
- Location: `tests/test_google_<service>.py`
- Tests: Import, Instantiation, `is_ready()` check
- Run: `pytest tests/test_google_*.py`
