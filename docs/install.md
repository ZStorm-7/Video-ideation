# Install idea-scout

Pick the one that matches where you use AI. All of them are free.

| You use | Steps | What you get |
|---|---|---|
| **The Claude app** (claude.ai, desktop, phone) | 4 clicks, below | the full method; your notes are one file you keep |
| **Claude Code** (terminal or IDE) | 1 command, below | everything: tools run, notes save to a private repo automatically |
| **Another agent** (Cursor, Codex, Gemini CLI…) | clone the repo, say "Read SKILL.md and give me video ideas" | the method; tools if the agent can run Python |
| **Any AI chat, nothing to install** (ChatGPT, Gemini…) | paste `prompts/idea-scout-lite.md` (full) or `prompts/idea-scout-loader.md` (one line, needs web access) | the method; no tools, notes come back as a block you save |
| **Let your AI install it** | tell it "Install the idea-scout skill for me. Follow INSTALL.md in https://github.com/ZStorm-7/Video-ideation" | the right option for its environment, done for you where it can |

## The Claude app (no terminal)
1. Download **`idea-scout.zip`** from the [latest release](https://github.com/ZStorm-7/Video-ideation/releases/latest).
2. In Claude, open **Customize → Skills** and add the ZIP (follow the on-screen prompt; the ZIP already has the layout Claude asks for).
3. Switch the skill on. Skills need **code execution** enabled in your Claude settings.
4. Start a chat and say **"run idea-scout"**.

Things to know in the app:
- **Notes:** the app may not keep files between chats. The skill handles this by giving you one file, `idea-scout-notes.md`,
  at the end of each session. Save it, and attach it at the start of the next one (or keep it in a Claude Project's files).
  It's yours alone, so it's private by default.
- **Internet:** whether the skill's helper scripts can reach YouTube depends on your Claude's network settings. If they can't,
  it uses web search and asks you to paste a few numbers instead (every step has a manual route). This is slower, not broken.
- **Plans:** the Claude help page says Skills are available on Free, Pro, Max, Ultra, Team and Enterprise plans, with code
  execution enabled.

## Claude Code
```bash
git clone https://github.com/ZStorm-7/Video-ideation ~/.claude/skills/idea-scout
```
Then type `/idea-scout`. On the first run it offers to create your private notes repo (`docs/memory.md`). Update later with
`git -C ~/.claude/skills/idea-scout pull` (`docs/updating.md`).

## Optional, free: a YouTube API key
Lets the skill scan your channel and search outliers automatically. Not needed to start (`docs/integrations.md`).
