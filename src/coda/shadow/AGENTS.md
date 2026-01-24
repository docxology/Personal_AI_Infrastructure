# Coda Shadow Module - Agent Guide

## Purpose

Enable **local-first discovery** of Coda documents. Agents search local shadow files (~50ms) instead of cloud API calls, then deep-fetch from Coda only when needed.

## Key Entry Points

| Task | Component |
|------|-----------|
| Sync docs to local | `ShadowSync` |
| Search locally | `shadow_search()` |
| Index management | `ShadowIndex` |
| Configuration | `ShadowConfig` |

## Agent Workflow Pattern

```python
from pathlib import Path
from coda.shadow import ShadowConfig, ShadowSync, shadow_search

# 1. Configure once
config = ShadowConfig(
    shadow_dir=Path.home() / ".pai/coda_shadows",
    doc_ids=["NDxZHneeIw"]  # PAI Doc Controller
)

# 2. Sync periodically
ShadowSync(config).run()

# 3. Search locally FIRST (Cartographer's Oath)
results = shadow_search(config.shadow_dir, "infrastructure")
for r in results:
    print(f"{r.page_name}: {r.browser_link}")

# 4. Only fetch from Coda API when target identified
from coda import CodaPagesClient
if results:
    page = CodaPagesClient().get_page(results[0].coda_doc_id, results[0].coda_page_id)
```

## The Cartographer's Oath

> **NEVER read cloud page content without checking local Shadows first.**

This prevents expensive API "fishing expeditions" that:
- Hit Coda rate limits
- Add unnecessary latency
- Waste quota on exploration

## Shadow File Format

```yaml
---
coda_doc_id: "NDxZHneeIw"
coda_page_id: "canvas-abc123"
page_name: "Architecture"
browser_link: "https://coda.io/d/..."
---
```

## Related

- [README.md](./README.md) - Full documentation
- [../AGENTS.md](../AGENTS.md) - Main Coda agent guide
