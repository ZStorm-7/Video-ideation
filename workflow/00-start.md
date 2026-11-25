# 0. Start: where are the notes, and who is this creator?

## 0a. Find or create the private notes (every session)
`<notes>` is the creator's **private notes repo**, a separate folder from this public skill. Find it: `python3
tools/notes.py where` (it checks `$IDEA_SCOUT_NOTES`, then `~/idea-scout-notes`); in a cloud agent, it's the repository
attached to the session named like `idea-scout-notes`. If it exists, skip to 0b.

If it doesn't, this is a first run. Say in one line: "I keep what I learn about your channel in a private notes repo that
only you can see, so every session starts where the last one ended." Then **[ASK]** where:

- **A private GitHub repo (recommended).** Syncs between your devices and agents, and you can read it on your phone.
  1. `python3 tools/notes.py init` creates the folder with the starter files.
  2. Create the repo: if the `gh` CLI is installed, run `gh repo create idea-scout-notes --private --source
     "$(python3 tools/notes.py where | head -1)" --remote origin`. Otherwise tell the creator: github.com/new → name it
     `idea-scout-notes` → choose **Private** → Create, then run `git -C <that folder> remote add origin <the repo URL>`.
     In a cloud agent: they create the private repo, then attach it to the session.
  3. `python3 tools/notes.py check` must say ok. It confirms with GitHub that the repo is not public and that no key is
     in the files; it refuses to push otherwise.
- **A local folder only.** Nothing leaves the computer. Fine to start with; the notes won't follow them to another device.
  Run `init` and skip the GitHub steps.

If a `creator/` folder exists in an older copy of the skill, move it over: `python3 tools/notes.py init --import
<old creator folder>`. Never write creator data into the skill's own folder.

## 0b. Who is this creator?
**[ASK]** "Do you already have a YouTube channel with videos on it?"
- **Yes** → ask for the channel link or @handle. Go to `01-learn-channel.md`.
- **Yes, but I want to change direction** → do `01-learn-channel.md` first (what exists is evidence), then `02-find-niche.md`.
- **No, I'm starting out** → `02-find-niche.md`, then come back to `01-learn-channel.md` to write the profile from their answers.

Also ask once (save in `<notes>/profile.md`):
- **Format:** Shorts, long-form, or both? (Shorts and long videos are judged separately everywhere in this skill.)
- **Goal for the next 3 months:** subscribers, views, money, a portfolio, fun? (It changes the scoring weights.)
- **Constraints:** how many videos a week, what they can actually produce (face on camera? animation? voiceover only?
  budget?). An idea they can't make is a bad idea.
- **Language and region** of the audience.

If `<notes>/` already has files, skip what's known and only ask what's missing or out of date (older than 30 days for
past videos and outliers).
