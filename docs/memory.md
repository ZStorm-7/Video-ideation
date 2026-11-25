# Memory: how the skill remembers you, privately

AI sessions forget. This skill doesn't, because what it learns about your channel is saved as plain Markdown in **your own
private notes repo**. That repo is separate from this public skill, so:

- **Private for you.** The skill repo is public and holds no personal data. Your notes live in a repo only you can see.
- **Easy to reach.** It's ordinary Markdown on GitHub: read or edit it in the browser or the GitHub phone app, and any agent
  (Claude Code, ChatGPT, Gemini CLI, Cursor, Codex…) can read it next time.
- **Easy to update.** Updating the skill is a `git pull`; your notes aren't in the way.

```
the skill (public, shared)            your notes (private, only yours)
~/.claude/skills/idea-scout     <->    ~/idea-scout-notes   →  github.com/<you>/idea-scout-notes (Private)
workflow/ library/ niches/ tools/      profile.md  past-videos.md  outliers.md  backlog.md  feedback.md  session-log.md
```

## Set it up once (2 minutes)
1. Install the skill (see the README): `git clone https://github.com/ZStorm-7/Video-ideation ~/.claude/skills/idea-scout`.
2. Say "run idea-scout". On the first run it offers to create the notes for you (`workflow/00-start.md`): a **private** GitHub
   repo called `idea-scout-notes`, or a local folder if you'd rather keep everything on your computer.
3. Done. Every session it reads your notes first and saves them at the end.

By hand: `python3 tools/notes.py init`, create an empty **Private** repo at github.com/new, then
`git -C ~/idea-scout-notes remote add origin <the repo URL>` and `python3 tools/notes.py save "first notes"`.

## Where the notes live
`python3 tools/notes.py where` prints it. Order: the `IDEA_SCOUT_NOTES` environment variable, then `~/idea-scout-notes`.
Keep them somewhere else with `export IDEA_SCOUT_NOTES=/path/to/notes`. In a cloud agent (no persistent home folder), attach
your private notes repo to the session; the agent reads and writes it there.

## What protects your privacy
`tools/notes.py check` (run by `save`) refuses to push when:
- GitHub says the notes repo is **public** (it asks GitHub anonymously: if a stranger can see it, so it fails);
- a file looks like it contains an API key or token (it reports the file, never the key);
- the notes folder is inside the public skill folder.
Your own responsibility: create the repo as **Private**, and keep keys in `~/.config/idea-scout/.env` or your agent's settings.
Anyone you add as a collaborator on the notes repo can read them.

## Rules for agents
- Read `<notes>/session-log.md` first: the last line says what's next.
- Write only inside `<notes>` during normal use. Never write creator data into the skill folder, and never commit API keys.
- Save with `python3 tools/notes.py save "<message>"`: one small dated commit per session. If a push is rejected because the
  remote changed, `git pull --no-rebase` in the notes folder, then save again. Never force-push.
- If `check` fails, fix what it names. Don't work around it, and don't make the repo public to "fix" access.
- If two people share notes (a team), add the person's name to each session-log line.
