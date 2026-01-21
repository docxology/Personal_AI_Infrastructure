# Docxology Scripts

Verification, setup, and testing tools for your PAI system.

---

## Scripts Overview

| Script | Purpose | Exit Code | Speed |
|--------|---------|-----------|-------|
| `setup-health-check.ts` | Quick status check | 0=OK, 1=Issues | Fast (~1s) |
| `verify-installation.ts` | Full verification | 0=Pass, 1=Fail | Medium (~5s) |
| `ensure-setup.ts` | Auto-fix setup | 0=OK, 1=Error | Fast (~2s) |
| `test-hooks.ts` | Test hooks | 0=Pass, 1=Fail | Fast (~3s) |
| `quick-start.sh` | Interactive guide | N/A | Interactive |

---

## setup-health-check.ts

**Quick health check for critical components**

Fast status check for regular monitoring. Checks only essential components.

### Usage

```bash
bun run docxology/scripts/setup-health-check.ts
```

### What It Checks

- PAI Directory exists
- Hooks Directory exists
- Skills Directory exists
- CORE Skill installed
- Security Validator installed
- Session Initializer installed
- Context Loader installed
- Hooks Configuration in settings.json
- Environment Config (.env file)
- History System directories
- Core Tools installed

### Output

```
🏥 PAI Health Check

Component Status:
──────────────────────────────────────────────────
✓ PAI Directory                  OK
✓ Hooks Directory                OK
✓ Skills Directory               OK
...

Healthy: 11 | Degraded: 0 | Unhealthy: 0

✅ System is fully operational
```

### Status Levels

- **healthy** - Component is working correctly
- **degraded** - Component partially working (non-critical)
- **unhealthy** - Component missing or broken (critical)

### Exit Codes

- `0` - System is operational (healthy or degraded only)
- `1` - Critical issues found (unhealthy components)

### When to Use

- Regular status checks
- Quick verification after changes
- Monitoring automation
- Pre-flight checks

---

## verify-installation.ts

**Comprehensive installation verification**

Full check of all PAI components, packs, and configurations. Runs functional tests.

### Usage

```bash
# Standard mode (summary only)
bun run docxology/scripts/verify-installation.ts

# Verbose mode (detailed output)
bun run docxology/scripts/verify-installation.ts --verbose
```

### What It Checks

**1. Environment & Dependencies**
- Bun runtime installed
- PAI_DIR configured
- .env file exists
- Environment variables set
- settings.json exists

**2. Hook System**
- All hook files installed
- Library files present
- Hook configuration valid

**3. Skill System**
- All skills installed
- Skill index generated
- Skill files valid

**4. History System**
- All history directories exist
- Execution categories present

**5. Tools**
- Core tools installed
- Tools executable

**6. Voice System**
- Voice server installed
- API keys configured

**7. Observability Server**
- Server app installed
- Client app installed
- Management script executable

**8. Functional Tests**
- Security validator (safe commands)
- Security validator (dangerous commands)
- Session initialization
- Core context loading

### Output

```
🔍 PAI Installation Verification

PAI_DIR: /Users/4d/.claude

📦 Environment & Dependencies
────────────────────────────────────────────────────────────
✓ Bun Runtime: Installed (v1.x.x)
✓ PAI Directory: Exists at /Users/4d/.claude
...

📊 Summary
────────────────────────────────────────────────────────────
✓ Passed:  54
✗ Failed:  0
⚠ Warnings: 0
   Total:   54

✅ All critical checks passed!
```

### Exit Codes

- `0` - All checks passed
- `1` - Some checks failed

### When to Use

- After installation
- When troubleshooting
- Before major changes
- System audits
- Pre-upgrade verification

---

## ensure-setup.ts

**Setup ensurer with auto-fix**

Ensures all required components exist and can automatically fix common issues.

### Usage

```bash
# Check only (no changes)
bun run docxology/scripts/ensure-setup.ts

# Auto-fix issues
bun run docxology/scripts/ensure-setup.ts --fix
```

### What It Ensures

**1. Directory Structure**
- PAI directory
- Hooks directory and lib
- Skills directory and CORE
- History directories (all categories)
- Tools directory
- Voice directory
- Observability directory

**2. Configuration Files**
- .env file with required variables
- settings.json hook configuration check

**3. Skill System**
- Skill index generation

**4. Scripts**
- Executable permissions on manage.sh

### Auto-Fix Capabilities

When run with `--fix`:
- Creates missing directories
- Creates .env with defaults if missing
- Adds missing environment variables to .env
- Generates skill index if missing
- Makes scripts executable

**Note:** Does NOT install pack files. Use pack installation process for that.

### Output

```
🔧 PAI Setup Ensurer

PAI_DIR: /Users/4d/.claude
Mode: Fix

📁 Directory Structure
──────────────────────────────────────────────────
✓ PAI Directory exists
✓ Hooks Directory exists
...

✅ Applied 3 fix(es)
```

### Exit Codes

- `0` - Success (fixes applied or no fixes needed)
- `1` - Error during fix operation

### When to Use

- After cloning repository
- When directories are missing
- After system updates
- Recovering from issues
- Initial setup

---

## test-hooks.ts

**Hook functional testing**

Tests all installed hooks with sample payloads to verify they work correctly.

### Usage

```bash
# Test all hooks
bun run docxology/scripts/test-hooks.ts

# Test specific hook
bun run docxology/scripts/test-hooks.ts --hook=security-validator
```

### What It Tests

**1. Security Validator**
- Allows safe commands (exit 0)
- Blocks dangerous commands (exit 2)

**2. Session Initialization**
- Creates session markers
- Sets tab titles
- Initializes directories

**3. Core Context Loading**
- Loads CORE skill
- Injects context

**4. Tab Title Updates**
- Extracts keywords
- Updates terminal titles

### Output

```
🧪 PAI Hook Testing

✓ security-validator: Allows safe command
✓ security-validator: Blocks dangerous command
✓ initialize-session: Initializes session
✓ load-core-context: Loads core context
✓ update-tab-titles: Updates tab title

──────────────────────────────────────────────────
Passed: 5 | Failed: 0

✅ All hook tests passed!
```

### Exit Codes

- `0` - All tests passed
- `1` - Some tests failed

### When to Use

- After hook installation
- When hooks behave unexpectedly
- Testing hook modifications
- Pre-deployment verification
- Debugging hook issues

---

## quick-start.sh

**Interactive quick start guide**

Interactive bash script that guides you through initial setup and testing.

### Usage

```bash
./docxology/scripts/quick-start.sh
```

### What It Does

1. Checks if Claude Code is running
2. Prompts you to restart if needed
3. Provides test commands
4. Optionally starts observability dashboard

### Output

Interactive prompts guide you through:
- Restarting Claude Code
- Testing your installation
- Starting observability (optional)

### When to Use

- First-time setup
- After major updates
- When onboarding
- Quick system check

---

## Usage Workflows

### After Installation

```bash
# 1. Ensure everything is set up
bun run docxology/scripts/ensure-setup.ts --fix

# 2. Verify full installation
bun run docxology/scripts/verify-installation.ts

# 3. Test hooks
bun run docxology/scripts/test-hooks.ts
```

### Regular Health Checks

```bash
# Quick status check (daily/weekly)
bun run docxology/scripts/setup-health-check.ts
```

### Troubleshooting

```bash
# Full verification with details
bun run docxology/scripts/verify-installation.ts --verbose

# Test specific component
bun run docxology/scripts/test-hooks.ts --hook=security-validator

# Auto-fix common issues
bun run docxology/scripts/ensure-setup.ts --fix
```

---

## Integration

### CI/CD Pipelines

```yaml
# Example GitHub Actions
- name: Verify PAI Installation
  run: bun run docxology/scripts/verify-installation.ts
```

### Pre-commit Hooks

```bash
#!/bin/bash
# .git/hooks/pre-commit
bun run docxology/scripts/setup-health-check.ts
```

### Automated Monitoring

```bash
# Cron job for daily health check
0 9 * * * cd /path/to/repo && bun run docxology/scripts/setup-health-check.ts
```

---

## Exit Codes Reference

All scripts follow standard Unix exit codes:

| Code | Meaning | Use Case |
|------|---------|----------|
| `0` | Success | All checks passed, no issues |
| `1` | Failure | Issues found, errors occurred |

This allows easy integration with:
- Shell conditionals: `if bun run ...; then ...`
- CI/CD systems: Fail builds on exit 1
- Monitoring: Alert on exit 1
- Automation: Chain scripts based on exit codes

---

## Requirements

- **Bun runtime** - All scripts require Bun
- **PAI_DIR** - Environment variable or defaults to `~/.claude`
- **PAI installation** - Scripts verify your PAI system

---

## Troubleshooting

### Scripts Not Found

```bash
# Ensure you're in repo root
cd /path/to/Personal_AI_Infrastructure

# Run with full path
bun run docxology/scripts/setup-health-check.ts
```

### Permission Denied

```bash
# Make scripts executable
chmod +x docxology/scripts/*.ts
chmod +x docxology/scripts/*.sh
```

### PAI_DIR Not Set

Scripts default to `~/.claude`. To use a custom location:

```bash
export PAI_DIR="$HOME/.config/pai"
bun run docxology/scripts/verify-installation.ts
```

---

## Adding New Scripts

When adding new scripts to docxology:

1. Place in `scripts/` directory
2. Use Bun runtime (`#!/usr/bin/env bun`)
3. Follow exit code standards (0=success, 1=failure)
4. Document in this README
5. Update root README.md if needed

---

*For complete PAI system documentation, see [../docs/](../docs/)*
