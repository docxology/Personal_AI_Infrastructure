# Triple Mirror - Agent Guide

## Purpose

Triple-mirror PAI knowledge bases to ensure redundancy and accessibility across:
- **Coda** - Document pages for structured access
- **GitHub** - Version-controlled repository
- **Google Drive** - Cloud files for device sync

## Quick Usage

```python
from mirror import MirrorConfig, MirrorSync

config = MirrorConfig(source_dir=Path("~/.pai/knowledge"))
sync = MirrorSync(config)
results = sync.sync_all()

for target, result in results.items():
    print(f"{target}: {'✓' if result.success else '✗'}")
```

## Entry Points

| Task | Method |
|------|--------|
| Sync all targets | `MirrorSync.sync_all()` |
| Sync Coda only | `MirrorSync.sync_coda()` |
| Sync GitHub only | `MirrorSync.sync_github()` |
| Sync Drive only | `MirrorSync.sync_drive()` |
| Get status | `MirrorSync.get_status()` |

## Default Configuration

- **Source**: `~/.pai/knowledge/`
- **Coda Doc**: `NDxZHneeIw` (PAI Controller)
- **GitHub**: `GithubBlanket/pai-knowledge`
- **Drive**: Root or specified folder ID
