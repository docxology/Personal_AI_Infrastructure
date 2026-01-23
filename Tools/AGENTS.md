# Tools - Agents Guide

## Overview

This directory contains utilities for building, validating, and maintaining PAI installations.

## Available Tools

| Tool | Purpose | Invocation |
|------|---------|------------|
| `CheckPAIState.md` | Diagnose PAI installation health | Read and execute |
| `PAIPackTemplate.md` | Create new packs | Read for spec |
| `PAIBundleTemplate.md` | Create new bundles | Read for spec |
| `InstallTemplate.md` | Wizard-style install flow | Read for template |
| `validate-pack.ts` | Validate pack completeness | `bun run Tools/validate-pack.ts` |

## When to Use

| User Request | Tool |
|--------------|------|
| "Check my PAI" | `CheckPAIState.md` |
| "Create a pack for X" | `PAIPackTemplate.md` |
| "Create a bundle for Y" | `PAIBundleTemplate.md` |
| "Validate my pack" | `validate-pack.ts` |
| "What's wrong with my setup?" | `CheckPAIState.md` |

## Tool Execution

### Diagnostic Tools (Markdown)
Read the complete file, then execute the steps described.

```
Read Tools/CheckPAIState.md and check my PAI state.
```

### Validation Tools (TypeScript)
Run directly with bun:

```bash
bun run Tools/validate-pack.ts                    # All packs
bun run Tools/validate-pack.ts pai-agents-skill   # Specific pack
bun run Tools/validate-pack.ts --changed-only     # CI mode
```

## Pack Validation

The `validate-pack.ts` script checks:
- Required files exist (README.md, INSTALL.md, VERIFY.md)
- SKILL.md workflow references are valid
- Dependencies are installed
- src/ directory structure is correct

## Creating Packs

1. Read `PAIPackTemplate.md` for complete specification
2. Create directory structure per template
3. Validate with `validate-pack.ts`
4. Test installation in clean environment

---

*Part of [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI)*
