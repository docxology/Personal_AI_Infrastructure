# PAI System Usage Guide

Your PAI system is fully installed and verified. Here's how to use it.

## 🚀 Quick Start

### 1. Restart Claude Code

**Important:** Hooks only activate when Claude Code starts. Restart it now:

```bash
# Close Claude Code completely, then restart it
# Or if using CLI:
claude
```

When Claude Code starts, you should see:
- Tab title updates to show current project
- Session initialization messages in the console
- CORE skill context automatically loaded

### 2. Verify It's Working

In a new Claude Code session, ask:

```
"Who are you?"
```

You should get a response from "Tet" (your AI assistant) with your identity loaded from the CORE skill.

---

## 🎯 Using Skills

### Available Skills

Your system has these skills installed:

1. **CORE** - Identity, preferences, routing (auto-loaded)
2. **Prompting** - Meta-prompting and template system
3. **Agents** - Dynamic agent composition and orchestration
4. **Art** - Visual content generation
5. **CreateSkill** - Create new skills

### How Skills Work

Skills are automatically routed based on your request. Just ask naturally:

```
"Create a new agent that helps with research"
→ Routes to Agents skill

"Generate an image of a futuristic city"
→ Routes to Art skill

"Create a new skill for data analysis"
→ Routes to CreateSkill skill
```

### Manual Skill Invocation

You can also explicitly invoke skills:

```
"Use the Art skill to create a logo"
"Use the Agents skill to spawn parallel researchers"
```

---

## 🔧 Common Workflows

### Creating a New Agent

```
"Create a research agent with these traits:
- Curious and thorough
- Focuses on technical documentation
- Summarizes findings concisely"
```

The Agents skill will:
1. Create a custom agent definition
2. Generate the agent prompt
3. Spawn it for you

### Generating Visual Content

```
"Create a technical diagram showing:
- System architecture
- Data flow between components
- API boundaries"
```

The Art skill will:
1. Understand your requirements
2. Generate the image using your configured API (Replicate/Google/OpenAI)
3. Save it to your project

### Using Meta-Prompting

```
"Use the Prompting skill to create a briefing template for:
- Project kickoff meetings
- Technical reviews
- Status updates"
```

The Prompting skill will:
1. Use Handlebars templates
2. Generate structured prompts
3. Save templates for reuse

---

## 📊 Monitoring & History

### View History

All your work is automatically captured:

```bash
# View recent sessions
ls -la ~/.claude/history/sessions/

# View learnings
ls -la ~/.claude/history/learnings/

# View research
ls -la ~/.claude/history/research/
```

### Observability Dashboard

Start the observability server to see real-time activity:

```bash
cd ~/.claude/observability
./manage.sh start
```

Then open: http://localhost:4000

You'll see:
- Live agent activity
- Tool usage
- Session tracking
- Performance metrics

---

## 🔐 Security Features

### Command Validation

The security validator automatically blocks dangerous commands:

```
# This will be BLOCKED:
"Delete everything in the home directory"
→ Security validator intercepts and blocks

# This is ALLOWED:
"List files in the current directory"
→ Safe command executes normally
```

### Protected Operations

These operations are automatically protected:
- Catastrophic deletions (`rm -rf /`)
- Reverse shells
- Credential theft patterns
- Prompt injection attempts
- PAI infrastructure deletion

---

## 🎤 Voice Notifications

Voice notifications are configured with ElevenLabs.

When tasks complete, you'll hear:
- Main agent completion announcements
- Subagent completion summaries
- Task status updates

To test:
```
"Complete this task and announce when done"
```

---

## 🛠️ Tools & Utilities

### Generate Skill Index

Update the skill index after adding new skills:

```bash
bun run ~/.claude/tools/GenerateSkillIndex.ts
```

### Search Skills

Find skills by description:

```bash
bun run ~/.claude/tools/SkillSearch.ts "research"
```

### View Architecture

View your system architecture:

```bash
bun run ~/.claude/tools/PaiArchitecture.ts generate
cat ~/.claude/skills/CORE/PaiArchitecture.md
```

---

## 📝 Customization

### Update Your Identity

Edit `~/.claude/skills/CORE/SKILL.md`:
- Change AI name
- Update personality traits
- Modify response format
- Add custom preferences

### Add Contacts

Edit `~/.claude/skills/CORE/Contacts.md`:
- Add frequent contacts
- Include roles and emails
- Quick reference for your AI

### Configure Stack Preferences

Edit `~/.claude/skills/CORE/CoreStack.md`:
- Set language preferences
- Define package managers
- Configure runtime choices

---

## 🧪 Testing & Verification

### Quick Health Check

```bash
bun run docxology/scripts/setup-health-check.ts
```

### Full Verification

```bash
bun run docxology/scripts/verify-installation.ts
```

### Test Hooks

```bash
bun run docxology/scripts/test-hooks.ts
```

---

## 🎓 Example Interactions

### Example 1: Research Task

```
You: "Research the latest developments in AI safety"

System:
1. Routes to Agents skill
2. Spawns research agent with appropriate personality
3. Agent conducts research
4. Results saved to history/research/
5. Voice notification when complete
```

### Example 2: Content Creation

```
You: "Create a blog post about PAI with a header image"

System:
1. Routes to Art skill for image generation
2. Creates header image
3. Routes to content creation workflow
4. Generates blog post
5. Saves both to project
```

### Example 3: Skill Creation

```
You: "Create a new skill for code review"

System:
1. Routes to CreateSkill meta-skill
2. Prompts for skill details
3. Generates SKILL.md, workflows, tools
4. Updates skill index
5. Skill is immediately available
```

---

## 🐛 Troubleshooting

### Hooks Not Firing

1. Restart Claude Code (hooks only load on startup)
2. Check `~/.claude/settings.json` has hooks configured
3. Verify hooks exist: `ls ~/.claude/hooks/*.ts`

### Skills Not Routing

1. Regenerate skill index: `bun run ~/.claude/tools/GenerateSkillIndex.ts`
2. Check skill has proper frontmatter in SKILL.md
3. Verify skill is in `~/.claude/skills/`

### Voice Not Working

1. Check ElevenLabs API key in `~/.claude/.env`
2. Verify voice server can start: `cd ~/.claude/voice && bun run server.ts`
3. Check port 8888 is available

### History Not Capturing

1. Verify history directories exist
2. Check hooks are registered in settings.json
3. Look for errors in Claude Code console

---

## 📚 Next Steps

1. **Customize Your Identity** - Edit CORE skill to match your preferences
2. **Add Your Contacts** - Populate Contacts.md
3. **Create Custom Skills** - Use CreateSkill to build domain-specific capabilities
4. **Explore Templates** - Check Prompting skill templates
5. **Monitor Activity** - Start observability dashboard
6. **Build Workflows** - Create reusable workflows for common tasks

---

## 💡 Pro Tips

- **Use natural language** - Skills route automatically based on intent
- **Check history** - Everything is captured automatically
- **Leverage agents** - Spawn parallel agents for complex tasks
- **Customize templates** - Modify Handlebars templates for your needs
- **Monitor dashboard** - Keep observability server running for insights

---

## 🆘 Getting Help

- Run health check: `bun run docxology/scripts/setup-health-check.ts`
- Full verification: `bun run docxology/scripts/verify-installation.ts`
- Check logs: `~/.claude/history/sessions/`
- Review architecture: `~/.claude/skills/CORE/PaiArchitecture.md`

Your PAI system is ready to use! Start by restarting Claude Code and asking "Who are you?" to verify everything is working.
