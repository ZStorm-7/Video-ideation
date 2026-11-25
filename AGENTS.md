# For AI agents (Codex, Cursor, Gemini CLI, Copilot, ChatGPT, any other)
This repo is a skill: plain Markdown instructions. To INSTALL it for a user, follow `INSTALL.md`. When the user asks for video ideas, a niche, or to score an idea:
1. Read `SKILL.md` and follow it step by step (`workflow/00` → `07`).
2. The creator's memory is NOT in this repo: it's their private notes repo (`python3 tools/notes.py where`). Read it first;
   at the end of the session update it and save it with `python3 tools/notes.py save "<message>"` (`docs/memory.md`).
3. Tools in `tools/` are optional Python 3 scripts (standard library only); keys come from `~/.config/idea-scout/.env` or the
   environment, never the chat and never the notes repo.
