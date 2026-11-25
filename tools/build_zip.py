#!/usr/bin/env python3
"""Build idea-scout.zip: the one-file install for the Claude app (Customize > Skills > upload). Standard library + git only.

    python3 tools/build_zip.py [--out idea-scout.zip]

The ZIP has the skill folder as its root (idea-scout/SKILL.md ...), contains only what the skill needs (no tests, CI files or
contributor docs), and is checked against the Claude app's limits first: name <= 64 characters and equal to the folder name,
description <= 200 characters. A release workflow attaches this ZIP to every GitHub release, so people can click to download it.
"""
import argparse, os, re, subprocess, sys, zipfile
import yt

EXCLUDE = ('tests/', '.github/', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'CLAUDE.md', '.gitignore')
MAX_NAME, MAX_DESC = 64, 200

def frontmatter(path):
    with open(path, encoding='utf-8') as f: text = f.read()
    fm = text.split('---')[1] if text.startswith('---') else ''
    name, desc = re.search(r'(?m)^name: (.*)$', fm), re.search(r'(?m)^description: (.*)$', fm)
    return (name.group(1).strip() if name else ''), (desc.group(1).strip() if desc else '')

def problems(root=yt.ROOT):
    name, desc = frontmatter(os.path.join(root, 'SKILL.md'))
    out = []
    if not name or len(name) > MAX_NAME: out.append(f'name must be 1-{MAX_NAME} characters (got {len(name)})')
    if not desc or len(desc) > MAX_DESC: out.append(f'description must be 1-{MAX_DESC} characters for the Claude app (got {len(desc)})')
    if ': ' in desc or ' #' in desc: out.append('description contains ": " or " #", which breaks the YAML frontmatter: reword it')
    return name, out

def files(root=yt.ROOT):
    listed = subprocess.check_output(['git', '-C', root, 'ls-files'], text=True).split('\n')
    return [f for f in listed if f and not f.startswith(EXCLUDE) and f not in EXCLUDE]

def build(out, root=yt.ROOT):
    name, errs = problems(root)
    if errs: sys.exit('not built: ' + '; '.join(errs))
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in files(root): z.write(os.path.join(root, f), f'{name}/{f}')
    return name

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', default='idea-scout.zip'); a = ap.parse_args()
    name = build(a.out)
    print(f'{a.out}: {len(files())} files, {os.path.getsize(a.out) // 1024} KB, skill folder "{name}/"')

if __name__ == '__main__':
    main()
