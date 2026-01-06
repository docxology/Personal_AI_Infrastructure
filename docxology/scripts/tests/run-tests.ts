#!/usr/bin/env bun
/**
 * Test Runner for Docxology Scripts
 * 
 * Runs all scripts in test mode with generic data and validates outputs.
 * 
 * Usage:
 *   bun run docxology/scripts/tests/run-tests.ts
 */

import { existsSync, mkdirSync, rmSync, writeFileSync, readFileSync, chmodSync } from 'fs';
import { join } from 'path';

const TEST_PAI_DIR = join(process.cwd(), 'docxology', 'scripts', 'tests', 'test-pai');
const FIXTURES_DIR = join(process.cwd(), 'docxology', 'scripts', 'tests', 'fixtures');

interface TestResult {
  script: string;
  passed: boolean;
  exitCode: number;
  output: string;
  error?: string;
}

const results: TestResult[] = [];

function setupTestEnvironment(): void {
  console.log('🔧 Setting up test environment...\n');
  
  // Clean up previous test directory
  if (existsSync(TEST_PAI_DIR)) {
    try {
      rmSync(TEST_PAI_DIR, { recursive: true, force: true });
    } catch (e) {
      console.log(`⚠ Warning: Could not clean up test directory: ${e}`);
    }
  }
  
  // Create test PAI directory structure
  mkdirSync(TEST_PAI_DIR, { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'hooks'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'hooks', 'lib'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'skills'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'skills', 'CORE'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'history', 'sessions'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'history', 'learnings'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'history', 'research'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'history', 'decisions'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'history', 'raw-outputs'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'history', 'execution', 'features'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'history', 'execution', 'bugs'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'history', 'execution', 'refactors'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'tools'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'voice'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'observability'), { recursive: true });
  
  // Copy sample skill file
  const sampleSkill = join(FIXTURES_DIR, 'sample-skill.md');
  if (existsSync(sampleSkill)) {
    writeFileSync(
      join(TEST_PAI_DIR, 'skills', 'CORE', 'SKILL.md'),
      readFileSync(sampleSkill, 'utf-8')
    );
  }
  
  // Create all required hook files for testing
  const sampleHook = join(FIXTURES_DIR, 'sample-hook.ts');
  const defaultHookContent = existsSync(sampleHook) 
    ? readFileSync(sampleHook, 'utf-8')
    : '#!/usr/bin/env bun\nconst input = JSON.parse(await Bun.stdin.text());\nprocess.exit(0);\n';
  
  // Security validator needs to actually validate commands
  const securityValidatorContent = `#!/usr/bin/env bun
try {
  const inputText = await Bun.stdin.text();
  const input = JSON.parse(inputText);
  const command = input?.tool_input?.command || '';
  const dangerous = ['rm -rf /', 'cat /etc/passwd', 'dd if='].some(c => command.includes(c));
  process.exit(dangerous ? 2 : 0);
} catch (e) {
  // If we can't parse input, allow it (for test compatibility)
  process.exit(0);
}
`;
  
  const requiredHooks = [
    { name: 'security-validator.ts', content: securityValidatorContent },
    { name: 'initialize-session.ts', content: defaultHookContent },
    { name: 'load-core-context.ts', content: defaultHookContent },
    { name: 'update-tab-titles.ts', content: defaultHookContent },
    { name: 'stop-hook.ts', content: defaultHookContent },
    { name: 'subagent-stop-hook.ts', content: defaultHookContent },
    { name: 'capture-all-events.ts', content: defaultHookContent },
    { name: 'capture-session-summary.ts', content: defaultHookContent },
  ];
  
  for (const hook of requiredHooks) {
    writeFileSync(join(TEST_PAI_DIR, 'hooks', hook.name), hook.content);
  }
  
  // Create required lib files
  const libContent = '// Test lib file\n';
  const requiredLibs = [
    'observability.ts',
    'metadata-extraction.ts',
  ];
  
  for (const lib of requiredLibs) {
    writeFileSync(join(TEST_PAI_DIR, 'hooks', 'lib', lib), libContent);
  }
  
  // Create required tool files
  const toolContent = '#!/usr/bin/env bun\n// Test tool file\n';
  const requiredTools = [
    'SkillSearch.ts',
    'GenerateSkillIndex.ts',
    'PaiArchitecture.ts',
  ];
  
  for (const tool of requiredTools) {
    writeFileSync(join(TEST_PAI_DIR, 'tools', tool), toolContent);
  }
  
  // Create skill index file
  const skillIndex = {
    skills: [
      {
        name: 'CORE',
        path: join(TEST_PAI_DIR, 'skills', 'CORE', 'SKILL.md'),
        description: 'Core skill for testing'
      }
    ]
  };
  writeFileSync(
    join(TEST_PAI_DIR, 'skills', 'skill-index.json'),
    JSON.stringify(skillIndex, null, 2)
  );
  
  // Create .env file from fixture
  const envFixture = join(FIXTURES_DIR, 'generic.env');
  if (existsSync(envFixture)) {
    let envContent = readFileSync(envFixture, 'utf-8');
    envContent = envContent.replace(/\${PAI_DIR}/g, TEST_PAI_DIR);
    writeFileSync(join(TEST_PAI_DIR, '.env'), envContent);
  }
  
  // Create settings.json from fixture
  const settingsFixture = join(FIXTURES_DIR, 'generic-settings.json');
  if (existsSync(settingsFixture)) {
    let settingsContent = readFileSync(settingsFixture, 'utf-8');
    settingsContent = settingsContent.replace(/\${PAI_DIR}/g, TEST_PAI_DIR);
    writeFileSync(join(TEST_PAI_DIR, 'settings.json'), settingsContent);
  }
  
  // Create mock voice server
  writeFileSync(join(TEST_PAI_DIR, 'voice', 'server.ts'), '#!/usr/bin/env bun\n// Mock voice server\n');
  
  // Create mock observability server structure
  mkdirSync(join(TEST_PAI_DIR, 'observability', 'apps', 'server'), { recursive: true });
  mkdirSync(join(TEST_PAI_DIR, 'observability', 'apps', 'client'), { recursive: true });
  const manageScript = join(TEST_PAI_DIR, 'observability', 'manage.sh');
  writeFileSync(manageScript, '#!/bin/bash\n# Mock manage script\n');
  // Make it executable
  try {
    chmodSync(manageScript, 0o755);
  } catch (e) {
    // Ignore chmod errors on some systems
  }
  
  // Validate test environment was created correctly
  const criticalPaths = [
    join(TEST_PAI_DIR, 'hooks'),
    join(TEST_PAI_DIR, 'skills', 'CORE'),
    join(TEST_PAI_DIR, '.env'),
    join(TEST_PAI_DIR, 'settings.json')
  ];
  
  const missingPaths = criticalPaths.filter(p => !existsSync(p));
  if (missingPaths.length > 0) {
    console.log(`⚠ Warning: Some test paths not created: ${missingPaths.join(', ')}`);
  }
  
  console.log('✓ Test environment ready\n');
}

function runTest(scriptName: string, args: string[] = []): TestResult {
  const scriptPath = join(process.cwd(), 'docxology', 'scripts', scriptName);
  
  // Verify script exists before running
  if (!existsSync(scriptPath)) {
    console.log(`\n🧪 Testing: ${scriptName}`);
    console.log(`   ✗ Script not found: ${scriptPath}`);
    return {
      script: scriptName,
      passed: false,
      exitCode: -1,
      output: '',
      error: `Script not found: ${scriptPath}`
    };
  }
  
  const testArgs = ['--test-mode', ...args];
  
  console.log(`\n🧪 Testing: ${scriptName}`);
  console.log(`   Args: ${testArgs.join(' ')}`);
  
  try {
    const result = Bun.spawnSync([
      'bun', 'run', scriptPath, ...testArgs
    ], {
      stdout: 'pipe',
      stderr: 'pipe',
      env: { ...process.env, PAI_DIR: TEST_PAI_DIR },
      cwd: process.cwd()
    });
    
    const exitCode = result.exitCode ?? -1;
    const stdout = result.stdout?.toString() || '';
    const stderr = result.stderr?.toString() || '';
    
    const passed = exitCode === 0;
    
    if (passed) {
      console.log(`   ✓ Passed (exit code: ${exitCode})`);
    } else {
      console.log(`   ✗ Failed (exit code: ${exitCode})`);
      if (stdout) {
        console.log(`   Output:\n${stdout.split('\n').map((l: string) => `      ${l}`).join('\n').substring(0, 1000)}`);
      }
      if (stderr) {
        console.log(`   Error: ${stderr.substring(0, 500)}`);
      }
    }
    
    return {
      script: scriptName,
      passed,
      exitCode,
      output: stdout,
      error: stderr || undefined
    };
  } catch (e) {
    console.log(`   ✗ Exception: ${e}`);
    return {
      script: scriptName,
      passed: false,
      exitCode: -1,
      output: '',
      error: String(e)
    };
  }
}

function runBashTest(scriptName: string, args: string[] = []): TestResult {
  const scriptPath = join(process.cwd(), 'docxology', 'scripts', scriptName);
  
  // Verify script exists before running
  if (!existsSync(scriptPath)) {
    console.log(`\n🧪 Testing: ${scriptName}`);
    console.log(`   ✗ Script not found: ${scriptPath}`);
    return {
      script: scriptName,
      passed: false,
      exitCode: -1,
      output: '',
      error: `Script not found: ${scriptPath}`
    };
  }
  
  const testArgs = ['--test-mode', ...args];
  
  console.log(`\n🧪 Testing: ${scriptName}`);
  console.log(`   Args: ${testArgs.join(' ')}`);
  
  try {
    // Make script executable if needed
    try {
      chmodSync(scriptPath, 0o755);
    } catch {
      // Ignore chmod errors
    }
    
    const result = Bun.spawnSync([
      'bash', scriptPath, ...testArgs
    ], {
      stdout: 'pipe',
      stderr: 'pipe',
      env: { ...process.env, PAI_DIR: TEST_PAI_DIR },
      cwd: process.cwd()
    });
    
    const exitCode = result.exitCode ?? -1;
    const stdout = result.stdout?.toString() || '';
    const stderr = result.stderr?.toString() || '';
    
    const passed = exitCode === 0;
    
    if (passed) {
      console.log(`   ✓ Passed (exit code: ${exitCode})`);
    } else {
      console.log(`   ✗ Failed (exit code: ${exitCode})`);
      if (stdout) {
        console.log(`   Output:\n${stdout.split('\n').map((l: string) => `      ${l}`).join('\n').substring(0, 1000)}`);
      }
      if (stderr) {
        console.log(`   Error: ${stderr.substring(0, 500)}`);
      }
    }
    
    return {
      script: scriptName,
      passed,
      exitCode,
      output: stdout,
      error: stderr || undefined
    };
  } catch (e) {
    console.log(`   ✗ Exception: ${e}`);
    return {
      script: scriptName,
      passed: false,
      exitCode: -1,
      output: '',
      error: String(e)
    };
  }
}

function cleanup(): void {
  console.log('\n🧹 Cleaning up test environment...');
  if (existsSync(TEST_PAI_DIR)) {
    try {
      rmSync(TEST_PAI_DIR, { recursive: true, force: true });
      console.log('✓ Cleanup complete\n');
    } catch (e) {
      console.log(`⚠ Warning: Could not fully clean up test directory: ${e}\n`);
    }
  } else {
    console.log('✓ Cleanup complete (no directory to clean)\n');
  }
}

// Main execution
console.log('\n🚀 Docxology Script Test Runner\n');
console.log('═'.repeat(60));

setupTestEnvironment();

// Run tests for TypeScript scripts
const scripts = [
  'setup-health-check.ts',
  'ensure-setup.ts',
  'verify-installation.ts',
  'test-hooks.ts'
];

for (const script of scripts) {
  const result = runTest(script);
  results.push(result);
}

// Test ensure-setup with --fix flag
const ensureSetupFix = runTest('ensure-setup.ts', ['--fix']);
results.push(ensureSetupFix);

// Test verify-installation with --verbose flag
const verifyInstallationVerbose = runTest('verify-installation.ts', ['--verbose']);
results.push(verifyInstallationVerbose);

// Test test-hooks with specific hook filter
const testHooksSpecific = runTest('test-hooks.ts', ['--hook=security-validator']);
results.push(testHooksSpecific);

// Test bash scripts
const bashScripts = [
  'quick-start.sh'
];

for (const script of bashScripts) {
  const result = runBashTest(script);
  results.push(result);
}

// Summary
console.log('\n' + '═'.repeat(60));
console.log('📊 Test Summary');
console.log('═'.repeat(60));

const passed = results.filter(r => r.passed).length;
const failed = results.filter(r => !r.passed).length;

console.log(`\nTotal Tests: ${results.length}`);
console.log(`✓ Passed: ${passed}`);
console.log(`✗ Failed: ${failed}\n`);

for (const result of results) {
  const icon = result.passed ? '✓' : '✗';
  const color = result.passed ? '\x1b[32m' : '\x1b[31m';
  console.log(`${color}${icon}\x1b[0m ${result.script} (exit: ${result.exitCode})`);
}

cleanup();

if (failed === 0) {
  console.log('\x1b[32m✅ All tests passed!\x1b[0m\n');
  process.exit(0);
} else {
  console.log('\x1b[31m❌ Some tests failed\x1b[0m\n');
  process.exit(1);
}
