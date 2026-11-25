# idea-scout 🎯

**Free video ideas for YouTubers that are built from proof, not from a blank AI chat.**
Works in any AI agent (Claude Code, ChatGPT, Gemini, Cursor, Codex…). Learns your channel, finds videos that blew up
10x their channel's subscribers or its average views, and turns their psychology into specific ideas for *you*: with hooks, titles, a thumbnail concept and a score.
It remembers you between sessions.

> Ask an AI for "10 viral video ideas" and you get the same 10 ideas as everyone else.
> This skill starts from 5 real outliers, filters through *your* channel, and checks every idea before you see it.

## What you get
For each top idea:
- the **angle** (specific, not a topic) and the **outlier** it borrows from (link + "51x its subscribers")
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
3. **Ideates** with their psychology + proven techniques (contrarian takes, hidden mechanisms, challenges, series…).
4. **Checks and scores:** repeat check, free demand check, saturation, makeability.
5. **Packages** the top 3: hooks, titles, thumbnail.
6. **Remembers:** saves your profile, backlog and results in `creator/` and commits them, so every new session
   (any agent) starts where you left off. The more results you log, the more specific it gets.

## Install (2 minutes)
1. On [github.com/ZStorm-7/Video-ideation](https://github.com/ZStorm-7/Video-ideation) click **Use this template → Create a new repository → Private** (your channel notes stay yours).
2. Open it in your AI agent:
   - **Claude Code:** `git clone https://github.com/<you>/<your-copy> ~/.claude/skills/idea-scout`, then type `/idea-scout`.
   - **Any other agent:** open the repo and say *"Read SKILL.md and give me video ideas."*
   - **No agent?** Paste [`prompts/anti-echo-chamber.md`](prompts/anti-echo-chamber.md) into any free AI chat.
3. Optional, free: add a YouTube Data API key to `.env` for automatic channel scans and outlier search
   ([`docs/integrations.md`](docs/integrations.md)).

## Free tools included (Python 3, nothing to install)
| Tool | What | Key? |
|---|---|---|
| `tools/channel_scan.py @you` | your uploads, Shorts and long-form medians, hits and flops | free YouTube key |
| `tools/find_outliers.py --q "..."` | outliers: 10x subscribers OR 10x channel average, 10k+ subs, recent | free YouTube key |
| `tools/overlap.py --idea "..."` | "did I already make this?" | none |
| `tools/demand.py "topic"` | real YouTube autocomplete demand signal + title phrases | none |

## Repo map
`SKILL.md` (start) · `workflow/` (the 8 steps) · `library/` (techniques, hooks, titles, thumbnails) · `niches/`
(tech, gaming, education, vlog packs) · `templates/` · `creator/` (your memory) · `tools/` · `docs/` · `examples/`

## Contributing
Niche packs, techniques, real example runs and agent reports are the most useful. See [CONTRIBUTING.md](CONTRIBUTING.md).
Made by [Bitframe](https://youtube.com/@Bit-frame). MIT licensed. If it helped you, a ⭐ helps others find it.
