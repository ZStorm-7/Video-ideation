# 3. Find 5 real outliers

An outlier is a video that did far better than its channel normally does. It's proof that an idea, angle or package
works with real people. Ideas start here, not in a blank chat.

## The rules (all of them)
- **Big enough channel:** the channel has **at least 10,000 subscribers** (tiny channels spike by luck).
- **Outlier ratio:** views ≥ **10× the channel's subscribers** AND/OR views ≥ **10× the channel's average views** (its
  last 10-20 videos of the same format). Say which rule(s) it passes.
- **Recent:** Shorts published in the last **7 days**; long-form in the last **30 days** (widen to 90 if the niche is slow,
  and say so).
- **Same format:** Shorts outliers for Shorts ideas, long-form for long-form.
- **Where to look:** mostly an **adjacent niche** (people who want the same thing your audience wants, e.g. for a coding
  channel: science explainers, productivity, gaming tech). Copying your own niche's hits makes you second best. Max 2 of
  the 5 from your own niche, and never their topic.
- **5 videos, at least 3 different channels.**

## Where to start searching
Read the creator's pack in `niches/` if there is one: its "adjacent niches" and "search keywords" are your first queries.
Always add the audience's language and country (`--lang`, `--region`) so you find outliers they could actually watch.
Run 3-5 queries across at least 2 adjacent niches before judging the results; one query is not a search.

## How (free first)
- **YouTube Data API key (free):** `python3 tools/find_outliers.py --q "keyword" --q "keyword 2" --format short --days 7 --lang en --save <notes>/outliers.md`
  → prints candidates that pass the rules (ratio, 10k minimum, recency) and appends picks to `<notes>/outliers.md`.
- **No key:** search YouTube (filter: upload date, sort by view count) or browse the adjacent channels; for each candidate
  note views, subscribers (and the channel's typical views from its Videos/Shorts tab); keep only those that pass.
  vidIQ's outlier finder, TikTok and Reddit work too (TikTok/Reddit only as inspiration, the 5 must be YouTube).
- Get each outlier's **transcript** (description → Show transcript) and note the **thumbnail and title**.

## Explain why each one worked (evidence, not vibes)
An outlier proves an outcome happened. It does not prove *why*. So for each of the 5, write a breakdown and label every
claim, so the creator can tell what you saw from what you are guessing:
- **Observed:** something you can point to: the exact first words, the thumbnail's subject and text, the title, the
  structure with timestamps, the numbers, what commenters say. Anyone could check it.
- **Hypothesis:** your explanation of why it worked, with **Confidence** (high / medium / low) and the **Evidence** for it.
  If you have no evidence, write "unknown". Never present a guess as a finding.

Look through these five lenses, and note the evidence for each:
1. **Promise:** what the viewer wanted, and whether people search for it (`tools/demand.py`).
2. **Hook:** the first 3 seconds, and the first 30 seconds of a long video: words, and what is on screen.
3. **Packaging:** the title pattern, and the thumbnail (subject, text, colour).
4. **Structure:** pacing, open loops, how early the first payoff comes (from the transcript).
5. **Context:** timing or a trend, the channel's own pull, the length, and what the top comments say.

Rule out the lazy explanations before you trust a hypothesis:
- **Topic or packaging?** Find the channel's other videos on the same topic. If they did not spike, the topic was not the
  reason: look at the angle and the packaging.
- **One-off or habit?** One big hit among flat results suggests luck or an outside push. A channel that is regularly above
  its average has a "channel effect" you cannot borrow.
- **Still climbing?** A young video may still be accelerating (views per hour), an old one has plateaued. Say which.
- **What the audience said:** the top comments often name the reason in their own words.

End each breakdown with three lines: **Borrow** (the transferable mechanism, in one sentence), **Don't borrow** (what is
specific to that channel or topic), and **How to test it** (the cheapest way the creator could check this hypothesis on their
own channel). The feedback loop (`workflow/modes.md` § D) later confirms or kills the hypotheses with the creator's own results.

## Write `<notes>/outliers.md` (template: `templates/outliers.md`)
Per outlier: link, title, channel, subscribers, views, channel average, ratio(s), date found, niche, and the breakdown
above. Outliers older than 30 days are stale: refresh them.
