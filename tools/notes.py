#!/usr/bin/env python3
"""Your private notes repo: the skill's memory of YOU, kept apart from this public skill. Standard library + git only.

    python3 tools/notes.py where                          # where the notes live, and whether they exist yet
    python3 tools/notes.py init [--path DIR] [--import OLD_DIR]   # create them (templates, .gitignore, git init)
    python3 tools/notes.py check                          # safe to push? (public remote? keys in the files?)
    python3 tools/notes.py save "what changed"            # check, commit, push

Location: $IDEA_SCOUT_NOTES, else ~/idea-scout-notes. Make the GitHub repo PRIVATE; `check` and `save` refuse to push
if GitHub says the remote is public or if a file looks like it contains an API key.
"""
import argparse, os, re, shutil, subprocess, sys, urllib.error, urllib.request
import yt

TEMPLATES = {'profile.md': 'creator-profile.md', 'past-videos.md': 'past-videos.md', 'outliers.md': 'outliers.md',
             'backlog.md': 'backlog.md', 'feedback.md': 'feedback.md', 'session-log.md': 'session-log.md'}
SECRETS = [('Google/YouTube API key', r'AIza[0-9A-Za-z_\-]{35}'), ('GitHub token', r'(?:ghp|gho|ghs|github_pat)_[0-9A-Za-z_]{20,}'),
           ('API secret key', r'sk-[0-9A-Za-z_\-]{20,}'), ('private key', r'-----BEGIN [A-Z ]*PRIVATE KEY-----'),
           ('key assignment', r'(?i)\b(?:YT_API_KEY|GEMINI_API_KEY|API_KEY|TOKEN|SECRET)\s*=\s*[^\s#]{8,}')]

def git(path, *args, check=False):
    return subprocess.run(['git', '-C', path, *args], capture_output=True, text=True, check=check)

def remote_url(path):
    r = git(path, 'remote', 'get-url', 'origin')
    return r.stdout.strip() if r.returncode == 0 else ''

def github_repo(url):
    """'https://github.com/o/r(.git)' or 'git@github.com:o/r(.git)' -> ('o', 'r'); anything else -> None."""
    m = re.search(r'github\.com[:/]+([^/\s]+)/([^/\s]+?)(?:\.git)?/?$', url)
    return (m.group(1), m.group(2)) if m else None

def public_via_git(owner, repo):
    """Second opinion that doesn't use GitHub's rate-limited API: can git read the repo with NO credentials?
    True = yes (public), False = it asked for a login or said not found (private or missing), None = can't tell."""
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0', GIT_ASKPASS='true', GIT_CONFIG_NOSYSTEM='1')
    try:
        r = subprocess.run(['git', '-c', 'credential.helper=', 'ls-remote', '--exit-code', '--heads', f'https://github.com/{owner}/{repo}.git'],
                           capture_output=True, text=True, timeout=30, env=env)
    except Exception:
        return None
    if r.returncode in (0, 2): return True  # 2 = reachable but no matching heads: still readable without a login
    err = (r.stderr or '').lower()
    if any(k in err for k in ('could not read username', 'authentication failed', 'repository not found', 'terminal prompts disabled')): return False
    return None

def is_public(owner, repo):
    """True if anyone can see the repo, False if not, None if we can't tell. Asks GitHub's API anonymously (404 = private or
    missing), and falls back to an anonymous `git ls-remote` when the API is rate-limited or unclear."""
    req = urllib.request.Request(f'https://api.github.com/repos/{owner}/{repo}', headers={'User-Agent': 'idea-scout'})
    try:
        urllib.request.urlopen(req, timeout=15); return True
    except urllib.error.HTTPError as e:
        if e.code == 404: return False
    except Exception:
        pass
    return public_via_git(owner, repo)

def find_secrets(path):
    """[(relative file, what it looks like)]; never returns the secret itself."""
    found = []
    for dp, dn, fn in os.walk(path):
        dn[:] = [d for d in dn if d != '.git']
        for f in fn:
            full, rel = os.path.join(dp, f), os.path.relpath(os.path.join(dp, f), path)
            if f == '.env' or f.endswith('.env'): found.append((rel, 'env file')); continue
            try:
                if os.path.getsize(full) > 2_000_000: continue
                with open(full, encoding='utf-8') as fh: text = fh.read()
            except (UnicodeDecodeError, OSError): continue
            for name, pat in SECRETS:
                if re.search(pat, text): found.append((rel, name)); break
    return found

def problems(path):
    """(errors, warnings) for the notes folder."""
    errs, warns = [], []
    if not os.path.isdir(os.path.join(path, '.git')): return [f'{path} is not a git repo: run "init" first'], []
    if os.path.realpath(path) == os.path.realpath(yt.ROOT) or os.path.realpath(path).startswith(os.path.realpath(yt.ROOT) + os.sep):
        errs.append('the notes folder is inside the public skill repo: notes must be their own private repo')
    for rel, what in find_secrets(path): errs.append(f'{rel}: looks like a {what}: remove it before saving')
    url = remote_url(path)
    if not url: warns.append('no remote yet: your notes are only on this computer (create a PRIVATE GitHub repo and add it as "origin")')
    else:
        gh = github_repo(url)
        if gh:
            pub = is_public(*gh)
            if pub is True: errs.append(f'{gh[0]}/{gh[1]} is PUBLIC on GitHub: anyone can read your channel notes. Make it private: Settings → Danger Zone → Change visibility')
            elif pub is None: warns.append('could not check whether the GitHub repo is private (offline or rate-limited): verify it yourself')
        else: warns.append(f'remote {url} is not on GitHub: make sure it is private')
    return errs, warns

def cmd_where(a):
    p = yt.notes_dir(); print(p); print('exists' if os.path.isdir(p) else 'not created yet: run "init"')
    if os.path.isdir(p) and remote_url(p): print('remote:', remote_url(p))

def cmd_init(a):
    p = os.path.abspath(os.path.expanduser(a.path)) if a.path else yt.notes_dir()
    os.makedirs(p, exist_ok=True)
    for dest, src in TEMPLATES.items():
        if not os.path.exists(os.path.join(p, dest)): shutil.copy(os.path.join(yt.ROOT, 'templates', src), os.path.join(p, dest))
    for name in ('README.md', '.gitignore'):
        if not os.path.exists(os.path.join(p, name)): shutil.copy(os.path.join(yt.ROOT, 'templates', 'notes-repo', name), os.path.join(p, name))
    if a.import_from:  # legacy: a creator/ folder from an older copy of the skill
        for f in os.listdir(a.import_from):
            if f.endswith('.md') and f != 'README.md': shutil.copy(os.path.join(a.import_from, f), os.path.join(p, f))
    if not os.path.isdir(os.path.join(p, '.git')): git(p, 'init', '-b', 'main')
    print(f'notes ready at {p}')
    if p != yt.notes_dir(): print(f'tell the skill where they are:  export IDEA_SCOUT_NOTES="{p}"')
    print('next: create an empty PRIVATE repo on GitHub (github.com/new, "Private"), then:\n'
          f'  git -C "{p}" remote add origin https://github.com/<you>/idea-scout-notes.git\n'
          '  python3 tools/notes.py save "first notes"')

def cmd_check(a):
    errs, warns = problems(yt.notes_dir())
    for w in warns: print('warning:', w)
    for e in errs: print('ERROR:', e)
    if not errs: print('ok: nothing looks unsafe to save')
    return 1 if errs else 0

def cmd_save(a):
    p = yt.notes_dir()
    if cmd_check(a): print('not saved.'); return 1
    git(p, 'add', '-A')
    if git(p, 'status', '--porcelain').stdout.strip():
        c = git(p, 'commit', '-m', f'idea-scout: {a.message}')
        if c.returncode: print('commit failed:', (c.stderr or c.stdout).strip(), '\n(set git user.name and user.email if asked)'); return 1
        print('committed:', a.message)
    else: print('nothing new to commit')
    if remote_url(p):
        r = git(p, 'push', '-u', 'origin', 'HEAD')
        if r.returncode: print('push failed:', r.stderr.strip(), '\nIf the remote has newer commits: git pull --no-rebase, then save again. Never force-push.'); return 1
        print('pushed to', remote_url(p))
    return 0

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('where').set_defaults(fn=cmd_where)
    i = sub.add_parser('init'); i.add_argument('--path'); i.add_argument('--import', dest='import_from'); i.set_defaults(fn=cmd_init)
    sub.add_parser('check').set_defaults(fn=cmd_check)
    s = sub.add_parser('save'); s.add_argument('message'); s.set_defaults(fn=cmd_save)
    a = ap.parse_args(); sys.exit(a.fn(a) or 0)

if __name__ == '__main__':
    main()
