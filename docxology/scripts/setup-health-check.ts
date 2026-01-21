#!/usr/bin/env bun
/**
 * PAI Setup Health Check
 * 
 * Quick health check for PAI system status.
 * Faster than full verification - checks critical components only.
 * 
 * Usage:
 *   bun run docxology/scripts/setup-health-check.ts
 *   bun run docxology/scripts/setup-health-check.ts --test-mode
 */

import { existsSync, readFileSync } from 'fs';
import { join } from 'path';
import { homedir } from 'os';

const TEST_MODE = process.argv.includes('--test-mode');

// In test mode, use a temporary directory or provided PAI_DIR
const PAI_DIR = TEST_MODE
  ? (process.env.PAI_DIR || join(process.cwd(), 'docxology', 'scripts', 'tests', 'test-pai'))
  : (process.env.PAI_DIR || join(homedir(), '.claude'));

interface HealthStatus {
  component: string;
  status: 'healthy' | 'degraded' | 'unhealthy';
  message: string;
}

const statuses: HealthStatus[] = [];

function checkHealth(component: string, condition: boolean, degradedCondition?: boolean): void {
  let status: 'healthy' | 'degraded' | 'unhealthy';
  let message: string;
  
  if (condition) {
    status = 'healthy';
    message = 'OK';
  } else if (degradedCondition) {
    status = 'degraded';
    message = 'Partial';
  } else {
    status = 'unhealthy';
    message = 'Missing';
  }
  
  statuses.push({ component, status, message });
}

console.log('\n🏥 PAI Health Check\n');
if (TEST_MODE) {
  console.log('🧪 TEST MODE - Using test PAI directory\n');
}

// Critical components
checkHealth('PAI Directory', existsSync(PAI_DIR));
checkHealth('Hooks Directory', existsSync(join(PAI_DIR, 'hooks')));
checkHealth('Skills Directory', existsSync(join(PAI_DIR, 'skills')));
checkHealth('CORE Skill', existsSync(join(PAI_DIR, 'skills', 'CORE', 'SKILL.md')));
checkHealth('Security Validator', existsSync(join(PAI_DIR, 'hooks', 'security-validator.ts')));
checkHealth('Session Initializer', existsSync(join(PAI_DIR, 'hooks', 'initialize-session.ts')));
checkHealth('Context Loader', existsSync(join(PAI_DIR, 'hooks', 'load-core-context.ts')));

// Configuration
const settingsPath = TEST_MODE
  ? join(PAI_DIR, 'settings.json')
  : join(homedir(), '.claude', 'settings.json');
let hasHooks = false;
if (existsSync(settingsPath)) {
  try {
    const settings = JSON.parse(readFileSync(settingsPath, 'utf-8'));
    hasHooks = !!(settings.hooks && Object.keys(settings.hooks).length > 0);
  } catch {}
}
checkHealth('Hooks Configuration', hasHooks);

// Environment
const envPath = join(PAI_DIR, '.env');
const hasEnv = existsSync(envPath);
let hasDA = false;
if (hasEnv) {
  try {
    const env = readFileSync(envPath, 'utf-8');
    hasDA = env.includes('DA=');
  } catch {}
}
checkHealth('Environment Config', hasEnv && hasDA, hasEnv);

// History system
checkHealth('History System', existsSync(join(PAI_DIR, 'history', 'sessions')));

// Tools
checkHealth('Core Tools', existsSync(join(PAI_DIR, 'tools', 'GenerateSkillIndex.ts')));

// Display results
console.log('Component Status:');
console.log('─'.repeat(50));

for (const status of statuses) {
  const icon = status.status === 'healthy' ? '✓' : status.status === 'degraded' ? '⚠' : '✗';
  const color = status.status === 'healthy' ? '\x1b[32m' : status.status === 'degraded' ? '\x1b[33m' : '\x1b[31m';
  console.log(`${color}${icon}\x1b[0m ${status.component.padEnd(30)} ${status.message}`);
}

console.log('─'.repeat(50));

const healthy = statuses.filter(s => s.status === 'healthy').length;
const degraded = statuses.filter(s => s.status === 'degraded').length;
const unhealthy = statuses.filter(s => s.status === 'unhealthy').length;

console.log(`\nHealthy: ${healthy} | Degraded: ${degraded} | Unhealthy: ${unhealthy}\n`);

if (unhealthy === 0 && degraded === 0) {
  console.log('\x1b[32m✅ System is fully operational\x1b[0m\n');
  process.exit(0);
} else if (unhealthy === 0) {
  console.log('\x1b[33m⚠️  System is operational with minor issues\x1b[0m\n');
  process.exit(0);
} else {
  console.log('\x1b[31m❌ System has critical issues - run full verification\x1b[0m\n');
  console.log('Run: bun run docxology/scripts/verify-installation.ts\n');
  process.exit(1);
}
