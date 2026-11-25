# Contributing

Thanks for helping creators get better ideas. Good first contributions:
- **A niche pack** (`niches/<niche>.md` from `niches/_template.md`): where outliers hide, what works, what's overdone.
  Most packs are unverified starting hypotheses. The best contribution is to *verify* one: run the outlier search, fix
  what's wrong, and change its Status line to "verified <date> from N outliers".
- **A technique or hook** for `library/` with a real example (link the video).
- **An example run** in `examples/` (your channel, real numbers, before/after; remove anything private). We have one,
  from a tech channel. Runs in food, fitness, finance, beauty, gaming or non-English channels are the most wanted.
- **A tool fix** in `tools/` (Python 3, standard library only, no new dependencies). Add or update a test in `tests/`
  and run `python3 -m unittest discover -s tests`; tests must work offline with no API key.
- **Agent compatibility**: tell us which agent you used and what broke (issue template "Agent report").

Rules
- Keep everything agent-neutral Markdown; tool-specific steps go in `docs/integrations.md`.
- Never commit keys, `.env`, or anyone's private channel data. `creator/` stays empty in this repo.
- Claims about YouTube need a source (`docs/why-it-works.md`) or are labelled as opinion.
- One topic per pull request; describe what you tested.

Be kind: see CODE_OF_CONDUCT.md.
