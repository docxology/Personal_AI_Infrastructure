# Authentication Guide

## Overview

All Google service clients share a centralized OAuth 2.0 authentication system. Credentials are stored in `google_services_token.json` and automatically loaded by the `UniversalGoogleClient`.

## Initial Setup

### 1. Create OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select a project
3. Navigate to **APIs & Services** > **Credentials**
4. Click **Create Credentials** > **OAuth client ID**
5. Select **Desktop application**
6. Download the JSON file as `credentials.json`
7. Place it in the project root

### 2. Run Authentication

```bash
python src/google/setup_auth.py
```

This will:
1. Open a browser for OAuth consent
2. Save the token to `google_services_token.json`
3. Configure the token for all services

### 3. Enable APIs

Enable the APIs you need in Google Cloud Console:
- [YouTube Data API](https://console.cloud.google.com/apis/library/youtube.googleapis.com)
- [Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com)
- [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com)
- etc.

## Token Structure

The `google_services_token.json` contains:

```json
{
  "token": "ya29.a0...",
  "refresh_token": "1//0...",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "xxx.apps.googleusercontent.com",
  "client_secret": "xxx",
  "scopes": ["https://www.googleapis.com/auth/..."]
}
```

## Scopes

Default scopes include:
- `https://www.googleapis.com/auth/gmail.modify`
- `https://www.googleapis.com/auth/drive`
- `https://www.googleapis.com/auth/calendar`
- `https://www.googleapis.com/auth/tasks`

To add more scopes, edit `src/google/setup_auth.py` and re-run authentication.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Token expired | Re-run `setup_auth.py` |
| API not enabled | Enable in GCP Console |
| Insufficient permissions | Add required scopes and re-authenticate |
| `is_ready() = False` | Check API is enabled and token has required scopes |

## Security

- Never commit `credentials.json` or `google_services_token.json` to version control
- Both files are listed in `.gitignore`
- Use environment variables for production deployments
