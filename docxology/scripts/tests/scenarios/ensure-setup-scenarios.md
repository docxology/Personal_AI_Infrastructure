# Ensure Setup Test Scenarios

## Scenario 1: Fresh Installation
- **Setup**: No PAI directory exists
- **Expected**: Creates all required directories and files
- **Test**: Run with `--test-mode --fix`

## Scenario 2: Partial Installation
- **Setup**: PAI directory exists but missing some components
- **Expected**: Creates missing directories and files
- **Test**: Run with `--test-mode --fix`

## Scenario 3: Complete Installation
- **Setup**: All components present
- **Expected**: Reports all components exist, no fixes needed
- **Test**: Run with `--test-mode`

## Scenario 4: Broken Configuration
- **Setup**: Invalid .env or settings.json
- **Expected**: Reports issues, fixes if `--fix` provided
- **Test**: Run with `--test-mode --fix`

## Scenario 5: Custom PAI_DIR
- **Setup**: Non-default PAI_DIR location
- **Expected**: Works correctly with custom location
- **Test**: Run with `--test-mode PAI_DIR=/tmp/test-pai`
