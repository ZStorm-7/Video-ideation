# Example: a real run for a small channel (Bitframe, November 2026)

A real session of this skill on the author's channel (@Bit-frame: computer-science Shorts, animated). All numbers below
are real, pulled on 2026-11-24 with the repo's tools. Ideas are the skill's output; results will be added to
`feedback` once the videos are posted.

## Before: what a blank AI chat gives
"Give me 10 viral tech Shorts ideas" → "What if the internet disappeared?", "How does Wi-Fi work?", "The history of
the computer", "5 coding tips"... the same list everyone gets. Nothing tied to this channel.

## Step 1: the channel (tools/channel_scan.py @Bit-frame)
86 subscribers · 5 Shorts (median 1,313 views) · 1 long video.
- Best: "2038 Bug: Your Computer Will Think It's 1901" (1,685 · 1.3x), "Your Phone Has No Idea Where You Are (How GPS Works)" (1,492 · 1.1x).
- Flops: music/remix edits (63-75 views · 0.0-0.1x). → lesson: the audience is here for explained tech, not edits.
Profile depth: 2/4 (profile + past videos, no feedback yet).

## Step 3: 5 outliers (tools/find_outliers.py, adjacent niches, Shorts, last 7 days, 10k+ subs)
| Title | Channel subs | Views | Ratio vs subs / vs channel avg | Psychology |
|---|---|---|---|---|
| [Why Apple Store iPhones Don't Have Security Cables](https://youtube.com/shorts/SQ-53PJXcCw) | 12,700 | 704,731 | 55x / 70x | hidden reason behind an everyday design |
| [What Happens When Sand Is Heated?](https://youtube.com/shorts/IsybjoQ6VHU) | 24,100 | 1,236,452 | 51x / 2.2x | "what happens when…" transformation you can watch |
| [99% of people don't know the truth about Bulletproof Helmets](https://youtube.com/shorts/XmtzsgUZjmQ) | 12,100 | 575,207 | 48x / 1.8x | myth the viewer believes, then the truth |
| [How to Actually Survive a Tsunami](https://youtube.com/shorts/6-qcl5Iwqyk) | 16,900 | 2,399,285 | 142x / 1.6x | survival stakes + steps in order |
| [Hydraulic Power Steering System Explained](https://youtube.com/shorts/fflHGjR54U0) | 58,000 | 809,155 | 14x / 5.6x | the hidden mechanism inside something you use |

## After: the top 3 (checked, scored, packaged)
### 1. The first 60 seconds after your account gets hacked · 25/30
- Borrows: the tsunami video's survival stakes + ordered steps. Technique: stakes story + you-focused.
- Demand (autocomplete): strong, 10 completions ("what to do if your account gets hacked on roblox / instagram / discord…").
- Hook (Short): "Your account just got hacked." · frame 1: a login alert popping up as the character's phone buzzes.
- Titles: Your Account Got Hacked: Do This First · What To Do If Your Account Gets Hacked · The First 60 Seconds After a Hack
- Thumbnail: the character frozen in front of a giant red "NEW LOGIN" alert · text: "DO THIS FIRST"
- Risk: generic advice video; fix by showing each step as a race against the hacker (a countdown).

### 2. Why your phone charges slower after 80 % · 23/30
- Borrows: the Apple security-cable video's hidden design reason. Technique: hidden mechanism.
- Demand: some (4 completions, mostly iPhone phrasing → use "iPhone" in a title).
- Hook: "Your phone is slowing down on purpose." · frame 1: a battery bar crawling at 80 %.
- Titles: Why Your iPhone Charges Slower After 80% · Your Phone Slows Charging on Purpose · The 80% Charging Secret
- Thumbnail: a battery icon at 80 % with a tiny brake pedal · text: "ON PURPOSE"
- Risk: near the channel's earlier battery video; angle is different (charging speed, not replacing) and passed the
  repeat check (25 % overlap).

### 3. 99 % of people use incognito mode wrong · 22/30
- Borrows: the bulletproof-helmet myth reveal. Technique: myth vs reality.
- Demand: some (4 completions: "what does incognito mode do", "how does incognito mode work").
- Hook: "Incognito mode doesn't hide you." · frame 1: a sneaky character in sunglasses, while three people watch.
- Titles: What Incognito Mode Actually Does · Incognito Mode Doesn't Hide You · 99% Use Incognito Mode Wrong
- Thumbnail: the character in a disguise with a giant spotlight on them · text: "THEY SEE YOU"

### Backlog (scored lower)
4. What really happens when you delete a file · 18/30 (weak demand) · 5. How your Wi-Fi knows which data is yours · 17/30 (weak demand)
