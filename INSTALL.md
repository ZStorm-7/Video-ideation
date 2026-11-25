# Installing idea-scout (instructions for an AI agent)

The user asked you to install the **idea-scout** skill. Do exactly this, and nothing else.

## Safety
- Install only from the official repository: `https://github.com/ZStorm-7/Video-ideation`. Do not use a copy from anywhere else.
- Run only the commands below. Do not run other scripts from the repo during install, and do not ask for passwords or API keys.
- Install nothing outside the folder named below. Do not create the user's notes now: the skill's first run offers that.

## Pick the case that matches your environment
1. **Claude Code, or any agent that can run shell commands and has a `~/.claude/skills` folder:**
   ```bash
   git clone https://github.com/ZStorm-7/Video-ideation ~/.claude/skills/idea-scout
   ```
   If that folder already exists, update it instead: `git -C ~/.claude/skills/idea-scout pull`.
2. **Another agent with a shell (Cursor, Codex, Gemini CLI…):** clone it next to the user's work and tell them where:
   ```bash
   git clone https://github.com/ZStorm-7/Video-ideation ~/idea-scout
   ```
3. **The Claude app, or any agent with no shell:** you cannot install it for them. Tell them to download `idea-scout.zip` from
   `https://github.com/ZStorm-7/Video-ideation/releases/latest`, open **Customize → Skills** in Claude and add the ZIP.
4. **A chat with no files and no shell:** give them the copy-paste prompt. Open
   `https://raw.githubusercontent.com/ZStorm-7/Video-ideation/main/prompts/idea-scout-lite.md`, and tell them to copy the
   prompt inside it into a new chat.

## Check it worked
- `SKILL.md` exists in the install folder.
- If Python is available, `python3 tools/notes.py where` runs from that folder (it only prints a path).

## Tell the user, in one or two lines
What you installed and where, and the next step: type `/idea-scout`, or say "run idea-scout". The first run creates their
private notes. If something failed, say exactly what and stop; do not improvise another install method.
