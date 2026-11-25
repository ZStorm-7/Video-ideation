# 7. Deliver, save the backlog, and remember the creator

## Deliver
Show the top picks in the format of `templates/ideas-output.md`, then the rest as a ranked one-line list.
**[ASK]** "Which one will you make? Want changes to any?" Mark the chosen idea in the backlog as `in progress`.

## Remember (every session, before you stop)
Update the `creator/` folder so the next session, in any agent, starts from here:
- `creator/profile.md`: anything new you learned (and the profile depth level).
- `creator/past-videos.md`: refreshed if you scanned the channel.
- `creator/outliers.md`: the outliers used today (with the date).
- `creator/backlog.md`: every idea not chosen (score, date, status `new`), and the chosen one as `in progress`.
- `creator/feedback.md`: results the creator reported (see below).
- `creator/session-log.md`: one dated line: what you did, what was decided, what's next.

Then **save it to GitHub** so other sessions see it (see `docs/memory.md`):
1. If your agent can run git in the creator's copy of this repo: `git add creator/ && git commit -m "idea-scout: <date>
   <what changed>" && git push`. Never commit keys or `.env` files.
2. If it can't: give the creator the updated files (or a patch) and say exactly which files to replace and commit.
Tell the creator in one line what was saved.

## The feedback loop
When the creator comes back with results (**Log how a video did**), record in `creator/feedback.md`: the idea, the
title/thumbnail used, views after 48 h and 7 days, vs their median, average view duration / CTR if they share them, and
their own verdict. Every 3 results, update "what works here" in the profile and the scoring weights. This is what moves
the profile from generic to specific.
