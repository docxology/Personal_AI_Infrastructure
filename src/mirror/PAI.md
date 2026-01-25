# Triple Mirror - PAI Integration

## PAI Context

Triple mirroring ensures PAI knowledge bases are replicated across three backends for redundancy, accessibility, and version control.

## Default Configuration

| Setting | Value |
|---------|-------|
| Source | `~/.pai/knowledge/` |
| Coda | Doc ID: `NDxZHneeIw` |
| GitHub | `GithubBlanket/pai-knowledge` |
| Drive | PAI Knowledge folder |

## Usage

```python
from mirror import MirrorSync, get_default_config

config = get_default_config()
sync = MirrorSync(config)
sync.sync_all()
```

## Test Verification

```bash
pytest tests/mirror/test_mirror.py -v
```
