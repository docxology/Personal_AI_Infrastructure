# Shadow Module - PAI Integration

## PAI Context

The Shadow Sync module enables **local-first discovery** and integrates with PAI email workflows for daily/weekly digests.

## Default Configuration

| Setting | Value |
|---------|-------|
| Shadow Directory | `~/.pai/coda_shadows/` |
| PAI Doc Controller | `NDxZHneeIw` |
| Sync Interval | 24 hours |

## Email Integration

### Daily Digest

```python
from coda.shadow import sync_pai_shadows, send_shadow_digest_email

sync_pai_shadows()
send_shadow_digest_email("user@example.com", digest_type="daily")
```

### Weekly Report

```python
send_shadow_digest_email("user@example.com", digest_type="weekly")
```

## Utility Functions

| Function | Purpose |
|----------|---------|
| `sync_pai_shadows()` | Sync PAI Document Controller |
| `generate_shadow_summary()` | Markdown summary for reports |
| `generate_daily_digest_content()` | HTML for daily emails |
| `generate_weekly_report_content()` | HTML for weekly emails |
| `send_shadow_digest_email()` | Send digest via Gmail |
| `quick_search()` | Search default shadow dir |
| `get_shadow_stats()` | Index statistics |

## Test Verification

```bash
pytest tests/coda/test_shadow_sync.py tests/coda/test_pai_utils.py -v
# Expected: 26 passed
```
