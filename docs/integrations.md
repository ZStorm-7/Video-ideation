# Integrations (all optional)

The skill works with no keys at all: the workflow always has a manual route. These make it faster and more accurate.

| Integration | Cost | Unlocks | Setup |
|---|---|---|---|
| **YouTube Data API v3** | Free (10,000 units/day) | `channel_scan.py` (your uploads + medians), `find_outliers.py` (outliers with the 10x / 10k rules), saturation counts | console.cloud.google.com → new project → enable "YouTube Data API v3" → Credentials → Create API key → restrict it to that API. Put `YT_API_KEY=...` in `.env` (git-ignored) or your agent's environment variables. |
| **YouTube autocomplete** | Free, no key | `demand.py` demand signal + search-friendly title phrases | nothing |
| **Gemini API** | Free tier | the agent can actually *watch* public YouTube videos (yours and outliers): hooks, pacing, visuals | aistudio.google.com → Get API key → `GEMINI_API_KEY` |
| **vidIQ** (MCP/app) | Paid credits | keyword volume + competition, outlier finder, transcripts | connect it in your agent; the workflow uses it when present |
| **Web search** | Usually built into the agent | fact checks, trend checks, niche research | nothing |

Never paste keys into a chat; use `.env` or your agent's settings. `.env` is in `.gitignore`.
