# idea-scout 🎯

**Free video ideas for YouTubers that are built from proof, not from a blank AI chat.**
Works in any AI agent (Claude Code, ChatGPT, Gemini, Cursor, Codex…). Learns your channel, finds videos that blew up
10x their channel's subscribers or its average views, and turns their psychology into specific ideas for *you*: with hooks, titles, a thumbnail concept and a score.
It remembers you between sessions.

> Ask an AI for "10 viral video ideas" and you get the same 10 ideas as everyone else.
> This skill starts from 5 real outliers, filters through *your* channel, and checks every idea before you see it.

## What you get
For each top idea:
- the **angle** (specific, not a topic) and the **outlier** it borrows from (link + "51x its subscribers"), with **why that
  outlier worked**: what was observed (its hook, packaging, comments) kept apart from what's only a hypothesis, with evidence
- a **3-second hook** (first words + first frame) and a **30-second hook** for long videos
- **3 titles** (one search-friendly, from real YouTube autocomplete) and a **thumbnail concept**
- a **score /30** (proof, fit, originality, demand, packaging, feasibility) and why it could flop
- a check that **you haven't made it already**

See a real run: [`examples/bitframe-2026-11.md`](examples/bitframe-2026-11.md).

## How it works
1. **Learns you:** your niche, audience, formats, past videos (hits and flops vs your median), how you come up with ideas.
   Starting from zero? It helps you choose a **viral niche** or a **personal niche** and shows you 3 videos to study.
2. **Finds 5 outliers:** videos with **10x more views than the channel's subscribers or its average**, from channels with
   **10,000+ subscribers**, posted recently, mostly in **adjacent niches** (so you're not copying your competitors).
3. **Explains and ideates:** for each outlier it separates what it saw from what it infers, and rules out lazy explanations
   (was it the topic or the packaging? a one-off or a habit?). Then it writes ideas from that mechanism plus proven
   techniques (contrarian takes, hidden mechanisms, challenges, series…).
4. **Checks and scores:** repeat check, free demand check, saturation, makeability.
5. **Packages** the top 3: hooks, titles, thumbnail.
6. **Remembers, privately, and shows you:** saves your profile, backlog and results in **your own private notes** (not in
   this public repo) and ends every session with a **Saved** recap: which files changed, where they live, and what to do
   first next time. Every new session in any agent starts where you left off. See [`docs/memory.md`](docs/memory.md).

## Get it: pick one (2 minutes)
The skill is public and has nothing personal in it. Your channel notes are saved separately, in a private place only you can see.

### Option 1: The Claude app (a few clicks, no terminal)
1. Download **`idea-scout.zip`** from the [latest release](https://github.com/ZStorm-7/Video-ideation/releases/latest).
2. In Claude, open **Customize → Skills** and add the ZIP.
3. Switch it on (Skills need code execution enabled in your Claude settings).
4. Start a chat and say **"run idea-scout"**.

### Option 2: Claude Code, or any AI agent with a terminal
```bash
git clone https://github.com/ZStorm-7/Video-ideation ~/.claude/skills/idea-scout
```
Then type `/idea-scout`. **Or let your AI do it:** tell it *"Install the idea-scout skill for me. Follow INSTALL.md in
https://github.com/ZStorm-7/Video-ideation"*. The agent-readable steps are in [`INSTALL.md`](INSTALL.md). Other agents
(Cursor, Codex, Gemini CLI): clone it anywhere and say *"Read SKILL.md and give me video ideas."*

### Option 3: Copy and paste into any AI chat (nothing to install)
- **Full prompt:** [`prompts/idea-scout-lite.md`](prompts/idea-scout-lite.md) holds the whole method in one box. Works in
  ChatGPT, Gemini, Claude or anything else, even with no internet. At the end it hands you a notes block to paste next time.
- **One-line prompt:** [`prompts/idea-scout-loader.md`](prompts/idea-scout-loader.md) tells an AI that can open links to load
  the latest skill from this repo.

More detail, and what each option can and can't do: [`docs/install.md`](docs/install.md).

### After you have it
1. **First run:** the skill offers to create your **private notes** (a private `idea-scout-notes` repo on GitHub, a local folder,
   or a single file if your chat can't keep files). It checks the repo is private before it saves anything.
2. Optional, free: add a YouTube Data API key to `~/.config/idea-scout/.env` for automatic channel scans and outlier
   search ([`docs/integrations.md`](docs/integrations.md)).

## Free tools included (Python 3, nothing to install)
| Tool | What | Key? |
|---|---|---|
| `tools/channel_scan.py @you` | your uploads, Shorts and long-form medians, hits and flops | free YouTube key |
| `tools/find_outliers.py --q "..."` | outliers: 10x subscribers OR 10x channel average, 10k+ subs, recent | free YouTube key |
| `tools/overlap.py --idea "..."` | "did I already make this?" (any language) | none |
| `tools/demand.py "topic"` | real YouTube autocomplete demand signal + title phrases | none |
| `tools/notes.py init / check / save` | creates your private notes repo, refuses to push it if public or if it holds a key | none |

## Other things you can ask for
Besides a full run, say: **"ideas from my backlog"**, **"score my idea: ..."**, **"find / change my niche"**, or
**"log how my video did"** (that last one is what makes the skill smarter about *you*). See `workflow/modes.md`.

## Keeping it up to date
`git pull` in the skill folder. Your notes live elsewhere, so an update never touches them
([`docs/updating.md`](docs/updating.md)).

## Repo map
`SKILL.md` (start) · `workflow/` (the 8 steps + shorter modes) · `library/` (techniques, hooks, titles, thumbnails) ·
`niches/` (tech, gaming, education, vlog, food, fitness, finance, business, beauty, travel starting packs) ·
`prompts/` (copy-paste versions) · `templates/` · `tools/` · `tests/` · `docs/` · `examples/` · `INSTALL.md` (for AI agents).
Your memory is not here: it's your private notes.

## Contributing
Niche packs, techniques, real example runs and agent reports are the most useful. See [CONTRIBUTING.md](CONTRIBUTING.md).
Made by [Bitframe](https://youtube.com/@Bit-frame). MIT licensed. If it helped you, a ⭐ helps others find it.
