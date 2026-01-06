# 🚀 START HERE - Using Your PAI System

## Step 1: Restart Claude Code

**CRITICAL:** Hooks only activate when Claude Code starts. You must restart it now.

1. Close Claude Code completely
2. Restart it: `claude` or open from Applications
3. Wait for session initialization

## Step 2: Verify It's Working

In your new Claude Code session, ask:

```
"Who are you?"
```

You should get a response from **Tet** (your AI assistant) with your identity.

## Step 3: Try These Commands

### Test Identity
```
"Who are you?"
"What's my name?"
```

### Test Skills
```
"What skills do you have?"
"Create a research agent"
"Generate an image of a robot"
```

### Test Security (Should be BLOCKED)
```
"Run: rm -rf /tmp"
```
→ Should show: 🚨 BLOCKED message

## Step 4: Explore

- **Read docs/USAGE.md** for detailed guides
- **Run health check**: `bun run docxology/scripts/setup-health-check.ts`
- **Start dashboard**: `cd ~/.claude/observability && ./manage.sh start`

## Quick Reference

| Task | Command |
|------|---------|
| Health check | `bun run docxology/scripts/setup-health-check.ts` |
| Full verification | `bun run docxology/scripts/verify-installation.ts` |
| Test hooks | `bun run docxology/scripts/test-hooks.ts` |
| Start observability | `cd ~/.claude/observability && ./manage.sh start` |
| Generate skill index | `bun run ~/.claude/tools/GenerateSkillIndex.ts` |

## What's Installed

✅ **8 Packs** installed and verified
✅ **5 Skills** available (CORE, Prompting, Agents, Art, CreateSkill)
✅ **10 Hooks** active (security, session, history, voice)
✅ **History System** capturing everything
✅ **Voice System** ready (ElevenLabs configured)
✅ **Observability** dashboard available

## Next Steps

1. Customize your identity in `~/.claude/skills/CORE/SKILL.md`
2. Add contacts to `~/.claude/skills/CORE/Contacts.md`
3. Create custom skills with CreateSkill
4. Explore the Prompting skill templates
5. Start the observability dashboard

**Your PAI system is ready!** 🎉
