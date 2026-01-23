# PAI Repository - Agents Guide

## Overview

This is the **Personal AI Infrastructure (PAI)** repository. PAI is a modular system for building personalized AI assistants that magnify human capabilities.

## Repository Structure

```
/
├── Packs/              # Individual capability modules (skills, hooks, tools)
├── Bundles/            # Curated collections of packs
├── Releases/           # Versioned complete distributions
├── Tools/              # Utilities for pack/bundle creation and validation
├── src/                # Python API clients (Google, Coda)
├── tests/              # pytest test suites
└── docxology/          # Documentation sidecar (symlink)
```

## Key Entry Points

| Task | Entry Point |
|------|-------------|
| Install PAI | `Bundles/Official/` or `Releases/v2.3/` |
| Create a pack | `Tools/PAIPackTemplate.md` |
| Create a bundle | `Tools/PAIBundleTemplate.md` |
| Check PAI state | `Tools/CheckPAIState.md` |
| Validate packs | `bun run Tools/validate-pack.ts` |
| Run tests | `pytest tests/` |

## Architecture

PAI uses a **Bundles → Packs → Contents** hierarchy:

- **Bundles** are curated collections for specific use cases
- **Packs** are self-contained capabilities (skills, hooks, tools)
- **Contents** are the actual code files within packs

## Naming Conventions

| Pattern | Meaning |
|---------|---------|
| `pai-*-skill` | Skill pack (provides a skill capability) |
| `pai-*-system` | Infrastructure pack (hooks, voice, history) |
| `pai-*-server` | Server component (observability dashboard) |
| `TitleCase/` | System directory (public) |
| `_ALLCAPS/` | Personal directory (never syncs to public) |

## Common Operations

### Running Tests
```bash
pytest tests/                    # All tests
pytest tests/google/            # Google API client tests
pytest tests/coda/              # Coda API client tests
```

### Validating Packs
```bash
bun run Tools/validate-pack.ts                    # All packs
bun run Tools/validate-pack.ts pai-agents-skill   # Specific pack
```

### Pack Installation
Read the pack's `README.md`, follow `INSTALL.md`, verify with `VERIFY.md`.

## Important Rules

1. **Never simplify pack code** - Copy complete implementations verbatim
2. **Always complete VERIFY.md** - Installation isn't done until verification passes
3. **API clients use MCP** - Google/Coda clients proxy through MCP servers
4. **Two-tier config** - USER overrides SYSTEM for all configurable components

---

*Part of [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI)*
