# Releases - Agents Guide

## Overview

Releases are versioned, complete distributions of PAI. Each release is a self-contained `.claude/` directory that can be installed directly.

## Available Releases

| Version | Status | Description |
|---------|--------|-------------|
| `v2.3/` | Current | Complete PAI with continuous learning |

## Release Structure

```
v{version}/
├── README.md           # Release notes
├── INSTALL.md          # Installation instructions
├── .claude/            # Complete PAI directory
│   ├── settings.json   # Configuration
│   ├── hooks/          # Hook implementations
│   ├── skills/         # All skills
│   ├── MEMORY/         # Memory system
│   └── ...
└── icons/              # Release artwork
```

## Installation

Releases can be installed by copying the `.claude/` directory:

```bash
# Backup existing
mv ~/.claude ~/.claude.backup

# Install release
cp -r Releases/v2.3/.claude ~/
```

## Releases vs Packs

| Use Releases When | Use Packs When |
|-------------------|----------------|
| Starting fresh | Adding to existing setup |
| Want known-good version | Want latest changes |
| Need complete system | Need specific capability |

## Version Policy

- Major versions (v3.0): Breaking changes
- Minor versions (v2.3): New features, backward compatible
- Patch versions (v2.3.1): Bug fixes only

## Release Contents

Each release includes:
- All infrastructure packs pre-installed
- All skill packs pre-installed
- Default configuration
- Empty MEMORY/ ready for use
- Complete hooks system

---

*Part of [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI)*
