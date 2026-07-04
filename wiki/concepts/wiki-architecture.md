---
type: concept
title: Wiki Architecture
tags:
  - architecture
  - knowledge-base
sources:
  - raw/daily/2026-07-04.md
created: 2026-07-04
updated: 2026-07-04
---

# Wiki Architecture

The loom Memory Compiler uses a three-layer architecture inspired by Karpathy's LLM Wiki pattern.

## Three-Layer Architecture

```
┌──────────────────────────────────────────┐
│  RAW SOURCES: raw/daily/                 │
│  (conversation logs — immutable,         │
│   append-only)                           │
├──────────────────────────────────────────┤
│  THE WIKI: wiki/                         │
│  (compiled knowledge — LLM-maintained)   │
├──────────────────────────────────────────┤
│  THE SCHEMA: SCHEMA.md                   │
│  (agent instructions — co-evolved)       │
└──────────────────────────────────────────┘
```

### Layer 1: Raw Sources (`raw/daily/`)
- Immutable daily session logs in `YYYY-MM-DD.md` format
- Captured via the `capture` workflow
- Never modified after creation — only appended to
- Structured with sections: Context, Key Exchanges, Decisions Made, Lessons Learned, Action Items

### Layer 2: The Wiki (`wiki/`)
- Compiled knowledge maintained by the Librarian and its subagents
- Contains subdirectories for different article types
- Articles use `[[wikilinks]]` for cross-referencing
- Index, overview, and build log provide navigation

### Layer 3: The Schema (`SCHEMA.md`)
- Agent instructions defining conventions, templates, and workflows
- Co-evolves — updated when conventions change
- Contains article format templates for each page type

## Directory Structure

```
loom/
├── raw/
│   └── daily/              # Session logs (YYYY-MM-DD.md)
├── wiki/
│   ├── index.md            # Master catalog — all articles listed
│   ├── log.md              # Append-only build log
│   ├── overview.md         # Top-level synthesis
│   ├── concepts/           # Atomic knowledge articles
│   ├── connections/        # Cross-cutting insights
│   ├── entities/           # People, tools, projects
│   └── qa/                 # Filed query answers
├── .opencode/
│   ├── agents/             # Agent definitions
│   └── subagents/          # Specialist subagent configs
├── SCHEMA.md               # This schema layer
└── opencode.jsonc          # Command definitions
```

## Article Types

| Type | Location | Purpose |
|------|----------|---------|
| entity | `wiki/entities/` | Named things: people, organizations, tools, projects |
| concept | `wiki/concepts/` | Atomic knowledge: facts, patterns, decisions, lessons |
| connection | `wiki/connections/` | Cross-cutting insights linking 2+ concepts |
| qa | `wiki/qa/` | Filed query answers |
| overview | `wiki/overview.md` | Top-level evolving synthesis |
| catalog | `wiki/index.md` | Master catalog |
| log | `wiki/log.md` | Build log |

## Related Concepts

- [[wiki/concepts/wiki-workflows|Wiki Workflows]] — How the architecture is used day-to-day
- [[wiki/entities/librarian-agent|Librarian Agent]] — The entity that manages this architecture

## Sources

- [[raw/daily/2026-07-04]] — Context of discovery
