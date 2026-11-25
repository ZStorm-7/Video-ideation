# For AI agents (Codex, Cursor, Gemini CLI, Copilot, ChatGPT, any other)
This repo is a skill: plain Markdown instructions. When the user asks for video ideas, a niche, or to score an idea:
1. Read `SKILL.md` and follow it step by step (`workflow/00` → `07`).
2. Read `creator/` first; at the end of the session update it and commit + push it (`docs/memory.md`).
3. Tools in `tools/` are optional Python 3 scripts (standard library only); keys come from `.env` / environment, never the chat.
