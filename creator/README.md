# creator/ : the skill's memory of YOU

This folder is empty in the public repo. The skill fills it as it learns your channel, and commits it after every
session so the next session (in Claude, ChatGPT, Gemini, Cursor, anything) starts where the last one ended:

| File | What |
|---|---|
| `profile.md` | who you are: niche, audience, formats, tone, what works, what flops, goals, constraints |
| `past-videos.md` | your uploads with views vs your median (the overlap check + "what works here") |
| `outliers.md` | the outlier videos used for ideas, dated |
| `backlog.md` | every idea not made yet, with scores |
| `feedback.md` | how the ideas you made actually did (this is what makes it smarter) |
| `session-log.md` | one line per session |

**Privacy:** make your copy of this repo **private** if you don't want your channel notes public ("Use this template" →
Private). Never put API keys in here; they go in `.env` (git-ignored) or your agent's settings.
