# Google Services Documentation

This directory contains documentation for all Google service integrations in the Personal AI Infrastructure.

## Overview

The Google services module provides Python clients for **91 Google APIs**, built on the official `google-api-python-client`. All clients inherit from `UniversalGoogleClient` and provide:
- Automatic authentication via OAuth 2.0
- Domain-specific convenience methods
- Full access to underlying API via `client.service`

## Quick Start

```python
from google.youtube.client import GoogleYoutubeClient

# Initialize client (auto-authenticates)
client = GoogleYoutubeClient()

# Use convenience methods
results = client.search("active inference")

# Or access raw API
raw = client.service.videos().list(id="abc123", part="snippet").execute()
```

## Authentication

All clients share the same OAuth token stored in `google_services_token.json`. To re-authenticate:

```bash
python src/google/setup_auth.py
```

## Service Categories

| Category | Services |
|----------|----------|
| **Productivity** | [Calendar](services/calendar.md), [Gmail](services/gmail.md), [Drive](services/drive.md), [Tasks](services/tasks.md), [Docs](services/docs.md), [Sheets](services/sheets.md), [Slides](services/slides.md), [Keep](services/keep.md), [Forms](services/forms.md) |
| **Communication** | [Chat](services/chat.md), [Meet](services/meet.md), [Contacts](services/contacts.md), [Groups](services/groups.md) |
| **Media** | [YouTube](services/youtube.md), [Photos](services/photos.md), [Books](services/books.md), [Fonts](services/fonts.md) |
| **Cloud & AI** | [Cloud](services/cloud.md), [Vertex AI](services/vertex_ai.md), [Gemini](services/gemini.md) |
| **Analytics** | [Analytics](services/analytics.md), [Search Console](services/search_console.md), [Tag Manager](services/tag_manager.md) |
| **Business** | [Ads](services/ads.md), [AdSense](services/adsense.md), [Merchant Center](services/merchant_center.md) |

## Directory Structure

```
doc/google/
├── README.md              # This file
├── authentication.md      # Auth setup guide
├── architecture.md        # Technical architecture
└── services/              # Per-service docs
    ├── youtube.md
    ├── sheets.md
    └── ...
```

## Related Links

- [Source Code](../../src/google/)
- [Tests](../../tests/)
- [API Reference](https://developers.google.com/apis-explorer)
