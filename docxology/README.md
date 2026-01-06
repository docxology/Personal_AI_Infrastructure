# Docxology - PAI Sidecar System

**Your personal sidecar to the PAI system** - verification, setup, documentation, and personal content that evolves with your infrastructure.

---

## What is Docxology?

Docxology is your **sidecar folder** - a companion system to PAI that provides:

- **Verification & Health Checks** - Ensure your PAI system is working correctly
- **Setup Automation** - Auto-fix common configuration issues
- **Usage Documentation** - Complete guides for using your PAI system
- **Personal Content** - Your plans, notes, and customizations

Think of it as your **operational toolkit** that grows alongside your PAI installation.

---

## Quick Navigation

| Folder | Purpose | Quick Access |
|--------|---------|--------------|
| **[scripts/](scripts/)** | Verification and setup tools | `bun run docxology/scripts/setup-health-check.ts` |
| **[docs/](docs/)** | Usage guides and documentation | Start with [docs/START_HERE.md](docs/START_HERE.md) |
| **[personal/](personal/)** | Your personal content | See [personal/README.md](personal/README.md) |
| **[LIFE_PLAN_Q1_2026.md](LIFE_PLAN_Q1_2026.md)** | Quick access life plan | Your Q1-Q2 2026 plan |

---

## Quick Start

### 1. Verify Your System

```bash
# Quick health check
bun run docxology/scripts/setup-health-check.ts

# Full verification
bun run docxology/scripts/verify-installation.ts
```

### 2. Read the Guides

1. **[docs/START_HERE.md](docs/START_HERE.md)** - Quick start guide
2. **[docs/USAGE.md](docs/USAGE.md)** - Complete usage documentation

### 3. Fix Setup Issues

```bash
# Auto-fix common issues
bun run docxology/scripts/ensure-setup.ts --fix
```

---

## Folder Structure

```
docxology/
├── README.md                    # This file - main entry point
├── LIFE_PLAN_Q1_2026.md        # Quick access personal plan
├── scripts/                     # Executable tools
│   ├── README.md                # Scripts documentation
│   ├── verify-installation.ts   # Full system verification
│   ├── setup-health-check.ts    # Quick health check
│   ├── ensure-setup.ts          # Auto-fix setup issues
│   ├── test-hooks.ts            # Hook functional testing
│   └── quick-start.sh           # Interactive quick start
├── docs/                        # System documentation
│   ├── README.md                # Documentation index
│   ├── START_HERE.md            # Quick start guide
│   └── USAGE.md                 # Complete usage guide
└── personal/                    # Your personal content
    └── README.md                # Personal folder guide
```

---

## Scripts Overview

All scripts are in [scripts/](scripts/). See [scripts/README.md](scripts/README.md) for full documentation.

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `setup-health-check.ts` | Quick status check | Regular monitoring |
| `verify-installation.ts` | Full verification | After installation, troubleshooting |
| `ensure-setup.ts` | Auto-fix setup | When things break, after updates |
| `test-hooks.ts` | Test hooks | Verify hooks work correctly |
| `quick-start.sh` | Interactive guide | First-time setup |

---

## Documentation Overview

All guides are in [docs/](docs/). See [docs/README.md](docs/README.md) for the full index.

| Document | Purpose | Read When |
|----------|---------|-----------|
| `START_HERE.md` | Quick start | First time using PAI |
| `USAGE.md` | Complete guide | Learning the system |

---

## Personal Content

The [personal/](personal/) folder is for your custom content:

- Personal plans and goals
- Custom workflows
- Private notes
- User-specific configurations

See [personal/README.md](personal/README.md) for guidelines.

**Note:** `LIFE_PLAN_Q1_2026.md` stays in the root for quick access.

---

## Common Workflows

### After Installation

```bash
# 1. Verify everything works
bun run docxology/scripts/verify-installation.ts

# 2. Fix any issues
bun run docxology/scripts/ensure-setup.ts --fix

# 3. Test hooks
bun run docxology/scripts/test-hooks.ts
```

### Regular Maintenance

```bash
# Quick health check
bun run docxology/scripts/setup-health-check.ts
```

### Troubleshooting

```bash
# Full verification with details
bun run docxology/scripts/verify-installation.ts --verbose

# Test specific component
bun run docxology/scripts/test-hooks.ts --hook=security-validator
```

---

## Integration with PAI

Docxology scripts work with your PAI installation:

- **PAI_DIR** - Automatically detects `~/.claude` or uses `$PAI_DIR`
- **Skills** - Can verify and test all installed skills
- **Hooks** - Tests all hook functionality
- **History** - Validates history system capture
- **Tools** - Checks core PAI tools

---

## Evolution Strategy

As your PAI system evolves, docxology grows with it:

- **New scripts** go in `scripts/` (or subfolders like `scripts/monitoring/`)
- **New docs** go in `docs/` (or subfolders like `docs/troubleshooting/`)
- **Personal content** goes in `personal/` (organized by topic)

The structure scales naturally as your needs grow.

---

## Requirements

- **Bun runtime** - All scripts use Bun
- **PAI installation** - Scripts verify your PAI system
- **PAI_DIR** - Environment variable or defaults to `~/.claude`

---

## Exit Codes

All scripts follow standard exit codes:
- `0` - Success
- `1` - Failure/Issues found

This allows integration with automation tools, CI/CD, and monitoring systems.

---

## Getting Help

1. **Read the docs** - Start with [docs/START_HERE.md](docs/START_HERE.md)
2. **Run health check** - `bun run docxology/scripts/setup-health-check.ts`
3. **Full verification** - `bun run docxology/scripts/verify-installation.ts --verbose`
4. **Check logs** - `~/.claude/history/sessions/`

---

## Contributing

Docxology is part of your personal PAI infrastructure. Customize it for your needs:

- Add your own scripts to `scripts/`
- Create custom docs in `docs/`
- Organize personal content in `personal/`

The structure is designed to evolve with your system.

---

*Docxology - Your PAI sidecar, evolving with your infrastructure.*
