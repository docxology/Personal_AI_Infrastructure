# Git Module - PAI Integration

## PAI Context

Git operations and GitHub API for PAI's version control and repository management.

## Default GitHub Account

@GithubBlanket (fristonblanket@gmail.com)

## Key Operations

| Use Case | Client | Method |
|----------|--------|--------|
| Check status | `GitClient` | `status()` |
| View history | `GitClient` | `log()` |
| Commit changes | `GitClient` | `commit()` |
| Push to remote | `GitClient` | `push()` |
| List repos | `GitHubClient` | `list_repos()` |
| Create issue | `GitHubClient` | `create_issue()` |
| Create PR | `GitHubClient` | `create_pull_request()` |

## Authentication

- **GitHub**: `~/.claude/github/token.json` or `GITHUB_TOKEN` env

## Tests

65 tests across 7 files in `tests/git/`

## Related

- [README.md](./README.md) - Documentation
- [AGENTS.md](./AGENTS.md) - Agent guide
