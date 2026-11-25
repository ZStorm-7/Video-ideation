# Memory: how the skill remembers you across sessions and agents

AI sessions forget. This skill doesn't, because everything it learns about you lives in your copy of this repo, in
`creator/`, and is committed to GitHub after every session. Any agent that opens the repo next time (Claude Code,
ChatGPT with the repo, Gemini CLI, Cursor, Codex…) reads `creator/` first and continues.

## Set it up once (2 minutes)
1. On GitHub: **Use this template → Create a new repository**, choose **Private** (your channel notes stay yours).
2. Give your agent access to that repo (clone it, or connect GitHub in your agent).
3. Say "run idea-scout" (or "read SKILL.md and give me video ideas").

## What the agent does at the end of every session
```
git add creator/
git commit -m "idea-scout: 2026-11-24 profile depth 2, 12 ideas, chose #1"
git push
```
If the agent can't push (no git access), it gives you the changed files and tells you which to replace and commit.

## Rules for agents
- Read `creator/session-log.md` first: the last line says what's next.
- Only write inside `creator/` during normal use. Never commit API keys, `.env`, or anything private the creator didn't
  ask to save.
- Small, dated commits; one per session. If a push is rejected because the remote changed, pull and merge, never force.
- If two people share a repo (a team), add the person's name to each session-log line.
