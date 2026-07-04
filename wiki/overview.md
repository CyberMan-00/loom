---
type: overview
updated: 2026-07-04
description: "Top-level evolving synthesis of the knowledge base."
sources:
  - "raw/daily/2026-07-04.md"
---

# Overview

**loom** is an **OpenCode-adapted Memory Compiler** — inspired by Karpathy's LLM Wiki pattern and coleam00's Claude Code implementation, but rebuilt for OpenCode's agent/skill architecture instead of Claude Code hooks.

## How It Works

```
OpenCode session
     │
     ├─ User runs `capture` → raw/daily/YYYY-MM-DD.md
     │
     ├─ User runs `compile` → raw/daily/ → wiki/{concepts,connections,entities}/
     │
     ├─ User runs `query`   → wiki/index.md → relevant articles → answer
     │
     └─ User runs `lint`    → health check → report
```

## Active Themes

- **Wiki architecture & workflows** — The foundational structure and lifecycle of the knowledge base is now documented
- **Librarian agent** — The orchestrator entity is defined with its subagent team and tools
- **Delegation with validation** — Core design pattern: specialized work delegated to subagents, then validated by the Librarian

## Source Count

| Source | Count |
|--------|-------|
| Daily logs | 1 |
| Web clippings | 1 |
| Concept articles | 2 |
| Connection articles | 1 |
| Entity articles | 1 |
| Q&A articles | 0 |
