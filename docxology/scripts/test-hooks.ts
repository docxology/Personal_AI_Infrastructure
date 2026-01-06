#!/usr/bin/env bun
/**
 * PAI Hook Testing Script
 * 
 * Tests all installed hooks with sample payloads.
 * 
 * Usage:
 *   bun run docxology/scripts/test-hooks.ts
 *   bun run docxology/scripts/test-hooks.ts --hook security-validator
 *   bun run docxology/scripts/test-hooks.ts --test-mode
 */

import { existsSync } from 'fs';
import { join } from 'path';
import { homedir } from 'os';

const TEST_MODE = process.argv.includes('--test-mode');
const SPECIFIC_HOOK = process.argv.find(arg => arg.startsWith('--hook='))?.split('=')[1];

// In test mode, use a temporary directory or provided PAI_DIR
const PAI_DIR = TEST_MODE
  ? (process.env.PAI_DIR || join(process.cwd(), 'docxology', 'scripts', 'tests', 'test-pai'))
  : (process.env.PAI_DIR || join(homedir(), '.claude'));

interface HookTest {
  name: string;
  file: string;
  payload: any;
  expectedExitCode: number;
  description: string;
}

const tests: HookTest[] = [
  {
    name: 'security-validator',
    file: 'security-validator.ts',
    payload: {
      session_id: 'test-123',
      tool_name: 'Bash',
      tool_input: { command: 'ls -la' }
    },
    expectedExitCode: 0,
    description: 'Allows safe command'
  },
  {
    name: 'security-validator',
    file: 'security-validator.ts',
    payload: {
      session_id: 'test-123',
      tool_name: 'Bash',
      tool_input: { command: 'rm -rf /' }
    },
    expectedExitCode: 2,
    description: 'Blocks dangerous command'
  },
  {
    name: 'security-validator',
    file: 'security-validator.ts',
    payload: {
      session_id: 'test-123',
      tool_name: 'Bash',
      tool_input: { command: 'echo "Hello World"' }
    },
    expectedExitCode: 0,
    description: 'Allows safe echo command'
  },
  {
    name: 'security-validator',
    file: 'security-validator.ts',
    payload: {
      session_id: 'test-123',
      tool_name: 'Bash',
      tool_input: { command: 'cat /etc/passwd' }
    },
    expectedExitCode: 2,
    description: 'Blocks sensitive file access'
  },
  {
    name: 'initialize-session',
    file: 'initialize-session.ts',
    payload: {
      session_id: 'test-session-123',
      cwd: process.cwd()
    },
    expectedExitCode: 0,
    description: 'Initializes session'
  },
  {
    name: 'initialize-session',
    file: 'initialize-session.ts',
    payload: {
      session_id: 'generic-test-session',
      cwd: '/tmp'
    },
    expectedExitCode: 0,
    description: 'Initializes session with custom directory'
  },
  {
    name: 'load-core-context',
    file: 'load-core-context.ts',
    payload: {
      session_id: 'test-session-123'
    },
    expectedExitCode: 0,
    description: 'Loads core context'
  },
  {
    name: 'update-tab-titles',
    file: 'update-tab-titles.ts',
    payload: {
      session_id: 'test-session-123',
      prompt: 'Create a new blog post about AI'
    },
    expectedExitCode: 0,
    description: 'Updates tab title'
  },
  {
    name: 'update-tab-titles',
    file: 'update-tab-titles.ts',
    payload: {
      session_id: 'test-session-123',
      prompt: 'Generic test prompt for validation'
    },
    expectedExitCode: 0,
    description: 'Updates tab title with generic prompt'
  }
];

console.log('\n🧪 PAI Hook Testing\n');
if (TEST_MODE) {
  console.log('🧪 TEST MODE - Using test PAI directory\n');
}

let passed = 0;
let failed = 0;

for (const test of tests) {
  if (SPECIFIC_HOOK && test.name !== SPECIFIC_HOOK) {
    continue;
  }
  
  const hookPath = join(PAI_DIR, 'hooks', test.file);
  
  if (!existsSync(hookPath)) {
    console.log(`⚠ ${test.name}: Hook file not found (${test.file})`);
    continue;
  }
  
  try {
    const result = Bun.spawnSync([
      'bun', 'run', hookPath
    ], {
      stdin: Buffer.from(JSON.stringify(test.payload)),
      stdout: 'pipe',
      stderr: 'pipe'
    });
    
    const exitCode = result.exitCode ?? -1;
    const stdout = result.stdout;
    const stderr = result.stderr;
    
    const success = exitCode === test.expectedExitCode;
    
    if (success) {
      console.log(`✓ ${test.name}: ${test.description}`);
      passed++;
    } else {
      console.log(`✗ ${test.name}: ${test.description}`);
      console.log(`  Expected exit code ${test.expectedExitCode}, got ${exitCode}`);
      if (stderr && stderr.toString()) {
        console.log(`  Error: ${stderr.toString().trim()}`);
      }
      failed++;
    }
  } catch (e) {
    console.log(`✗ ${test.name}: Test failed with exception`);
    console.log(`  ${e}`);
    failed++;
  }
}

console.log('\n' + '─'.repeat(50));
console.log(`Passed: ${passed} | Failed: ${failed}\n`);

if (failed === 0) {
  console.log('\x1b[32m✅ All hook tests passed!\x1b[0m\n');
  process.exit(0);
} else {
  console.log('\x1b[31m❌ Some hook tests failed\x1b[0m\n');
  process.exit(1);
}
