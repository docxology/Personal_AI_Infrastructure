# Play Games

## Overview

Gaming services integration for Personal AI Infrastructure.

- **API**: `games`
- **Source**: [`src/google/play_games/client.py`](../../../src/google/play_games/client.py)
- **Test**: [`tests/test_google_play_games.py`](../../../tests/test_google_play_games.py)

## Quick Start

```python
from google.play_games.client import GooglePlayGamesClient

client = GooglePlayGamesClient()

if client.is_ready():
    # Use convenience methods or raw API
    result = client.service.<resource>().<method>().execute()
```

## Methods

- `list_achievements()`
- `list_leaderboards()`

## Authentication

Requires OAuth token in `google_services_token.json`. See [Authentication Guide](../authentication.md).

## API Reference

- [Official Documentation](https://developers.google.com/apis-explorer/#p/games/)
