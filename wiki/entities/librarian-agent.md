---
type: entity
title: "Librarian Agent"
description: "The Knowledge Base Steward — top-level orchestrator of the loom Memory Compiler"
tags: [agent, knowledge-management, librarian]
sources:
  - "raw/daily/2026-07-04.md"
created: 2026-07-04
updated: 2026-07-04
---

# Librarian Agent

## Role & Background

The Librarian is the primary steward of the `loom` Memory Compiler knowledge base. It owns the full lifecycle of wiki content: delegating execution to specialized subagents, validating results, flagging empty or stale documents for user approval, and keeping the wiki healthy. It never modifies `raw/` files (immutable source of truth) and never deletes anything without explicit user approval.

The Librarian is inspired by Karpathy's LLM Wiki pattern and coleam00's Memory Compiler implementation, rebuilt for OpenCode's agent/skill architecture.

## Key Details

### Core Principles

- **Delegate, don't reimplement** — All specialized work is delegated to subagents (wiki-capturer, wiki-compiler, wiki-querier, wiki-linter)
- **Validate after every action** — Post-task validation ensures content quality
- **Never modify `raw/`** — Raw daily logs are the immutable source of truth
- **Never delete without consent** — Every removal requires explicit `[y/N]` user approval
- **Structured reporting** — Findings always presented as markdown tables with exact file paths and token counts

### Tools Available

| Tool | Purpose |
|------|---------|
| **Read** | Read files and directories (articles, index, logs) |
| **Write** | Create new files (log entries, cleanup reports) |
| **Edit** | Modify existing files (update index.md, log.md) |
| **Glob** | Find files by pattern (wiki articles by directory) |
| **Grep** | Search for wikilinks across wiki pages |
| **Bash** | Run validation (wc, token count, ls, rm with approval) |
| **Task** | Delegate work to a subagent |
| **WebSearch** | Real-time web search with deep/fast modes |
| **WebFetch** | Fetch content from specific URLs |

### Internet Capabilities

The Librarian has access to real-time web search (with `"deep"` mode for comprehensive research and `"fast"` for quick results) and a web fetch tool for reading specific URLs. This enables researching new topics and incorporating web knowledge directly into the wiki workflow.

## Subagent Team

| Subagent | Role | Trigger |
|----------|------|---------|
| wiki-capturer | Session memory recorder | `capture`, `save session` |
| wiki-compiler | Daily logs → wiki articles | `compile` |
| wiki-querier | Knowledge base search & answer | `query`, `search`, `ask` |
| wiki-linter | Health check specialist | `lint`, `check`, `health` |

## Connections

- [[wiki/concepts/wiki-architecture|Wiki Architecture]] — The three-layer system the Librarian manages
- [[wiki/concepts/wiki-workflows|Wiki Workflows]] — The capture/compile/query/lint cycle the Librarian orchestrates
- [[wiki/connections/librarian-orchestrates-workflows|Connection: Librarian Orchestrates Workflows]] — How the entity drives the workflows
