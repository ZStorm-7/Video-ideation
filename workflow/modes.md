# Shorter modes (everything except the full run)

The menu in `SKILL.md` has five options. "New ideas" is the full run (`00` → `07`). The other four are here. Every mode
ends the same way: update `creator/` (`07-deliver-and-remember.md`, "Remember") before you stop.

## A. Ideas from my backlog
Use when `creator/backlog.md` has ideas with status `new` and the creator wants to pick from them, not start fresh.
1. Read the backlog. Drop anything that is now stale: timely ideas older than 30 days, or ideas the creator has since
   made (check `creator/past-videos.md`; run `tools/overlap.py` if it is out of date).
2. Re-check the survivors: demand (`tools/demand.py`) and saturation (05b), because both change.
3. Re-score with today's weights (05c). If `creator/feedback.md` has lessons, apply them: they outrank the defaults.
4. If `creator/outliers.md` is older than 30 days, offer to refresh it (`03`) and run the **Backlog remix** variant of
   `prompts/anti-echo-chamber.md` on the top 3, so they borrow from fresh proof.
5. Package the top 3 (`06`), deliver (`07`).

## B. Score my own idea
Use when the creator arrives with an idea they already like.
1. **[ASK]** for the idea in one or two sentences, and whether it is a Short or long-form. If it is a topic and not an
   angle (rule 3 in `SKILL.md`), say so kindly and offer 3 sharper angles on it. Let them pick, then score that.
2. Run 05a (repeat, makeable, safe) and 05b (demand, saturation).
3. Look for proof: 1-2 outlier searches on the idea's angle (`03`). If nothing close exists, say "no proof found" and cap
   Proof at 2/5. That is useful information, not a verdict: new angles are allowed, they are just riskier.
4. Score it (05c) and give a verdict: **make it** · **fix it** (name the weakest criterion and one concrete change) ·
   **drop it** (and say why in one line). Never inflate a score to be agreeable; the creator is trusting the number.
5. For "make it" and "fix it": 3 titles, a 3-second hook and a thumbnail concept (`06`). Save the idea and its score in
   the backlog.

## C. Find / change my niche
`02-find-niche.md`. If the channel already has videos, do `01-learn-channel.md` first: what exists is evidence about what
the audience wants. Save the decision in `creator/profile.md`, then offer a full run in the new niche.

## D. Log how a video did
Use when the creator comes back after posting. This is the step that makes the skill better for them over time.
1. **[ASK]** which video (link, or which backlog idea) and when it went live.
2. Timing: results under 48 hours are early signals only. Say so and offer to log the 7-day numbers later. Don't draw
   conclusions from a video that is still climbing.
3. Get the numbers: with a key, re-run `tools/channel_scan.py` to refresh views and the median; otherwise ask for views,
   CTR and average view duration from YouTube Studio (CTR and retention are optional but the most useful).
4. Append a row to `creator/feedback.md` (`templates/feedback.md`): idea, title and thumbnail used, views at 48 h / 7 d,
   vs the creator's median, CTR, average view duration, and their own verdict. Set the idea's backlog status to `made`.
5. Compare with the prediction: the idea's score against the actual result. Separate the causes when you can:
   low CTR with good retention = a good video with weak packaging; high CTR with poor retention = the title promised more
   than the video paid off; both low = the idea or the audience fit.
6. Every 3 results, update `Lessons so far` and "What works here / What flops here" in `creator/profile.md`, and adjust
   the scoring weights to match. Say plainly that 3 results are a hint, not a rule; 10+ results make a pattern.
7. Move the profile depth: 3+ results logged → level 3; 10+ → level 4 (`SKILL.md`). Tell the creator what changed.
