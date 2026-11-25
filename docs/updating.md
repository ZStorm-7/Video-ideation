# Getting updates

This skill keeps improving (new niche packs, fixes, better prompts). Your copy of it holds your private channel notes in
`creator/`, so updating means merging the new skill files in without touching `creator/`. The public repo never
changes `creator/`, so there is nothing to clash with.

## One-time setup (in your copy of the repo)
```bash
git remote add upstream https://github.com/ZStorm-7/Video-ideation.git
```

## Each time you want the latest version
```bash
git fetch upstream
git merge upstream/main
```

The very first time, git will refuse because a repo made with "Use this template" has its own history. Add the flag once:
```bash
git merge upstream/main --allow-unrelated-histories
```
If git reports a conflict, it will be in a file you edited yourself (for example a niche pack you customized). Keep your
version of anything you changed on purpose, take theirs for the rest, then `git add` the files and `git commit`.
Your `creator/` files are never in the conflict list.

Then push: `git push`.

## If you installed it as a Claude Code skill
Run the same commands inside `~/.claude/skills/idea-scout`.

## Tip for agents
If the creator asks to "update the skill", run the commands above. Don't touch `creator/`, and don't force-push.
After merging, tell the creator in one line what changed (read the new commit messages with
`git log --oneline HEAD@{1}..HEAD`).
