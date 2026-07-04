---
type: concept
title: "Wiki Workflows"
tags: [workflows, best-practices, knowledge-lifecycle]
sources:
  - "raw/daily/2026-07-04.md"
created: 2026-07-04
updated: 2026-07-04
---

# Wiki Workflows

The loom Memory Compiler has four core workflows that form a continuous knowledge lifecycle.

## The Knowledge Lifecycle

```
Working Session
      │
      ▼
  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │ CAPTURE  │ ──► │ COMPILE  │ ──► │  QUERY   │ ──► │  LINT    │
  │ raw/daily│     │ wiki/    │     │ wiki/qa/ │     │ health   │
  └──────────┘     └──────────┘     └──────────┘     └──────────┘
      ▲                                                    │
      └────────────────────────────────────────────────────┘
```

### 1. Capture — Save Session Memory

**Purpose**: Preserve key decisions, lessons, discoveries, and action items from a work session before they're forgotten.

**How it works**: The user describes what happened; the agent structures it into the daily log template with Context, Key Exchanges, Decisions Made, Lessons Learned, and Action Items. Content is saved to `raw/daily/YYYY-MM-DD.md` with a token count.

**Best practice**: Capture immediately after productive sessions — debugging wins, design decisions, architectural discussions.

### 2. Compile — Daily Logs → Wiki Articles

**Purpose**: Distill the signal from raw logs into structured, permanently linked wiki articles.

**How it works**: The agent reads uncompiled daily logs, identifies distinct pieces of knowledge (concepts, entities, connections), then creates or updates articles in the appropriate wiki subdirectories. Prefers updating existing articles over creating near-duplicates.

**Best practice**: Compile when 2-3 logs have accumulated. Use `compile:all` for a full rebuild.

### 3. Query — Ask the Knowledge Base

**Purpose**: Get answers from accumulated knowledge with `[[wikilink]]` citations.

**How it works**: The agent reads `wiki/index.md`, identifies 3-10 relevant articles, reads them in full, and synthesizes an answer with citation links. Optionally (`--file-back`) saves the Q&A as a permanent `wiki/qa/` article.

**Best practice**: Use `query:file-back` when an answer is valuable enough to keep permanently. This compounds the knowledge base over time.

### 4. Lint — Health Check

**Purpose**: Keep the wiki navigable and healthy by finding broken links, orphan pages, sparse articles, and contradictions.

**How it works**: Runs 7 checks: broken links, orphan pages, uncompiled sources, stale articles, missing backlinks, sparse articles, contradictions. Produces a structured markdown report. Never deletes anything without approval.

**Best practice**: Run `/lint` weekly. Use `/lint:structural` for a faster free-tier check. Use `/cleanup` periodically to remove truly stale content.

## Internet-Enhanced Workflows

The Librarian can integrate web research into any step:
- **Research → Capture**: Search the web for a topic and save findings as a daily log
- **Research → Compile**: Fetch documentation and compile it directly into concept articles
- **Research → Query**: Answer questions using both wiki knowledge and web sources

## Commands Reference

| Command | Alias | What it does |
|---------|-------|-------------|
| `/capture` | `save session` | Save today's session to daily log |
| `/compile` | — | Compile new daily logs into wiki articles |
| `/compile:all` | — | Force recompile all daily logs |
| `/query` | `search` / `ask` | Ask a question against the wiki |
| `/query:file-back` | — | Query and save answer to wiki/qa/ |
| `/lint` | `check` / `health` | Run all 7 health checks |
| `/lint:structural` | — | Run structural checks only (free) |
| `/cleanup` | `prune` | Scan for empty/stale articles and ask for removal |

## Related Concepts

- [[wiki/concepts/wiki-architecture|Wiki Architecture]] — The system these workflows operate on
- [[wiki/entities/librarian-agent|Librarian Agent]] — The entity that orchestrates these workflows

## Sources

- [[raw/daily/2026-07-04]] — Context of discovery
