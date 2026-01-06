#!/bin/bash
#
# PAI Quick Start Guide
# Interactive guide to get started with your PAI system
#

echo ""
echo "🚀 PAI Quick Start"
echo "════════════════════════════════════════════════════════════"
echo ""

# Check if Claude Code is running
if pgrep -f "claude" > /dev/null; then
    echo "⚠️  Claude Code is currently running"
    echo ""
    echo "To activate all hooks and features, you need to:"
    echo "  1. Close Claude Code completely"
    echo "  2. Restart it"
    echo ""
    read -p "Press Enter when you've restarted Claude Code..."
else
    echo "✓ Claude Code is not running"
    echo ""
    echo "Start Claude Code now to activate the PAI system:"
    echo "  claude"
    echo ""
    read -p "Press Enter when Claude Code is started..."
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo "🧪 Testing Your Installation"
echo "════════════════════════════════════════════════════════════"
echo ""

echo "In your new Claude Code session, try these commands:"
echo ""
echo "1. Identity Check:"
echo "   \"Who are you?\""
echo ""
echo "2. Skill Test:"
echo "   \"What skills do you have?\""
echo ""
echo "3. Security Test (this should be BLOCKED):"
echo "   \"Run: rm -rf /tmp/test\""
echo ""
echo "4. Agent Creation:"
echo "   \"Create a research agent\""
echo ""

echo "════════════════════════════════════════════════════════════"
echo "📊 Optional: Start Observability Dashboard"
echo "════════════════════════════════════════════════════════════"
echo ""

read -p "Start observability dashboard? (y/N) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    PAI_DIR="${PAI_DIR:-$HOME/.claude}"
    if [ -f "$PAI_DIR/observability/manage.sh" ]; then
        echo "Starting observability server..."
        cd "$PAI_DIR/observability"
        ./manage.sh start
        echo ""
        echo "✓ Dashboard available at: http://localhost:4000"
    else
        echo "⚠️  Observability server not found"
    fi
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo "✅ You're Ready!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Your PAI system is active. Check docs/USAGE.md for detailed guides."
echo ""
echo "Quick commands:"
echo "  bun run docxology/scripts/setup-health-check.ts    # Health check"
echo "  bun run docxology/scripts/verify-installation.ts  # Full verification"
echo "  bun run docxology/scripts/test-hooks.ts           # Test hooks"
echo ""
