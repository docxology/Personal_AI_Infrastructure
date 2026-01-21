#!/usr/bin/env bun
/**
 * PAI Installation Verification Script
 * 
 * Comprehensive health check for all installed PAI packs and components.
 * Run this after installation or when troubleshooting.
 * 
 * Usage:
 *   bun run docxology/scripts/verify-installation.ts
 *   bun run docxology/scripts/verify-installation.ts --verbose
 *   bun run docxology/scripts/verify-installation.ts --test-mode
 */

import { existsSync, readFileSync, statSync } from 'fs';
import { join } from 'path';
import { homedir } from 'os';

const TEST_MODE = process.argv.includes('--test-mode');
const VERBOSE = process.argv.includes('--verbose') || process.argv.includes('-v');

// In test mode, use a temporary directory or provided PAI_DIR
const PAI_DIR = TEST_MODE
  ? (process.env.PAI_DIR || join(process.cwd(), 'docxology', 'scripts', 'tests', 'test-pai'))
  : (process.env.PAI_DIR || join(homedir(), '.claude'));

interface CheckResult {
  name: string;
  status: 'pass' | 'fail' | 'warn';
  message: string;
  details?: string;
}

const results: CheckResult[] = [];

function check(name: string, condition: boolean, message: string, details?: string): void {
  const status = condition ? 'pass' : 'fail';
  results.push({ name, status, message, details });
  
  if (VERBOSE || !condition) {
    const icon = condition ? '✓' : '✗';
    const color = condition ? '\x1b[32m' : '\x1b[31m';
    console.log(`${color}${icon}\x1b[0m ${name}: ${message}`);
    if (details) console.log(`   ${details}`);
  }
}

function warn(name: string, message: string, details?: string): void {
  results.push({ name, status: 'warn', message, details });
  if (VERBOSE) {
    console.log(`\x1b[33m⚠\x1b[0m ${name}: ${message}`);
    if (details) console.log(`   ${details}`);
  }
}

console.log('\n🔍 PAI Installation Verification\n');
if (TEST_MODE) {
  console.log('🧪 TEST MODE - Using test PAI directory\n');
}
console.log(`PAI_DIR: ${PAI_DIR}\n`);

// ============================================================================
// 1. ENVIRONMENT & DEPENDENCIES
// ============================================================================

console.log('📦 Environment & Dependencies');
console.log('─'.repeat(60));

// Check Bun
try {
  const bunVersion = Bun.version;
  check('Bun Runtime', true, `Installed (v${bunVersion})`);
} catch {
  check('Bun Runtime', false, 'Not found - install with: curl -fsSL https://bun.sh/install | bash');
}

// Check PAI_DIR
check('PAI Directory', existsSync(PAI_DIR), `Exists at ${PAI_DIR}`, existsSync(PAI_DIR) ? undefined : 'Create directory or set PAI_DIR environment variable');

// Check .env file
const envPath = join(PAI_DIR, '.env');
const envExists = existsSync(envPath);
check('.env File', envExists, envExists ? 'Found' : 'Missing - API keys may not be configured');

if (envExists) {
  try {
    const envContent = readFileSync(envPath, 'utf-8');
    const hasDA = envContent.includes('DA=');
    const hasTimeZone = envContent.includes('TIME_ZONE=');
    check('DA Variable', hasDA, hasDA ? 'Set' : 'Not set');
    check('TIME_ZONE Variable', hasTimeZone, hasTimeZone ? 'Set' : 'Not set');
    
    if (envContent.includes('ELEVENLABS_API_KEY')) {
      check('ElevenLabs API Key', true, 'Configured (voice system enabled)');
    } else {
      warn('ElevenLabs API Key', 'Not configured (voice system disabled)');
    }
  } catch (e) {
    check('.env Readable', false, `Cannot read: ${e}`);
  }
}

// Check settings.json
const settingsPath = TEST_MODE
  ? join(PAI_DIR, 'settings.json')
  : join(homedir(), '.claude', 'settings.json');
const settingsExists = existsSync(settingsPath);
check('settings.json', settingsExists, settingsExists ? 'Found' : 'Missing - hooks will not work');

if (settingsExists) {
  try {
    const settings = JSON.parse(readFileSync(settingsPath, 'utf-8'));
    const hasHooks = settings.hooks && typeof settings.hooks === 'object';
    check('Hooks Configuration', hasHooks, hasHooks ? 'Configured' : 'Missing hooks section');
    
    if (hasHooks) {
      const hookEvents = Object.keys(settings.hooks);
      check('Hook Events', hookEvents.length > 0, `${hookEvents.length} event types configured`, hookEvents.join(', '));
    }
  } catch (e) {
    check('settings.json Valid', false, `Invalid JSON: ${e}`);
  }
}

console.log('');

// ============================================================================
// 2. HOOK SYSTEM
// ============================================================================

console.log('🪝 Hook System');
console.log('─'.repeat(60));

const hooksDir = join(PAI_DIR, 'hooks');
const hooksLibDir = join(hooksDir, 'lib');

check('Hooks Directory', existsSync(hooksDir), existsSync(hooksDir) ? 'Exists' : 'Missing');

if (existsSync(hooksDir)) {
  const requiredHooks = [
    'security-validator.ts',
    'initialize-session.ts',
    'load-core-context.ts',
    'update-tab-titles.ts',
    'stop-hook.ts',
    'subagent-stop-hook.ts',
    'capture-all-events.ts',
    'capture-session-summary.ts',
  ];
  
  const optionalHooks = [
    'stop-hook-voice.ts',
    'subagent-stop-hook-voice.ts',
  ];
  
  for (const hook of requiredHooks) {
    const hookPath = join(hooksDir, hook);
    check(`Hook: ${hook}`, existsSync(hookPath), existsSync(hookPath) ? 'Installed' : 'Missing');
  }
  
  for (const hook of optionalHooks) {
    const hookPath = join(hooksDir, hook);
    if (existsSync(hookPath)) {
      check(`Hook: ${hook}`, true, 'Installed (voice system)');
    } else {
      warn(`Hook: ${hook}`, 'Not installed (voice system disabled)');
    }
  }
  
  // Check lib files
  check('Hooks Lib Directory', existsSync(hooksLibDir), existsSync(hooksLibDir) ? 'Exists' : 'Missing');
  
  if (existsSync(hooksLibDir)) {
    const libFiles = ['observability.ts', 'metadata-extraction.ts', 'prosody-enhancer.ts'];
    for (const lib of libFiles) {
      const libPath = join(hooksLibDir, lib);
      if (existsSync(libPath)) {
        check(`Lib: ${lib}`, true, 'Installed');
      } else if (lib === 'prosody-enhancer.ts') {
        warn(`Lib: ${lib}`, 'Not installed (voice system)');
      } else {
        check(`Lib: ${lib}`, false, 'Missing');
      }
    }
  }
}

console.log('');

// ============================================================================
// 3. SKILL SYSTEM
// ============================================================================

console.log('🎯 Skill System');
console.log('─'.repeat(60));

const skillsDir = join(PAI_DIR, 'skills');
check('Skills Directory', existsSync(skillsDir), existsSync(skillsDir) ? 'Exists' : 'Missing');

if (existsSync(skillsDir)) {
  const requiredSkills = ['CORE'];
  const optionalSkills = ['Prompting', 'Agents', 'Art', 'CreateSkill'];
  
  for (const skill of requiredSkills) {
    const skillPath = join(skillsDir, skill);
    const skillMd = join(skillPath, 'SKILL.md');
    check(`Skill: ${skill}`, existsSync(skillMd), existsSync(skillMd) ? 'Installed' : 'Missing');
  }
  
  for (const skill of optionalSkills) {
    const skillPath = join(skillsDir, skill);
    const skillMd = join(skillPath, 'SKILL.md');
    if (existsSync(skillMd)) {
      check(`Skill: ${skill}`, true, 'Installed');
    } else {
      warn(`Skill: ${skill}`, 'Not installed (optional)');
    }
  }
  
  // Check skill index
  const skillIndexPath = join(skillsDir, 'skill-index.json');
  if (existsSync(skillIndexPath)) {
    try {
      const index = JSON.parse(readFileSync(skillIndexPath, 'utf-8'));
      const skillCount = Array.isArray(index) ? index.length : Object.keys(index).length;
      check('Skill Index', true, `Generated (${skillCount} skills)`);
    } catch {
      check('Skill Index', false, 'Invalid JSON');
    }
  } else {
    warn('Skill Index', 'Not generated - run: bun run tools/GenerateSkillIndex.ts');
  }
}

console.log('');

// ============================================================================
// 4. HISTORY SYSTEM
// ============================================================================

console.log('📚 History System');
console.log('─'.repeat(60));

const historyDir = join(PAI_DIR, 'history');
check('History Directory', existsSync(historyDir), existsSync(historyDir) ? 'Exists' : 'Missing');

if (existsSync(historyDir)) {
  const historyCategories = ['sessions', 'learnings', 'research', 'decisions', 'raw-outputs'];
  const executionCategories = ['features', 'bugs', 'refactors'];
  
  for (const category of historyCategories) {
    const categoryPath = join(historyDir, category);
    check(`Category: ${category}`, existsSync(categoryPath), existsSync(categoryPath) ? 'Exists' : 'Missing');
  }
  
  const executionDir = join(historyDir, 'execution');
  if (existsSync(executionDir)) {
    for (const category of executionCategories) {
      const categoryPath = join(executionDir, category);
      check(`Execution: ${category}`, existsSync(categoryPath), existsSync(categoryPath) ? 'Exists' : 'Missing');
    }
  }
}

console.log('');

// ============================================================================
// 5. TOOLS
// ============================================================================

console.log('🛠️  Tools');
console.log('─'.repeat(60));

const toolsDir = join(PAI_DIR, 'tools');
check('Tools Directory', existsSync(toolsDir), existsSync(toolsDir) ? 'Exists' : 'Missing');

if (existsSync(toolsDir)) {
  const requiredTools = ['SkillSearch.ts', 'GenerateSkillIndex.ts', 'PaiArchitecture.ts'];
  for (const tool of requiredTools) {
    const toolPath = join(toolsDir, tool);
    check(`Tool: ${tool}`, existsSync(toolPath), existsSync(toolPath) ? 'Installed' : 'Missing');
  }
}

console.log('');

// ============================================================================
// 6. VOICE SYSTEM
// ============================================================================

console.log('🔊 Voice System');
console.log('─'.repeat(60));

const voiceDir = join(PAI_DIR, 'voice');
const voiceServer = join(voiceDir, 'server.ts');
check('Voice Directory', existsSync(voiceDir), existsSync(voiceDir) ? 'Exists' : 'Missing');
check('Voice Server', existsSync(voiceServer), existsSync(voiceServer) ? 'Installed' : 'Missing');

if (envExists) {
  try {
    const envContent = readFileSync(envPath, 'utf-8');
    if (envContent.includes('ELEVENLABS_API_KEY')) {
      check('Voice API Key', true, 'ElevenLabs configured');
    } else if (envContent.includes('GOOGLE_API_KEY')) {
      check('Voice API Key', true, 'Google TTS configured');
    } else {
      warn('Voice API Key', 'No TTS API key found');
    }
  } catch {
    // Already checked above
  }
}

console.log('');

// ============================================================================
// 7. OBSERVABILITY SERVER
// ============================================================================

console.log('📊 Observability Server');
console.log('─'.repeat(60));

const observabilityDir = join(PAI_DIR, 'observability');
check('Observability Directory', existsSync(observabilityDir), existsSync(observabilityDir) ? 'Exists' : 'Missing');

if (existsSync(observabilityDir)) {
  const serverDir = join(observabilityDir, 'apps', 'server');
  const clientDir = join(observabilityDir, 'apps', 'client');
  const manageScript = join(observabilityDir, 'manage.sh');
  
  check('Server App', existsSync(serverDir), existsSync(serverDir) ? 'Installed' : 'Missing');
  check('Client App', existsSync(clientDir), existsSync(clientDir) ? 'Installed' : 'Missing');
  check('Manage Script', existsSync(manageScript), existsSync(manageScript) ? 'Installed' : 'Missing');
  
  if (existsSync(manageScript)) {
    const stats = statSync(manageScript);
    check('Manage Script Executable', (stats.mode & parseInt('111', 8)) !== 0, 'Executable');
  }
}

console.log('');

// ============================================================================
// 8. FUNCTIONAL TESTS
// ============================================================================

console.log('🧪 Functional Tests');
console.log('─'.repeat(60));

// Test security validator
try {
  const result = Bun.spawnSync([
    'bun', 'run', join(hooksDir, 'security-validator.ts')
  ], {
    stdin: Buffer.from(JSON.stringify({
      session_id: 'test',
      tool_name: 'Bash',
      tool_input: { command: 'ls -la' }
    })),
    stdout: 'pipe',
    stderr: 'pipe'
  });
  
  const exitCode = result.exitCode ?? -1;
  if (exitCode === 0) {
    check('Security Validator (safe)', true, 'Allows safe commands');
  } else {
    check('Security Validator (safe)', false, `Unexpected exit code: ${exitCode}`);
  }
} catch (e) {
  check('Security Validator (safe)', false, `Test failed: ${e}`);
}

// Test session initialization
try {
  const result = Bun.spawnSync([
    'bun', 'run', join(hooksDir, 'initialize-session.ts')
  ], {
    stdin: Buffer.from(JSON.stringify({
      session_id: 'test-verification',
      cwd: process.cwd()
    })),
    stdout: 'pipe',
    stderr: 'pipe'
  });
  
  const exitCode = result.exitCode ?? -1;
  if (exitCode === 0) {
    check('Session Initialization', true, 'Runs successfully');
  } else {
    check('Session Initialization', false, `Exit code: ${exitCode}`);
  }
} catch (e) {
  check('Session Initialization', false, `Test failed: ${e}`);
}

console.log('');

// ============================================================================
// SUMMARY
// ============================================================================

const passed = results.filter(r => r.status === 'pass').length;
const failed = results.filter(r => r.status === 'fail').length;
const warnings = results.filter(r => r.status === 'warn').length;

console.log('─'.repeat(60));
console.log('📊 Summary');
console.log('─'.repeat(60));
console.log(`✓ Passed:  ${passed}`);
console.log(`✗ Failed:  ${failed}`);
console.log(`⚠ Warnings: ${warnings}`);
console.log(`   Total:   ${results.length}`);
console.log('');

if (failed === 0) {
  console.log('\x1b[32m✅ All critical checks passed!\x1b[0m\n');
  process.exit(0);
} else {
  console.log('\x1b[31m❌ Some checks failed. Review the output above.\x1b[0m\n');
  process.exit(1);
}
