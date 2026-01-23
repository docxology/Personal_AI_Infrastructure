# Packs - Agents Guide

## Overview

Packs are self-contained capability modules. Each pack provides a complete, tested capability that can be installed independently.

## Pack Categories

| Category | Prefix | Description |
|----------|--------|-------------|
| Infrastructure | `pai-*-system` | Core systems (hooks, voice, history) |
| Skills | `pai-*-skill` | Domain capabilities (agents, browser, research) |
| Servers | `pai-*-server` | Service components (observability) |

## Pack Structure

```
pai-{name}/
├── README.md      # Overview, architecture, what it solves
├── INSTALL.md     # Step-by-step installation
├── VERIFY.md      # Mandatory verification checklist
└── src/           # Actual code files
    ├── hooks/     # Hook implementations
    ├── tools/     # CLI utilities
    ├── skills/    # Skill definitions
    └── config/    # Configuration files
```

## Installation Flow

1. **Read README.md** - Understand what the pack does
2. **Follow INSTALL.md** - Execute installation steps
3. **Complete VERIFY.md** - Confirm all checks pass

## Critical Rules

1. **Copy complete files** - Never simplify or summarize code
2. **Preserve all lines** - Every line exists for a reason
3. **Complete VERIFY.md** - Installation isn't done until verification passes
4. **Check dependencies** - Install prerequisite packs first

## Installation Order

```
1. pai-hook-system       ← Foundation (no dependencies)
2. pai-core-install      ← Depends on hooks
3. pai-voice-system      ← Depends on hooks, core
4. pai-observability     ← Depends on hooks
5. pai-*-skill           ← Most depend only on core
```

## Validation

```bash
bun run Tools/validate-pack.ts                    # All packs
bun run Tools/validate-pack.ts pai-agents-skill   # Specific pack
```

## Creating Packs

Read `Tools/PAIPackTemplate.md` for the complete specification.

---

*Part of [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI)*
