# Docxology Scripts Testing

Comprehensive testing framework for validating all docxology scripts with generic sample data and scenarios.

---

## Overview

This testing framework ensures all docxology scripts work correctly with generic data that can be used by any user, not just the current installation. It provides:

- **Generic Test Fixtures** - Sample data that works for any user
- **Test Mode Support** - All scripts support `--test-mode` flag
- **Test Runner** - Automated test execution
- **Validation Suite** - Comprehensive validation of all components

---

## Quick Start

### Run All Tests

```bash
bun run docxology/scripts/tests/run-tests.ts
```

### Run Validation

```bash
bun run docxology/scripts/tests/validate-all.ts
```

### Test Individual Scripts

```bash
# Test mode examples
bun run docxology/scripts/setup-health-check.ts --test-mode
bun run docxology/scripts/ensure-setup.ts --test-mode --fix
bun run docxology/scripts/verify-installation.ts --test-mode
bun run docxology/scripts/test-hooks.ts --test-mode
./docxology/scripts/quick-start.sh --test-mode
```

---

## Test Structure

```
tests/
├── README.md                    # This file
├── run-tests.ts                 # Test runner
├── validate-all.ts               # Validation suite
├── fixtures/                     # Test fixtures
│   ├── generic.env               # Generic .env template
│   ├── generic-settings.json     # Generic settings.json
│   ├── sample-skill.md           # Sample skill file
│   └── sample-hook.ts            # Sample hook file
└── scenarios/                    # Test scenarios
    ├── ensure-setup-scenarios.md
    └── health-check-scenarios.md
```

---

## Test Fixtures

### generic.env

Generic environment configuration with placeholder values:
- `DA=TestUser` (generic user)
- `TIME_ZONE=UTC` (generic timezone)
- Placeholder API keys

### generic-settings.json

Generic Claude Code settings with hook configurations. Uses `${PAI_DIR}` placeholder that gets replaced during testing.

### sample-skill.md

Generic skill file for testing skill system functionality.

### sample-hook.ts

Minimal hook implementation for testing hook execution.

---

## Test Mode

All scripts support `--test-mode` flag which:

1. **Uses Test Directory**: Creates/uses `docxology/scripts/tests/test-pai/` instead of `~/.claude`
2. **Generic Defaults**: Uses "TestUser", "UTC", "TestApp" instead of hardcoded values
3. **Test Fixtures**: Loads fixtures from `tests/fixtures/` when available
4. **Isolated Testing**: Doesn't affect real PAI installation

### Example

```bash
# Normal mode (uses real PAI installation)
bun run docxology/scripts/ensure-setup.ts --fix

# Test mode (uses test directory)
bun run docxology/scripts/ensure-setup.ts --test-mode --fix
```

---

## Test Scenarios

### Ensure Setup Scenarios

1. **Fresh Installation** - No PAI directory exists
2. **Partial Installation** - Some components missing
3. **Complete Installation** - All components present
4. **Broken Configuration** - Invalid files
5. **Custom PAI_DIR** - Non-default location

### Health Check Scenarios

1. **Fully Healthy** - All components working
2. **Degraded** - Optional components missing
3. **Unhealthy** - Critical components missing
4. **Missing PAI_DIR** - Directory doesn't exist
5. **Partial Installation** - Mixed status

---

## Test Runner

The `run-tests.ts` script:

1. Sets up isolated test environment
2. Runs all scripts in test mode
3. Validates exit codes
4. Reports results
5. Cleans up test directory

### Usage

```bash
bun run docxology/scripts/tests/run-tests.ts
```

### Output

```
🚀 Docxology Script Test Runner

🔧 Setting up test environment...
✓ Test environment ready

🧪 Testing: setup-health-check.ts
   ✓ Passed (exit code: 0)

🧪 Testing: ensure-setup.ts
   ✓ Passed (exit code: 0)

...

📊 Test Summary
Total Tests: 5
✓ Passed: 5
✗ Failed: 0

✅ All tests passed!
```

---

## Validation Suite

The `validate-all.ts` script validates:

1. **Test Fixtures** - All required fixtures exist and are valid
2. **Script Test Mode** - All scripts support `--test-mode`
3. **Generic Values** - No hardcoded user-specific values
4. **Test Infrastructure** - Test runner and scenarios exist
5. **Content Validation** - Fixtures contain generic values

### Usage

```bash
bun run docxology/scripts/tests/validate-all.ts
```

### Output

```
🔍 Docxology Scripts Validation Suite

📦 Validating Test Fixtures...
✓ generic.env: Found
✓ generic.env (content): Contains generic values
✓ generic-settings.json: Found
✓ generic-settings.json (valid JSON): Valid JSON with hooks

📜 Validating Script Test Mode Support...
✓ ensure-setup.ts (--test-mode): Supports --test-mode
✓ ensure-setup.ts (generic): Uses generic defaults

...

📊 Validation Summary
Total Validations: 20
✓ Passed: 20
✗ Failed: 0

✅ All validations passed!
```

---

## Generic User Profile

For testing purposes, scripts use:

- **Name**: "Test User"
- **DA**: "TestUser"
- **Timezone**: "UTC" (not location-specific)
- **PAI_DIR**: Temporary test directory

This ensures scripts work for any user without hardcoded assumptions.

---

## Adding New Tests

### 1. Add Test Fixture

Create fixture in `fixtures/` directory:

```bash
# Example: new-fixture.json
{
  "test": "data"
}
```

### 2. Update Test Runner

Add test case to `run-tests.ts`:

```typescript
const newTest = runTest('new-script.ts', ['--test-mode']);
results.push(newTest);
```

### 3. Add Validation

Add validation check to `validate-all.ts`:

```typescript
validateFixture('new-fixture.json', exists, exists ? 'Found' : 'Missing');
```

---

## Best Practices

1. **Always Use Test Mode** - Test scripts with `--test-mode` before committing
2. **Generic Values** - Never hardcode user-specific values
3. **Isolated Testing** - Test mode uses separate directory
4. **Clean Fixtures** - Keep fixtures generic and reusable
5. **Document Scenarios** - Document test scenarios in `scenarios/`

---

## Troubleshooting

### Tests Fail

1. Check test directory exists: `docxology/scripts/tests/test-pai/`
2. Verify fixtures are present: `ls docxology/scripts/tests/fixtures/`
3. Run validation: `bun run docxology/scripts/tests/validate-all.ts`

### Script Doesn't Support Test Mode

1. Check script has `TEST_MODE` variable
2. Verify script uses generic defaults in test mode
3. Update script to support `--test-mode` flag

### Fixtures Not Found

1. Verify fixtures exist in `tests/fixtures/`
2. Check file paths in scripts
3. Ensure fixtures are committed to repository

---

## Integration

### CI/CD

Add to GitHub Actions:

```yaml
- name: Test Docxology Scripts
  run: bun run docxology/scripts/tests/run-tests.ts

- name: Validate Scripts
  run: bun run docxology/scripts/tests/validate-all.ts
```

### Pre-commit

Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
bun run docxology/scripts/tests/validate-all.ts
```

---

*Testing ensures docxology scripts work correctly for all users with generic data.*
