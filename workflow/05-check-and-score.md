# 5. Check and score

## 5a. Hard filters (drop the idea if it fails)
- **Not a repeat:** `python3 tools/overlap.py --ideas ideas.txt --past <notes>/past-videos.md --outliers <notes>/outliers.md`
  flags titles/angles too close (≥ 50 % word overlap) to the creator's own videos or to the 5 outliers' topics. No tool?
  Compare by hand against `<notes>/past-videos.md`.
- **Makeable:** fits the creator's constraints (time, budget, on camera or not, skills).
- **Safe:** nothing misleading, harmful or against YouTube's policies; no other creator's content reused.

## 5b. Signals (free)
- **Demand:** `python3 tools/demand.py "how does ram work"` reads YouTube search autocomplete (free, no key): if the topic
  completes into several searches, people look for it. Note the top suggestions; they're also title ideas.
  vidIQ keyword volume/competition is an optional upgrade.
- **Saturation:** how many videos on this exact angle were posted in the last 7 days (Shorts) / 30 days (long)? Search
  YouTube by upload date, or `tools/find_outliers.py --count --q "angle"` with a key. Many recent copies = saturated.

## 5c. Score each idea /30 (template: `templates/scorecard.md`)
| Criterion (0-5) | 5 means |
|---|---|
| **Proof** | borrows a clear outlier psychology (10x+, recent, same format) |
| **Fit** | perfect for this creator's audience, niche and strengths (profile) |
| **Originality** | nobody (including the creator) did this angle recently; passes the "anyone test" |
| **Demand** | people search for it (autocomplete/volume) or it rides a live trend |
| **Packaging** | the title + thumbnail are obvious and make you need to click (write them first: if you can't, it's weak) |
| **Feasibility** | the creator can make it well this week |
Weights by goal (from the profile): growth → Proof and Packaging ×1.5; search/evergreen → Demand ×1.5; brand → Fit and
Originality ×1.5. At profile level 3+, adjust weights to what `<notes>/feedback.md` shows worked.

## 5d. Rank
Keep the top 3-5. For each, name its 2 strongest criteria and its weakest (and how to fix it). Everything else goes to
the backlog with its score.
