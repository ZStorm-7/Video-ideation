# 7. Deliver, save the backlog, and remember the creator

## Deliver
Show the top picks in the format of `templates/ideas-output.md`, then the rest as a ranked one-line list.
**[ASK]** "Which one will you make? Want changes to any?" Mark the chosen idea in the backlog as `in progress`.

## Remember (every session, before you stop)
Update the `<notes>/` folder so the next session, in any agent, starts from here:
- `<notes>/profile.md`: anything new you learned (and the profile depth level).
- `<notes>/past-videos.md`: refreshed if you scanned the channel.
- `<notes>/outliers.md`: the outliers used today (with the date).
- `<notes>/backlog.md`: every idea not chosen (score, date, status `new`), and the chosen one as `in progress`.
- `<notes>/feedback.md`: results the creator reported (see below).
- `<notes>/session-log.md`: one dated line: what you did, what was decided, what's next.

Then **save it** so other sessions see it (see `docs/memory.md`):
1. If your agent can run commands: `python3 tools/notes.py save "<date> <what changed>"`. It checks that the repo is
   private and that no key is in the files, then commits and pushes. If it refuses, fix what it names; never bypass it.
2. If it can't run commands: give the creator the updated files and say which to replace in their notes repo.
Tell the creator in one line what was saved and where.

## The feedback loop
When the creator comes back with results (**Log how a video did**), record in `<notes>/feedback.md`: the idea, the
title/thumbnail used, views after 48 h and 7 days, vs their median, average view duration / CTR if they share them, and
their own verdict. Every 3 results, update "what works here" in the profile and the scoring weights. This is what moves
the profile from generic to specific.
