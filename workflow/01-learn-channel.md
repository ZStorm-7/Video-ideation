# 1. Learn the channel (the filter that makes ideas specific)

Goal: understand the channel well enough that your ideas couldn't be pasted onto another one. Spend real effort here
the first time; later sessions only refresh it.

## 1a. Collect the uploads (free)
- **With a YouTube Data API key** (free, see `docs/integrations.md`): `python3 tools/channel_scan.py @handle --out <notes>/past-videos.md`.
  It lists every upload (Shorts and long-form apart) with views, date, length, and views vs the format's median, and
  marks hits (≥ 2× median) and flops (≤ 0.5× median).
- **Without a key:** ask the creator to paste their video list (YouTube Studio → Content, or the channel's Videos and
  Shorts tabs: title + views + date), or browse the channel page if your agent can. Fill `templates/past-videos.md`.

## 1b. Study the content, not just the numbers
For the top 5 and bottom 3 videos of each format (and the 3 newest), learn:
- the **hook** (first sentence and first image), the **structure**, the **pacing**, the **promise** vs what's delivered;
- the **packaging** (title pattern, thumbnail: face? text? colour?);
- **comments**: what viewers asked, praised, complained about (questions in comments are free video ideas);
- the creator's **techniques and style**: how they explain, joke, open, end; recurring formats or series.
How: watch them if your agent can (Gemini can watch a public YouTube URL; vidIQ can too), otherwise read transcripts
(YouTube description → Show transcript, pasted by the creator) and look at the thumbnails.

## 1c. How they come up with ideas
**[ASK]** "How do your ideas usually start? (comments, your own life, trends, other channels, a list?) Which of your
videos are you proudest of, and which did you expect to do better?" Their process and taste are part of the profile.

## 1d. Write `<notes>/profile.md`
Use `templates/creator-profile.md`. Keep it short and concrete: niche (and sub-niche), audience (who, age range, what they
want), formats, tone, techniques, what works here (with video links + numbers), what flops here, banned topics, goals,
constraints. Show it to the creator: **[ASK]** "Is this you? Anything wrong or missing?" Fix it, then save.
