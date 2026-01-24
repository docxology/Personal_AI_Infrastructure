# GitHub - README

GitHub REST API client.

## Default Account
@GithubBlanket (fristonblanket@gmail.com)

## Contents

| File | Purpose |
|------|---------|
| `client.py` | GitHubClient class |
| `auth.py` | Token management |

## Usage

```python
from git.github import GitHubClient

client = GitHubClient()
repos = client.list_repos()
```
