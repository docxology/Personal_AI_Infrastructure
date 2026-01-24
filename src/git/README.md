# Git Module

Local git operations and GitHub API client.

## Structure

```
git/
├── core/           # Local git CLI wrapper
│   ├── client.py   # GitClient class (14 methods)
│   └── utils.py    # Helper functions (4 functions)
├── github/         # GitHub REST API (@GithubBlanket)
│   ├── client.py   # GitHubClient class (10 methods)
│   └── auth.py     # Token management
└── __init__.py
```

## Local Git Operations

```python
from git import GitClient

client = GitClient("/path/to/repo")
```

| Method | Description |
|--------|-------------|
| `status(short=False)` | Repository status |
| `log(n=10, oneline=False)` | Commit history |
| `diff(staged=False)` | Show changes |
| `branch(list_all=False)` | List branches |
| `checkout(ref, create=False)` | Switch branches |
| `add(paths=None, all=False)` | Stage files |
| `commit(message, all=False)` | Create commit |
| `push(remote, branch, force)` | Push to remote |
| `pull(remote, branch)` | Pull from remote |
| `fetch(remote, prune=False)` | Fetch updates |
| `remote(verbose=False)` | List remotes |
| `rev_parse(ref)` | Resolve reference |

## GitHub API

```python
from git import GitHubClient

gh = GitHubClient()  # Uses @GithubBlanket by default
```

| Method | Description |
|--------|-------------|
| `get_authenticated_user()` | Current user info |
| `list_repos(user, type, sort)` | List repositories |
| `get_repo(owner, repo)` | Repository details |
| `create_repo(name, private)` | Create repository |
| `list_issues(owner, repo, state)` | List issues |
| `create_issue(owner, repo, title)` | Create issue |
| `close_issue(owner, repo, number)` | Close issue |
| `list_pull_requests(owner, repo)` | List PRs |
| `create_pull_request(...)` | Create PR |

## Authentication

- **Git**: System git configuration
- **GitHub**: `GITHUB_TOKEN` env or `~/.claude/github/token.json`

## Testing

```bash
pytest tests/git/ -v  # 65 tests
```

## Related

- [AGENTS.md](./AGENTS.md) - Agent guide
- [PAI.md](./PAI.md) - PAI integration
