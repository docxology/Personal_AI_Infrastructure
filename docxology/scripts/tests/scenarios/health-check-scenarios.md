# Health Check Test Scenarios

## Scenario 1: Fully Healthy System
- **Setup**: All components present and working
- **Expected**: All 11 components show "healthy"
- **Exit Code**: 0

## Scenario 2: Degraded System
- **Setup**: Some optional components missing
- **Expected**: Shows degraded status for optional components
- **Exit Code**: 0 (non-critical)

## Scenario 3: Unhealthy System
- **Setup**: Critical components missing
- **Expected**: Shows unhealthy status
- **Exit Code**: 1

## Scenario 4: Missing PAI Directory
- **Setup**: PAI_DIR doesn't exist
- **Expected**: Reports unhealthy
- **Exit Code**: 1

## Scenario 5: Partial Installation
- **Setup**: Some hooks missing, some present
- **Expected**: Mixed healthy/unhealthy status
- **Exit Code**: 1 (if critical missing)
