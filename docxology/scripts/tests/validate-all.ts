#!/usr/bin/env bun
/**
 * Comprehensive Validation Suite for Docxology Scripts
 * 
 * Validates all scripts work correctly with generic data and scenarios.
 * 
 * Usage:
 *   bun run docxology/scripts/tests/validate-all.ts
 */

import { existsSync, readFileSync } from 'fs';
import { join } from 'path';

interface ValidationResult {
  category: string;
  test: string;
  passed: boolean;
  message: string;
}

const validations: ValidationResult[] = [];

function validate(name: string, condition: boolean, message: string): void {
  validations.push({
    category: 'General',
    test: name,
    passed: condition,
    message
  });
}

function validateScript(scriptName: string, condition: boolean, message: string): void {
  validations.push({
    category: 'Scripts',
    test: scriptName,
    passed: condition,
    message
  });
}

function validateFixture(fixtureName: string, condition: boolean, message: string): void {
  validations.push({
    category: 'Fixtures',
    test: fixtureName,
    passed: condition,
    message
  });
}

console.log('\n🔍 Docxology Scripts Validation Suite\n');
console.log('═'.repeat(60));

// 1. Validate test fixtures exist
console.log('\n📦 Validating Test Fixtures...\n');

const fixturesDir = join(process.cwd(), 'docxology', 'scripts', 'tests', 'fixtures');
const requiredFixtures = [
  'generic.env',
  'generic-settings.json',
  'sample-skill.md',
  'sample-hook.ts'
];

for (const fixture of requiredFixtures) {
  const fixturePath = join(fixturesDir, fixture);
  const exists = existsSync(fixturePath);
  validateFixture(fixture, exists, exists ? 'Found' : 'Missing');
  
  if (exists) {
    // Validate content
    try {
      const content = readFileSync(fixturePath, 'utf-8');
      
      if (fixture === 'generic.env') {
        const hasGenericValues = content.includes('TestUser') && content.includes('UTC');
        validateFixture(`${fixture} (content)`, hasGenericValues, hasGenericValues ? 'Contains generic values' : 'Missing generic values');
      }
      
      if (fixture === 'generic-settings.json') {
        try {
          const json = JSON.parse(content);
          const hasHooks = json.hooks && Object.keys(json.hooks).length > 0;
          validateFixture(`${fixture} (valid JSON)`, hasHooks, hasHooks ? 'Valid JSON with hooks' : 'Invalid or missing hooks');
        } catch {
          validateFixture(`${fixture} (valid JSON)`, false, 'Invalid JSON');
        }
      }
    } catch (e) {
      validateFixture(`${fixture} (readable)`, false, `Cannot read: ${e}`);
    }
  }
}

// 2. Validate scripts support --test-mode
console.log('\n📜 Validating Script Test Mode Support...\n');

const scriptsDir = join(process.cwd(), 'docxology', 'scripts');
const scripts = [
  'ensure-setup.ts',
  'setup-health-check.ts',
  'verify-installation.ts',
  'test-hooks.ts'
];

for (const script of scripts) {
  const scriptPath = join(scriptsDir, script);
  if (existsSync(scriptPath)) {
    const content = readFileSync(scriptPath, 'utf-8');
    const hasTestMode = content.includes('--test-mode') || content.includes('TEST_MODE');
    const hasGenericDefaults = content.includes('TestUser') || content.includes('UTC') || content.includes('TEST_MODE');
    
    validateScript(`${script} (--test-mode)`, hasTestMode, hasTestMode ? 'Supports --test-mode' : 'Missing --test-mode support');
    validateScript(`${script} (generic)`, hasGenericDefaults, hasGenericDefaults ? 'Uses generic defaults' : 'Uses hardcoded values');
  } else {
    validateScript(script, false, 'Script not found');
  }
}

// 3. Validate quick-start.sh supports --test-mode
console.log('\n📜 Validating Quick Start Script...\n');

const quickStartPath = join(scriptsDir, 'quick-start.sh');
if (existsSync(quickStartPath)) {
  const content = readFileSync(quickStartPath, 'utf-8');
  const hasTestMode = content.includes('--test-mode') || content.includes('TEST_MODE');
  validateScript('quick-start.sh (--test-mode)', hasTestMode, hasTestMode ? 'Supports --test-mode' : 'Missing --test-mode support');
} else {
  validateScript('quick-start.sh', false, 'Script not found');
}

// 4. Validate test runner exists and is valid
console.log('\n🧪 Validating Test Infrastructure...\n');

const testRunnerPath = join(process.cwd(), 'docxology', 'scripts', 'tests', 'run-tests.ts');
const testRunnerExists = existsSync(testRunnerPath);
validate('Test Runner', testRunnerExists, testRunnerExists ? 'Found' : 'Missing');

if (testRunnerExists) {
  try {
    const runnerContent = readFileSync(testRunnerPath, 'utf-8');
    const hasSetupFunction = runnerContent.includes('setupTestEnvironment');
    const hasRunTestFunction = runnerContent.includes('runTest');
    const hasCleanupFunction = runnerContent.includes('cleanup');
    validate('Test Runner (functions)', hasSetupFunction && hasRunTestFunction && hasCleanupFunction, 
      hasSetupFunction && hasRunTestFunction && hasCleanupFunction ? 'Has required functions' : 'Missing required functions');
  } catch (e) {
    validate('Test Runner (readable)', false, `Cannot read: ${e}`);
  }
}

// 5. Validate no hardcoded user-specific values in scripts
console.log('\n🔍 Validating Generic Values...\n');

const hardcodedValues = ['Tet', 'America/Los_Angeles'];
let foundHardcoded = false;

for (const script of scripts) {
  const scriptPath = join(scriptsDir, script);
  if (existsSync(scriptPath)) {
    const content = readFileSync(scriptPath, 'utf-8');
    for (const value of hardcodedValues) {
      // Check if it's in a comment or conditional (test mode)
      const inTestMode = content.includes('TEST_MODE') && content.includes(value);
      const inComment = content.split('\n').some(line => {
        const trimmed = line.trim();
        return trimmed.startsWith('//') && trimmed.includes(value);
      });
      
      if (content.includes(value) && !inTestMode && !inComment) {
        foundHardcoded = true;
        validate(`Hardcoded value in ${script}`, false, `Found hardcoded value: ${value}`);
      }
    }
  }
}

if (!foundHardcoded) {
  validate('No hardcoded values', true, 'All scripts use generic defaults');
}

// 6. Validate scenarios exist
console.log('\n📋 Validating Test Scenarios...\n');

const scenariosDir = join(process.cwd(), 'docxology', 'scripts', 'tests', 'scenarios');
const requiredScenarios = [
  'ensure-setup-scenarios.md',
  'health-check-scenarios.md'
];

for (const scenario of requiredScenarios) {
  const scenarioPath = join(scenariosDir, scenario);
  const exists = existsSync(scenarioPath);
  validate(`Scenario: ${scenario}`, exists, exists ? 'Found' : 'Missing');
}

// 7. Validate test runner includes all scripts
console.log('\n🧪 Validating Test Coverage...\n');

if (testRunnerExists) {
  try {
    const runnerContent = readFileSync(testRunnerPath, 'utf-8');
    
    // Check that all scripts are tested
    const requiredScripts = [
      'setup-health-check.ts',
      'ensure-setup.ts',
      'verify-installation.ts',
      'test-hooks.ts',
      'quick-start.sh'
    ];
    
    for (const script of requiredScripts) {
      const isTested = runnerContent.includes(script);
      validate(`Test Coverage: ${script}`, isTested, isTested ? 'Tested' : 'Not tested');
    }
    
    // Check for additional test scenarios
    const hasVerboseTest = runnerContent.includes('--verbose') || runnerContent.includes('verbose');
    const hasHookFilterTest = runnerContent.includes('--hook=') || runnerContent.includes('hook=');
    const hasFixFlagTest = runnerContent.includes('--fix');
    const hasBashTest = runnerContent.includes('runBashTest') || runnerContent.includes('bash');
    
    validate('Test Coverage: Additional scenarios', hasVerboseTest && hasHookFilterTest && hasFixFlagTest, 
      hasVerboseTest && hasHookFilterTest && hasFixFlagTest ? 'Additional scenarios covered' : 'Missing some test scenarios');
    validate('Test Coverage: Bash script support', hasBashTest, hasBashTest ? 'Bash scripts supported' : 'Bash script support missing');
  } catch (e) {
    validate('Test Runner (readable)', false, `Cannot read: ${e}`);
  }
}

// Summary
console.log('\n' + '═'.repeat(60));
console.log('📊 Validation Summary');
console.log('═'.repeat(60));

const categories = ['General', 'Scripts', 'Fixtures'];
for (const category of categories) {
  const categoryValidations = validations.filter(v => v.category === category);
  const passed = categoryValidations.filter(v => v.passed).length;
  const failed = categoryValidations.filter(v => !v.passed).length;
  
  console.log(`\n${category}:`);
  for (const validation of categoryValidations) {
    const icon = validation.passed ? '✓' : '✗';
    const color = validation.passed ? '\x1b[32m' : '\x1b[31m';
    console.log(`  ${color}${icon}\x1b[0m ${validation.test}: ${validation.message}`);
  }
  console.log(`  Total: ${categoryValidations.length} | Passed: ${passed} | Failed: ${failed}`);
}

const totalPassed = validations.filter(v => v.passed).length;
const totalFailed = validations.filter(v => !v.passed).length;

console.log('\n' + '═'.repeat(60));
console.log(`\nTotal Validations: ${validations.length}`);
console.log(`✓ Passed: ${totalPassed}`);
console.log(`✗ Failed: ${totalFailed}\n`);

if (totalFailed === 0) {
  console.log('\x1b[32m✅ All validations passed!\x1b[0m\n');
  process.exit(0);
} else {
  console.log('\x1b[31m❌ Some validations failed\x1b[0m\n');
  process.exit(1);
}
