# Triple Mirror Module

Triple-mirror PAI knowledge bases to Coda, GitHub, and Google Drive.

## Quick Start

```python
from mirror import MirrorConfig, MirrorSync

config = MirrorConfig(
    source_dir=Path("~/.pai/knowledge"),
    coda_doc_id="NDxZHneeIw",
    github_repo="GithubBlanket/pai-knowledge",
)

sync = MirrorSync(config)
results = sync.sync_all()
```

## Targets

| Target | Client | Storage |
|--------|--------|---------|
| Coda | `CodaPagesClient` | Document pages |
| GitHub | `GitClient` + `GitHubClient` | Repository |
| Drive | `GoogleDriveClient` | Cloud folder |

## Components

| File | Purpose |
|------|---------|
| `mirror_config.py` | Configuration dataclass |
| `mirror_coda.py` | Coda page mirror |
| `mirror_github.py` | GitHub repo mirror |
| `mirror_drive.py` | Drive folder mirror |
| `mirror_sync.py` | Unified orchestrator |

## Individual Syncs

```python
# Sync to specific target only
sync.sync_coda()
sync.sync_github()
sync.sync_drive()
```

## Testing

```bash
pytest tests/mirror/ -v
```
