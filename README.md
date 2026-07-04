# loom

**loom** is an OpenCode-adapted Memory Compiler — inspired by Karpathy's LLM Wiki pattern and coleam00's Claude Memory Compiler, rebuilt for OpenCode's agent/skill architecture.

It captures daily session logs and compiles them into a structured wiki knowledge base that persists across conversations.

## Overview

loom organizes knowledge into three layers:

```
raw/daily/         →  Immutable session logs (append-only)
wiki/              →  Compiled wiki articles (LLM-maintained)
SCHEMA.md          →  Agent instructions (co-evolved with conventions)
```

Commands are defined in `opencode.jsonc` and orchestrated by the Librarian agent:

| Command | Purpose |
|---------|---------|
| `capture` | Save today's session decisions and lessons |
| `compile` | Compile daily logs into structured wiki articles |
| `query` | Ask questions against the knowledge base |
| `lint` | Run health checks on the wiki |

## Setup

### Prerequisites

- [OpenCode](https://opencode.ai) — an AI coding assistant for the terminal

### Dependencies

- **Python 3** + `tiktoken` — required for token counting (`.opencode/scripts/count_tokens.py`)

  ```bash
  pip install tiktoken
  ```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/CyberMan-00/loom.git
   cd loom
   ```

2. The project is configured via `opencode.jsonc`. Open it and ensure the `default_agent` and skill paths match your environment.

3. (Optional) Open the vault in [Obsidian](https://obsidian.md) for a visual wiki experience — the `.obsidian/` config is included.

### Usage

Run commands in OpenCode:

- `capture` — Saves today's session to `raw/daily/YYYY-MM-DD.md`
- `compile` — Compiles new daily logs into wiki articles
- `query` — Queries the wiki knowledge base
- `lint` — Runs a health check on the wiki

## License

Apache 2.0
