# Git Core - README

Local git CLI wrapper.

## Contents

| File | Purpose |
|------|---------|
| `client.py` | GitClient class wrapping git CLI |
| `utils.py` | Helper functions |

## Usage

```python
from git.core import GitClient, is_git_repo

if is_git_repo():
    client = GitClient()
    print(client.status())
```
