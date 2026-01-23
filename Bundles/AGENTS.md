# Bundles - Agents Guide

## Overview

Bundles are curated collections of packs designed to work together as cohesive systems.

## Available Bundles

| Bundle | Description | Packs |
|--------|-------------|-------|
| `Official/` | Complete PAI system | All 23 packs |

## Bundle Structure

```
{bundle-name}/
├── README.md           # Overview and capabilities
├── INSTALL.md          # Installation wizard
├── VERIFY.md           # Bundle-level verification
└── icons/              # Bundle artwork
```

## Installation Flow

1. **Read README.md** - Understand what the bundle provides
2. **Follow INSTALL.md** - Guided wizard with user questions
3. **Complete VERIFY.md** - Confirm all packs installed correctly

## Bundle vs Individual Packs

| Use Bundle When | Use Individual Packs When |
|-----------------|---------------------------|
| Starting fresh | Adding specific capability |
| Want complete system | Have existing setup |
| Prefer guided setup | Know what you need |

## Creating Bundles

Read `Tools/PAIBundleTemplate.md` for the complete specification.

Key requirements:
- Clear use case definition
- Documented pack interactions
- Installation order with dependencies
- Bundle-level verification

## Bundle Tiers

Bundles can define tiers for progressive installation:

| Tier | Purpose |
|------|---------|
| Starter | Minimum viable setup |
| Intermediate | Common additions |
| Advanced | Full capabilities |
| Complete | Everything included |

---

*Part of [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI)*
