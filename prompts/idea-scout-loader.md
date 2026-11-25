# The short version: one line that loads the latest skill

Paste this into an AI that **can open web links** (ChatGPT with browsing, Gemini, Claude with web access, Cursor, Codex…). It
reads the skill straight from this repo, so you always get the current version. If your AI can't open links, use the
[full copy-paste prompt](idea-scout-lite.md) instead.

```
Use the idea-scout skill. Read https://raw.githubusercontent.com/ZStorm-7/Video-ideation/main/SKILL.md and follow it. It links
to other files in the same repository (workflow/, library/, niches/, templates/): open them with the same raw address as you need
them. If you can't open links, tell me and I'll paste the full prompt instead. Keep my notes private: don't ask me for
passwords or API keys, and don't save anything to a public place.
```

**Want it to stay put?** This loads whatever is on the `main` branch today. To pin a version, replace `main` in the address with
a release tag such as `v1.0.0`.

**Want your AI to install it instead?** Tell it: *"Install the idea-scout skill for me. Follow INSTALL.md in
https://github.com/ZStorm-7/Video-ideation"*.
