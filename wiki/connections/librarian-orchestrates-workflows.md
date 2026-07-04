---
type: connection
title: "Connection: Librarian Orchestrates Wiki Workflows"
connects:
  - "wiki/entities/librarian-agent"
  - "wiki/concepts/wiki-architecture"
  - "wiki/concepts/wiki-workflows"
sources:
  - "raw/daily/2026-07-04.md"
created: 2026-07-04
updated: 2026-07-04
---

# Connection: Librarian Orchestrates Wiki Workflows

## The Connection

The Librarian agent is not a passive tool — it is the active orchestrator that owns the full knowledge lifecycle. The three-layer architecture provides the **structure** (what exists), the workflows provide the **process** (what to do), and the Librarian provides the **agency** (who does it and validates it).

Without the Librarian, the wiki is just files on disk. Without the architecture, the Librarian has no structure to operate on. Without the workflows, the architecture sits unused.

## Key Insight

The core design insight is **delegation with validation**: the Librarian delegates specialized work to subagents but always validates results afterward. This prevents the common failure mode where automated wiki tools create orphaned, empty, or contradictory content without oversight.

The chain of trust flows:
1. User requests an action
2. Librarian delegates to the appropriate subagent
3. Subagent executes the specialized work
4. Librarian validates the results (checks for emptiness, orphan pages, broken links)
5. Librarian reports findings and asks for user approval before destructive actions

This makes the human the final decision-maker while the automation handles the heavy lifting.

## Related

- [[wiki/entities/librarian-agent|Librarian Agent]]
- [[wiki/concepts/wiki-architecture|Wiki Architecture]]
- [[wiki/concepts/wiki-workflows|Wiki Workflows]]

## Sources

- [[raw/daily/2026-07-04]] — Context of discovery
