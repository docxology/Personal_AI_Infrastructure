# Git Module - Agent Guide

## Purpose

Local git operations and GitHub API access for PAI.

## Module Structure

- **git.core** - Local git CLI wrapper (14 methods)
- **git.github** - GitHub REST API (10 methods)

## Key Entry Points

| Task | Client | Method |
|------|--------|--------|
| Check status | `GitClient` | `status()` |
| View log | `GitClient` | `log()` |
| Create commit | `GitClient` | `commit()` |
| Push changes | `GitClient` | `push()` |
| List repos | `GitHubClient` | `list_repos()` |
| Create issue | `GitHubClient` | `create_issue()` |
| Create PR | `GitHubClient` | `create_pull_request()` |

## Patterns

```python
from git import GitClient, GitHubClient

# Local git
git = GitClient()
git.status()
git.log(n=5, oneline=True)
git.commit("fix: bug", all=True)
git.push()

# GitHub API
gh = GitHubClient()
gh.list_repos()
gh.create_issue("owner", "repo", "Title", body="Description")
```

## Default GitHub Account

@GithubBlanket (fristonblanket@gmail.com)

## Testing

```bash
pytest tests/git/ -v  # 65 tests
```

## Related

- [core/](./core/) - Local operations
- [github/](./github/) - GitHub API
