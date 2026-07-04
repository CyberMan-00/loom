---
type: schema
purpose: "Agent instructions for the OpenCode Memory Compiler."
---

# SCHEMA.md — Memory Compiler for OpenCode

This document is the **schema layer** — it tells the wiki-compiler agent (and any OpenCode agent working in this vault) how the knowledge base is structured, what conventions to follow, and what workflows to execute.

Adapted from Karpathy's LLM Wiki pattern and coleam00's `claude-memory-compiler`, rebuilt for OpenCode's agent/skill architecture.

---

## Three-Layer Architecture

```
┌──────────────────────────────────────────────────────┐
│  RAW SOURCES: raw/daily/                             │
│  (conversation logs — immutable, append-only)        │
│  You write them by running the `capture` command.    │
├──────────────────────────────────────────────────────┤
│  THE WIKI: wiki/                                     │
│  (compiled knowledge — LLM-owned)                    │
│  The wiki-compiler agent creates and maintains this. │
├──────────────────────────────────────────────────────┤
│  THE SCHEMA: SCHEMA.md                               │
│  (agent instructions — co-evolved)                   │
│  Update this when conventions change.                │
└──────────────────────────────────────────────────────┘
```

## Directory Structure

```
loom/
├── raw/
│   └── daily/                       # Session logs (YYYY-MM-DD.md)
├── wiki/
│   ├── index.md                     # [LLM-maintained] Master catalog
│   ├── log.md                       # [LLM-maintained] Build log
│   ├── overview.md                  # [LLM-maintained] Top-level synthesis
│   ├── concepts/                    # [LLM-maintained] Atomic knowledge articles
│   ├── connections/                 # [LLM-maintained] Cross-cutting insights
│   ├── entities/                    # [LLM-maintained] People, tools, projects
│   └── qa/                          # [LLM-maintained] Filed query answers
├── .opencode/
│   ├── agents/
│   │   └── wiki-compiler.md         # The wiki compiler subagent
│   └── subagents/
├── .obsidian/                       # Obsidian config (do not touch)
├── SCHEMA.md                        # This file
└── opencode.jsonc                   # OpenCode command definitions
```

## Naming Conventions

- **File names**: kebab-case, no spaces (e.g., `supabase-auth.md`, `error-handling-patterns.md`)
- **Wikilinks**: Use `[[wiki/concepts/name|Name]]` or `[[wiki/entities/name|Name]]` format
- **Dates**: ISO 8601 (YYYY-MM-DD for dates, full ISO for timestamps in log.md)
- **Frontmatter**: Every wiki page must have YAML frontmatter with at minimum: `type`, `title`, `updated`, `description`, `sources`

### Page Types

| Type | Location | Purpose |
|------|----------|---------|
| `entity` | `wiki/entities/` | Named things: people, organizations, tools, projects |
| `concept` | `wiki/concepts/` | Atomic knowledge: facts, patterns, decisions, lessons learned |
| `connection` | `wiki/connections/` | Cross-cutting insights linking 2+ concepts |
| `qa` | `wiki/qa/` | Filed query answers |
| `overview` | `wiki/overview.md` | Top-level evolving synthesis |
| `catalog` | `wiki/index.md` | Master catalog |
| `log` | `wiki/log.md` | Build log |

---

## Article Format Templates

### Concept Article (`wiki/concepts/<name>.md`)

```markdown
---
type: concept
title: "Concept Name"
tags: [domain, topic]
sources:
  - "raw/daily/YYYY-MM-DD.md"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Concept Name

[2-4 sentence core explanation]

## Key Points

- [Bullet points, each self-contained]

## Details

[Deeper explanation, encyclopedia-style]

## Related Concepts

- [[wiki/concepts/related-concept]] — How it connects

## Sources

- [[raw/daily/YYYY-MM-DD]] — Context of discovery
```

### Entity Article (`wiki/entities/<name>.md`)

```markdown
---
type: entity
title: "Entity Name"
description: "One-line description"
tags: [tag1, tag2]
sources:
  - "raw/daily/YYYY-MM-DD.md"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Entity Name

## Role & Background

## Key Details

## Connections

- [[wiki/concepts/related-concept]] — Relationship
```

### Connection Article (`wiki/connections/<name>.md`)

```markdown
---
type: connection
title: "Connection: X and Y"
connects:
  - "wiki/concepts/concept-x"
  - "wiki/concepts/concept-y"
sources:
  - "raw/daily/YYYY-MM-DD.md"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Connection: X and Y

## The Connection

[What links these concepts]

## Key Insight

[The non-obvious relationship discovered]

## Related

- [[wiki/concepts/concept-x]]
- [[wiki/concepts/concept-y]]
```

### Q&A Article (`wiki/qa/<slug>.md`)

```markdown
---
type: qa
title: "Q: Question summary"
question: "The exact question asked"
consulted:
  - "wiki/concepts/article-1"
  - "wiki/concepts/article-2"
filed: YYYY-MM-DD
---

# Q: Question Summary

## Answer

[The synthesized answer with [[wikilinks]]]

## Sources Consulted

- [[wiki/concepts/article-1]] — Why it was relevant

## Follow-Up Questions

- What about edge case X?
```

### Daily Log (`raw/daily/YYYY-MM-DD.md`)

```markdown
# Daily Log: YYYY-MM-DD

## Session (HH:MM) — Brief Title

**Context:** What I was working on.

**Key Exchanges:**
- User asked about X, assistant explained Y
- Decided to use Z approach

**Decisions Made:**
- Chose library X because...

**Lessons Learned:**
- Always do X before Y to avoid...

**Action Items:**
- [ ] Follow up on X
```

---

## Workflows

### 1. Capture — Save Session Memory

When the user runs the `capture` command (or asks you to save today's session):

1. Ask what happened in the session — key decisions, lessons, discoveries
2. Write or append to `raw/daily/YYYY-MM-DD.md` using the daily log format
3. Keep it factual and concise
4. If today's file already exists, append a new session section

### 2. Compile — Daily Logs → Wiki Articles

When the user runs the `compile` command (or asks you to compile):

1. Read `wiki/index.md` to understand current knowledge state
2. Read existing articles that may need updating
3. For each daily log that hasn't been compiled yet (or all if `--all`):
   a. Read the daily log thoroughly
   b. Identify distinct pieces of knowledge — decisions, patterns, lessons, entities
   c. For each piece:
      - If an existing concept covers this: **UPDATE** it with new info, add the source
      - If it's new: **CREATE** a new `wiki/concepts/` article
   d. If a daily log reveals a non-obvious connection between 2+ concepts: **CREATE** a `wiki/connections/` article
   e. If new named entities appear (people, tools, projects): **CREATE** `wiki/entities/` articles
4. **UPDATE** `wiki/index.md` with all new/modified entries
5. **UPDATE** `wiki/overview.md` if the overall picture has changed
6. **APPEND** to `wiki/log.md`

**Important**: A single daily log may touch 3-10 wiki articles. Prefer updating existing articles over creating near-duplicates.

### 3. Query — Ask the Knowledge Base

When the user runs the `query` command (or asks a question):

1. Read `wiki/index.md` (the master catalog)
2. Based on the question, identify 3-10 relevant articles from the index
3. Read those articles in full
4. Synthesize an answer with `[[wikilink]]` citations
5. Optionally (if `--file-back`): create a `wiki/qa/` article, update index.md and log.md

**Why this works without RAG**: At personal scale (50-500 articles), reading a structured index outperforms vector similarity. The LLM understands what the question is really asking; cosine similarity just finds similar words.

### 4. Lint — Health Check

When the user runs the `lint` command:

Run these checks and produce a markdown report:

| # | Check | What It Finds |
|---|-------|---------------|
| 1 | **Broken links** | `[[wikilinks]]` pointing to non-existent files |
| 2 | **Orphan pages** | Articles with zero inbound links from other articles |
| 3 | **Uncompiled sources** | Daily logs that haven't been compiled yet |
| 4 | **Stale articles** | Source changed since article was last compiled |
| 5 | **Missing backlinks** | A links to B but B doesn't link back to A |
| 6 | **Sparse articles** | Under 200 words, likely incomplete |
| 7 | **Contradictions** | Conflicting claims across articles |

**NEVER** delete files unilaterally — flag issues for user approval. Append results to `wiki/log.md`.

---

## Cross-Referencing Rules

- Every page should link to at least one other page via `[[wikilinks]]`
- When updating a page, scan for all other pages that reference it and update those too
- If a source contradicts an existing page, note the contradiction in both — do NOT silently overwrite

## Hard Rules

1. **NEVER** modify files in `raw/` — they are the immutable source of truth
2. **ALWAYS** update `wiki/index.md` when adding or removing a page
3. **ALWAYS** append to `wiki/log.md` after every operation
4. **NEVER** delete user content without explicit approval
5. **Co-evolve this schema** — if a convention isn't working, propose an update to SCHEMA.md
