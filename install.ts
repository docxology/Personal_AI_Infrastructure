#!/usr/bin/env bun
/**
 * PAI Installation Wizard v2.4
 *
 * Handles fresh installs, updates, and intelligent migration from existing systems.
 * Now supports split repository pattern with config overlay.
 *
 * Usage:
 *   bun run install.ts                              # Interactive wizard
 *   bun run install.ts --fresh                      # Force fresh install
 *   bun run install.ts --migrate                    # Force migration mode
 *   bun run install.ts --validate                   # Only run validation
 *   bun run install.ts --config-repo PATH           # Use private config repo for overlay
 *   bun run install.ts --setup                      # Fix permissions and start voice server
 */

import { existsSync, mkdirSync, cpSync, readFileSync, writeFileSync, readdirSync, statSync, appendFileSync, rmSync } from 'fs';
import { join, basename } from 'path';
import { homedir, hostname } from 'os';
import { execSync, spawn } from 'child_process';

// ANSI colors
const colors = {
  reset: '\x1b[0m',
  bold: '\x1b[1m',
  dim: '\x1b[2m',
  blue: '\x1b[38;2;59;130;246m',
  green: '\x1b[38;2;34;197;94m',
  yellow: '\x1b[38;2;234;179;8m',
  red: '\x1b[38;2;239;68;68m',
  cyan: '\x1b[38;2;6;182;212m',
  gray: '\x1b[38;2;100;116;139m',
};

const c = colors;

// Paths
const HOME = homedir();
const CLAUDE_DIR = join(HOME, '.claude');
const PAI_MARKER = join(CLAUDE_DIR, '.pai-marker');
const SHELL = process.env.SHELL || '/bin/zsh';
const IS_ZSH = SHELL.includes('zsh');
const SHELL_RC = join(HOME, IS_ZSH ? '.zshrc' : '.bashrc');
const VOICE_SERVER_DIR = join(CLAUDE_DIR, 'VoiceServer');
const VOICE_SERVER_PORT = 8888;
const MACHINE_HOSTNAME = hostname();

// PAI Version
const PAI_VERSION = '2.4';

// Default voice IDs - ElevenLabs pre-made voices
const DEFAULT_VOICES = {
  male: '21m00Tcm4TlvDq8ikWAM',
  female: 'EXAVITQu4vr4xnSDxMaL',
  neutral: 'pNInz6obpgDQGcFmaJgB',
};

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

function print(msg: string) {
  console.log(msg);
}

function printHeader() {
  print('');
  print(`${c.blue}${c.bold}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓${c.reset}`);
  print(`${c.blue}${c.bold}┃${c.reset}              ${c.cyan}PAI Installation Wizard${c.reset}                       ${c.blue}${c.bold}┃${c.reset}`);
  print(`${c.blue}${c.bold}┃${c.reset}       ${c.gray}Personal AI Infrastructure v${PAI_VERSION}${c.reset}                     ${c.blue}${c.bold}┃${c.reset}`);
  print(`${c.blue}${c.bold}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${c.reset}`);
  print('');
}

function printStep(num: number, total: number, msg: string) {
  print(`${c.blue}[${num}/${total}]${c.reset} ${c.bold}${msg}${c.reset}`);
}

function printSuccess(msg: string) {
  print(`  ${c.green}✓${c.reset} ${msg}`);
}

function printWarning(msg: string) {
  print(`  ${c.yellow}!${c.reset} ${msg}`);
}

function printError(msg: string) {
  print(`  ${c.red}✗${c.reset} ${msg}`);
}

function printInfo(msg: string) {
  print(`  ${c.gray}→${c.reset} ${msg}`);
}

function getArg(args: string[], flag: string): string | null {
  const idx = args.indexOf(flag);
  if (idx !== -1 && idx + 1 < args.length) {
    return args[idx + 1];
  }
  return null;
}

// ============================================================================
// DEEP MERGE UTILITY
// ============================================================================

function deepMerge(target: any, source: any): any {
  const result = { ...target };

  for (const key of Object.keys(source)) {
    if (source[key] && typeof source[key] === 'object' && !Array.isArray(source[key])) {
      if (target[key] && typeof target[key] === 'object' && !Array.isArray(target[key])) {
        result[key] = deepMerge(target[key], source[key]);
      } else {
        result[key] = { ...source[key] };
      }
    } else {
      result[key] = source[key];
    }
  }

  return result;
}

// ============================================================================
// PERMISSIONS FIX
// ============================================================================

function fixPermissions(targetDir: string): void {
  print('');
  print(`${c.bold}Fixing permissions${c.reset}`);
  print(`${c.gray}─────────────────────────────────────────────────${c.reset}`);

  try {
    execSync(`chmod -R 755 "${targetDir}"`, { stdio: 'pipe' });
    printSuccess('Set directory permissions (755)');

    // Set executable permissions for scripts
    const executablePatterns = ['*.ts', '*.sh', '*.hook.ts'];
    for (const pattern of executablePatterns) {
      try {
        execSync(`find "${targetDir}" -name "${pattern}" -exec chmod 755 {} \\;`, { stdio: 'pipe' });
      } catch (e) {
        // Pattern might not match any files
      }
    }
    printSuccess('Set executable permissions');
  } catch (err: any) {
    printError(`Permission fix failed: ${err.message}`);
  }
}

// ============================================================================
// VOICE SERVER MANAGEMENT
// ============================================================================

function findRunningVoiceServers(): number[] {
  const pids: number[] = [];
  try {
    const result = execSync(`lsof -ti:${VOICE_SERVER_PORT} -sTCP:LISTEN`, { encoding: 'utf-8', stdio: ['pipe', 'pipe', 'pipe'] });
    const lines = result.trim().split('\n');
    for (const line of lines) {
      const pid = parseInt(line.trim());
      if (!isNaN(pid)) pids.push(pid);
    }
  } catch (e) {
    // No processes found
  }
  return pids;
}

function killVoiceServers(): void {
  const pids = findRunningVoiceServers();
  if (pids.length > 0) {
    printInfo(`Found ${pids.length} existing voice server process(es)`);
    for (const pid of pids) {
      try {
        execSync(`kill -9 ${pid}`, { stdio: 'pipe' });
        printSuccess(`Killed process ${pid}`);
      } catch (e) {
        printWarning(`Could not kill process ${pid}`);
      }
    }
  }
}

async function startVoiceServer(): Promise<boolean> {
  const serverScript = join(VOICE_SERVER_DIR, 'server.ts');

  if (!existsSync(serverScript)) {
    printWarning('Voice server script not found');
    return false;
  }

  killVoiceServers();

  try {
    const child = spawn('bun', ['run', serverScript], {
      detached: true,
      stdio: 'ignore',
      cwd: VOICE_SERVER_DIR,
    });
    child.unref();

    await new Promise(resolve => setTimeout(resolve, 2000));

    const running = findRunningVoiceServers().length > 0;
    if (running) {
      printSuccess('Voice server started');
      return true;
    } else {
      printWarning('Voice server may not have started correctly');
      return false;
    }
  } catch (err: any) {
    printError(`Failed to start voice server: ${err.message}`);
    return false;
  }
}

// ============================================================================
// CONFIG REPO FUNCTIONS
// ============================================================================

interface ConfigRepo {
  path: string;
  hasBaseSettings: boolean;
  hasMachineSettings: boolean;
  hasSkills: boolean;
  hasAgents: boolean;
  hasMemoryLearning: boolean;
  hasSrcAx: boolean;
}

function scanConfigRepo(configRepoPath: string): ConfigRepo | null {
  if (!existsSync(configRepoPath)) {
    return null;
  }

  const machineSettingsPath = join(configRepoPath, 'settings', 'machines', `${MACHINE_HOSTNAME}.json`);

  return {
    path: configRepoPath,
    hasBaseSettings: existsSync(join(configRepoPath, 'settings', 'base.json')),
    hasMachineSettings: existsSync(machineSettingsPath),
    hasSkills: existsSync(join(configRepoPath, 'skills')),
    hasAgents: existsSync(join(configRepoPath, 'agents')),
    hasMemoryLearning: existsSync(join(configRepoPath, 'MEMORY', 'LEARNING')),
    hasSrcAx: existsSync(join(configRepoPath, 'src', 'ax')),
  };
}

function mergeSettings(systemDir: string, configRepo: ConfigRepo): any {
  let settings: any = {};

  // 1. Load base settings from config repo
  if (configRepo.hasBaseSettings) {
    const basePath = join(configRepo.path, 'settings', 'base.json');
    try {
      settings = JSON.parse(readFileSync(basePath, 'utf-8'));
      printSuccess('Loaded base settings from config repo');
    } catch (e) {
      printWarning('Could not parse base.json');
    }
  }

  // 2. Load machine-specific settings
  if (configRepo.hasMachineSettings) {
    const machinePath = join(configRepo.path, 'settings', 'machines', `${MACHINE_HOSTNAME}.json`);
    try {
      const machineSettings = JSON.parse(readFileSync(machinePath, 'utf-8'));
      settings = deepMerge(settings, machineSettings);
      printSuccess(`Loaded machine settings for ${MACHINE_HOSTNAME}`);
    } catch (e) {
      printWarning(`Could not parse ${MACHINE_HOSTNAME}.json`);
    }
  }

  // 3. Set PAI_DIR to actual installation path
  if (!settings.env) settings.env = {};
  settings.env.PAI_DIR = CLAUDE_DIR;

  return settings;
}

function overlayConfigContent(targetDir: string, configRepo: ConfigRepo): void {
  print('');
  print(`${c.bold}Overlaying config repo content${c.reset}`);
  print(`${c.gray}─────────────────────────────────────────────────${c.reset}`);

  // Overlay skills (CORE/USER and personal skills like _DAILYACTIVITIES)
  if (configRepo.hasSkills) {
    const skillsDir = join(configRepo.path, 'skills');
    const entries = readdirSync(skillsDir);

    for (const entry of entries) {
      const srcPath = join(skillsDir, entry);
      const stat = statSync(srcPath);

      if (stat.isDirectory()) {
        if (entry === 'CORE') {
          // Only overlay USER subdirectory from CORE
          const userSrc = join(srcPath, 'USER');
          const userDst = join(targetDir, 'skills', 'CORE', 'USER');
          if (existsSync(userSrc)) {
            mkdirSync(userDst, { recursive: true });
            cpSync(userSrc, userDst, { recursive: true });
            printSuccess('Overlaid skills/CORE/USER');
          }
        } else if (entry.startsWith('_')) {
          // Personal skills (e.g., _DAILYACTIVITIES)
          const dstPath = join(targetDir, 'skills', entry);
          cpSync(srcPath, dstPath, { recursive: true });
          printSuccess(`Overlaid personal skill: ${entry}`);
        }
      }
    }
  }

  // Overlay agents
  if (configRepo.hasAgents) {
    const srcAgents = join(configRepo.path, 'agents');
    const dstAgents = join(targetDir, 'agents');
    mkdirSync(dstAgents, { recursive: true });
    cpSync(srcAgents, dstAgents, { recursive: true });
    printSuccess('Overlaid agents');
  }

  // Overlay MEMORY/LEARNING
  if (configRepo.hasMemoryLearning) {
    const srcLearning = join(configRepo.path, 'MEMORY', 'LEARNING');
    const dstLearning = join(targetDir, 'MEMORY', 'LEARNING');
    mkdirSync(dstLearning, { recursive: true });
    cpSync(srcLearning, dstLearning, { recursive: true });
    printSuccess('Overlaid MEMORY/LEARNING');
  }

  // Overlay src/ax
  if (configRepo.hasSrcAx) {
    const srcAx = join(configRepo.path, 'src', 'ax');
    const dstAx = join(targetDir, 'src', 'ax');
    mkdirSync(join(targetDir, 'src'), { recursive: true });
    cpSync(srcAx, dstAx, { recursive: true });
    printSuccess('Overlaid src/ax framework');
  }
}

// ============================================================================
// PAI MARKER
// ============================================================================

interface PaiMarker {
  installedAt: string;
  paiVersion: string;
  systemRepoCommit?: string;
  configRepoCommit?: string;
  hostname: string;
}

function getGitCommit(repoPath: string): string | undefined {
  try {
    return execSync(`git -C "${repoPath}" rev-parse HEAD`, { encoding: 'utf-8', stdio: ['pipe', 'pipe', 'pipe'] }).trim();
  } catch (e) {
    return undefined;
  }
}

function writePaiMarker(systemRepoPath?: string, configRepoPath?: string): void {
  const marker: PaiMarker = {
    installedAt: new Date().toISOString(),
    paiVersion: PAI_VERSION,
    hostname: MACHINE_HOSTNAME,
  };

  if (systemRepoPath) {
    marker.systemRepoCommit = getGitCommit(systemRepoPath);
  }
  if (configRepoPath) {
    marker.configRepoCommit = getGitCommit(configRepoPath);
  }

  writeFileSync(PAI_MARKER, JSON.stringify(marker, null, 2));
  printSuccess(`Written .pai-marker (v${PAI_VERSION})`);
}

function readPaiMarker(): PaiMarker | null {
  if (!existsSync(PAI_MARKER)) return null;
  try {
    return JSON.parse(readFileSync(PAI_MARKER, 'utf-8'));
  } catch (e) {
    return null;
  }
}

// ============================================================================
// SHELL ALIAS
// ============================================================================

function setupShellAlias(): void {
  const aliasLine = `alias pai='bun run ${CLAUDE_DIR}/skills/CORE/Tools/PAI.ts'`;
  const marker = '# PAI alias';
  const rcFileName = IS_ZSH ? '.zshrc' : '.bashrc';

  try {
    let shellRcContent = '';
    if (existsSync(SHELL_RC)) {
      shellRcContent = readFileSync(SHELL_RC, 'utf-8');
    }

    if (shellRcContent.includes('alias pai=')) {
      const lines = shellRcContent.split('\n');
      const updated = lines.map(line => {
        if (line.includes('alias pai=')) {
          return `${marker}\n${aliasLine}`;
        }
        return line;
      });
      writeFileSync(SHELL_RC, updated.join('\n'));
      printSuccess(`Updated PAI alias in ${rcFileName}`);
    } else {
      const addition = `\n${marker}\n${aliasLine}\n`;
      appendFileSync(SHELL_RC, addition);
      printSuccess(`Added PAI alias to ${rcFileName}`);
    }

    printInfo(`Run "source ~/${rcFileName}" or restart terminal to use "pai" command`);
  } catch (err: any) {
    printWarning(`Could not update ${rcFileName}: ${err.message}`);
    printInfo(`Add manually: ${aliasLine}`);
  }
}

// ============================================================================
// VALIDATION
// ============================================================================

interface ValidationResult {
  passed: boolean;
  checks: Array<{ name: string; passed: boolean; message: string }>;
}

function validateInstallation(targetDir: string): ValidationResult {
  const result: ValidationResult = { passed: true, checks: [] };

  // Check settings.json
  const settingsPath = join(targetDir, 'settings.json');
  if (existsSync(settingsPath)) {
    try {
      const settings = JSON.parse(readFileSync(settingsPath, 'utf-8'));
      if (settings.principal?.name && settings.daidentity?.name) {
        result.checks.push({ name: 'settings.json', passed: true, message: 'Valid configuration' });
      } else {
        result.checks.push({ name: 'settings.json', passed: false, message: 'Missing required fields' });
        result.passed = false;
      }
    } catch (e) {
      result.checks.push({ name: 'settings.json', passed: false, message: 'Invalid JSON' });
      result.passed = false;
    }
  } else {
    result.checks.push({ name: 'settings.json', passed: false, message: 'File not found' });
    result.passed = false;
  }

  // Check required directories
  const requiredDirs = ['skills', 'MEMORY', 'hooks'];
  for (const dir of requiredDirs) {
    const dirPath = join(targetDir, dir);
    if (existsSync(dirPath)) {
      result.checks.push({ name: `Directory: ${dir}`, passed: true, message: 'Exists' });
    } else {
      result.checks.push({ name: `Directory: ${dir}`, passed: false, message: 'Missing' });
      result.passed = false;
    }
  }

  // Check CORE skill
  const coreSkill = join(targetDir, 'skills', 'CORE', 'SKILL.md');
  if (existsSync(coreSkill)) {
    result.checks.push({ name: 'CORE skill', passed: true, message: 'SKILL.md found' });
  } else {
    result.checks.push({ name: 'CORE skill', passed: false, message: 'SKILL.md not found' });
    result.passed = false;
  }

  // Check .pai-marker
  const marker = readPaiMarker();
  if (marker) {
    result.checks.push({ name: '.pai-marker', passed: true, message: `v${marker.paiVersion} installed at ${marker.installedAt.split('T')[0]}` });
  } else {
    result.checks.push({ name: '.pai-marker', passed: false, message: 'Not found' });
  }

  return result;
}

function printValidationResults(results: ValidationResult): void {
  print('');
  print(`${c.bold}Validation Results${c.reset}`);
  print(`${c.gray}─────────────────────────────────────────────────${c.reset}`);

  for (const check of results.checks) {
    if (check.passed) {
      printSuccess(`${check.name}: ${check.message}`);
    } else {
      printError(`${check.name}: ${check.message}`);
    }
  }

  print('');
  if (results.passed) {
    print(`${c.green}${c.bold}✓ Installation validated successfully${c.reset}`);
  } else {
    print(`${c.red}${c.bold}✗ Installation validation failed${c.reset}`);
  }
}

// ============================================================================
// MAIN INSTALLATION FLOW
// ============================================================================

async function main(): Promise<void> {
  const args = process.argv.slice(2);

  printHeader();

  // --setup mode: just fix permissions and start voice server
  if (args.includes('--setup')) {
    printStep(1, 2, 'Fixing permissions');
    fixPermissions(CLAUDE_DIR);

    printStep(2, 2, 'Starting voice server');
    await startVoiceServer();

    print('');
    print(`${c.green}${c.bold}Setup complete!${c.reset}`);
    process.exit(0);
  }

  // --validate mode
  if (args.includes('--validate')) {
    const results = validateInstallation(CLAUDE_DIR);
    printValidationResults(results);
    process.exit(results.passed ? 0 : 1);
  }

  // Get the script's directory (this is the system repo)
  const scriptDir = import.meta.dir;
  const systemRepoPath = scriptDir;

  // Check for --config-repo flag
  const configRepoPath = getArg(args, '--config-repo');
  let configRepo: ConfigRepo | null = null;

  if (configRepoPath) {
    configRepo = scanConfigRepo(configRepoPath);
    if (configRepo) {
      print(`${c.cyan}Config repo detected:${c.reset} ${configRepoPath}`);
      printInfo(`Base settings: ${configRepo.hasBaseSettings ? 'Yes' : 'No'}`);
      printInfo(`Machine settings (${MACHINE_HOSTNAME}): ${configRepo.hasMachineSettings ? 'Yes' : 'No'}`);
      printInfo(`Personal skills: ${configRepo.hasSkills ? 'Yes' : 'No'}`);
      printInfo(`Agents: ${configRepo.hasAgents ? 'Yes' : 'No'}`);
      printInfo(`MEMORY/LEARNING: ${configRepo.hasMemoryLearning ? 'Yes' : 'No'}`);
      printInfo(`src/ax: ${configRepo.hasSrcAx ? 'Yes' : 'No'}`);
    } else {
      printWarning(`Config repo not found at ${configRepoPath}`);
    }
  }

  // ================================================================
  // Step 1: Prepare target directory
  // ================================================================
  printStep(1, 6, 'Preparing installation');

  if (!existsSync(CLAUDE_DIR)) {
    mkdirSync(CLAUDE_DIR, { recursive: true });
    printSuccess('Created ~/.claude directory');
  } else {
    printInfo('~/.claude directory exists');
  }

  // ================================================================
  // Step 2: Copy system files from this repo
  // ================================================================
  printStep(2, 6, 'Installing system files');

  // Copy core directories from system repo
  const systemDirs = ['skills', 'hooks', 'MEMORY', 'VoiceServer', 'bin', 'agents'];
  for (const dir of systemDirs) {
    const srcDir = join(systemRepoPath, dir);
    const dstDir = join(CLAUDE_DIR, dir);

    if (existsSync(srcDir)) {
      mkdirSync(dstDir, { recursive: true });
      cpSync(srcDir, dstDir, { recursive: true });
      printSuccess(`Installed ${dir}/`);
    }
  }

  // Copy individual files
  const systemFiles = ['statusline-command.sh', 'CLAUDE.md', 'PAI.md'];
  for (const file of systemFiles) {
    const srcFile = join(systemRepoPath, file);
    if (existsSync(srcFile)) {
      cpSync(srcFile, join(CLAUDE_DIR, file));
      printSuccess(`Installed ${file}`);
    }
  }

  // ================================================================
  // Step 3: Overlay config repo content (if provided)
  // ================================================================
  if (configRepo) {
    printStep(3, 6, 'Overlaying config content');
    overlayConfigContent(CLAUDE_DIR, configRepo);
  } else {
    printStep(3, 6, 'Config overlay (skipped - no config repo)');
    printInfo('Use --config-repo PATH to overlay personal config');
  }

  // ================================================================
  // Step 4: Generate settings.json
  // ================================================================
  printStep(4, 6, 'Generating settings');

  let settings: any;

  if (configRepo) {
    settings = mergeSettings(CLAUDE_DIR, configRepo);
  } else {
    // Fallback: use existing settings.json or create minimal
    const existingSettings = join(CLAUDE_DIR, 'settings.json');
    if (existsSync(existingSettings)) {
      try {
        settings = JSON.parse(readFileSync(existingSettings, 'utf-8'));
        printInfo('Using existing settings.json');
      } catch (e) {
        settings = {};
      }
    } else {
      settings = {
        paiVersion: PAI_VERSION,
        env: { PAI_DIR: CLAUDE_DIR },
        principal: { name: 'User', timezone: Intl.DateTimeFormat().resolvedOptions().timeZone },
        daidentity: { name: 'PAI', fullName: 'PAI - Personal AI' },
      };
      printInfo('Created minimal settings.json');
    }
  }

  // Ensure version is set
  settings.paiVersion = PAI_VERSION;

  writeFileSync(join(CLAUDE_DIR, 'settings.json'), JSON.stringify(settings, null, 2));
  printSuccess('Written settings.json');

  // ================================================================
  // Step 5: Write marker and fix permissions
  // ================================================================
  printStep(5, 6, 'Finalizing installation');

  writePaiMarker(systemRepoPath, configRepoPath || undefined);
  fixPermissions(CLAUDE_DIR);
  setupShellAlias();

  // ================================================================
  // Step 6: Validate
  // ================================================================
  printStep(6, 6, 'Validating installation');

  const results = validateInstallation(CLAUDE_DIR);
  printValidationResults(results);

  if (results.passed) {
    print('');
    print(`${c.blue}${c.bold}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓${c.reset}`);
    print(`${c.blue}${c.bold}┃${c.reset}                                                               ${c.blue}${c.bold}┃${c.reset}`);
    print(`${c.blue}${c.bold}┃${c.reset}   ${c.green}${c.bold}PAI v${PAI_VERSION} installed successfully!${c.reset}                         ${c.blue}${c.bold}┃${c.reset}`);
    print(`${c.blue}${c.bold}┃${c.reset}                                                               ${c.blue}${c.bold}┃${c.reset}`);
    print(`${c.blue}${c.bold}┃${c.reset}   ${c.cyan}Next steps:${c.reset}                                                 ${c.blue}${c.bold}┃${c.reset}`);
    const rcFile = IS_ZSH ? '.zshrc' : '.bashrc';
    print(`${c.blue}${c.bold}┃${c.reset}   1. Run ${c.green}source ~/${rcFile}${c.reset} to enable 'pai' command          ${c.blue}${c.bold}┃${c.reset}`);
    print(`${c.blue}${c.bold}┃${c.reset}   2. Run ${c.green}pai${c.reset} or ${c.green}claude${c.reset} in any directory to start        ${c.blue}${c.bold}┃${c.reset}`);
    print(`${c.blue}${c.bold}┃${c.reset}                                                               ${c.blue}${c.bold}┃${c.reset}`);
    print(`${c.blue}${c.bold}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛${c.reset}`);
    print('');
  }

  process.exit(results.passed ? 0 : 1);
}

// Run
main().catch((err) => {
  console.error(`${c.red}Error:${c.reset}`, err.message);
  process.exit(1);
});
