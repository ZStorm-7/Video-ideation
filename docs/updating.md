# Getting updates

This skill keeps improving (new niche packs, fixes, better prompts). Your channel notes live in a separate private repo
(`docs/memory.md`), so updating the skill can never touch them. From the skill's folder:

```bash
git pull
```

If you installed it as a Claude Code skill, that folder is `~/.claude/skills/idea-scout`:

```bash
git -C ~/.claude/skills/idea-scout pull
```

That's it. If git says you have local changes, you edited a skill file (for example a niche pack you customized): commit
your change first (`git commit -am "my edits"`) and pull again; git will merge, and only a clash on the same lines needs a
decision. Keep your version of anything you changed on purpose.

## Tip for agents
If the creator asks to "update the skill", run the command above. Don't touch the notes, and don't force-pull or reset.
Afterwards tell the creator in one line what changed: `git log --oneline HEAD@{1}..HEAD`.

## Moving from an older copy (notes inside the skill folder)
Older versions kept notes in a `creator/` folder inside your own private copy of the skill. To switch: install the skill
fresh from the public repo, then `python3 tools/notes.py init --import <path to your old creator folder>` and set up the
private notes repo as in `docs/memory.md`. Then you can archive the old private copy.
