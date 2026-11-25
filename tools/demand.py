#!/usr/bin/env python3
"""Free demand check (step 5b): YouTube search autocomplete for a topic. No key, no account.

    python3 tools/demand.py "how does ram work" ["another topic" ...] [--lang en] [--country US]

If a phrase completes into many YouTube searches, people are looking for it; the completions are also ready-made
search-friendly title phrases. This is a signal, not a search-volume number (vidIQ / keyword tools give volumes).
"""
import argparse, json, string, urllib.parse, urllib.request

def suggest(q, hl='en', gl='US'):
    url = 'https://suggestqueries.google.com/complete/search?' + urllib.parse.urlencode(dict(client='firefox', ds='yt', q=q, hl=hl, gl=gl))
    raw = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'idea-scout'}), timeout=20).read()
    return json.loads(raw.decode('utf-8', 'replace'))[1]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('topics', nargs='+'); ap.add_argument('--lang', default='en'); ap.add_argument('--country', default='US'); ap.add_argument('--deep', action='store_true', help='also try "<topic> a..z"')
    a = ap.parse_args()
    for t in a.topics:
        s = suggest(t, a.lang, a.country); deep = set()
        if a.deep:
            for ch in string.ascii_lowercase[:12]: deep.update(suggest(f'{t} {ch}', a.lang, a.country))
        n = len(s); level = 'strong' if n >= 8 else 'some' if n >= 3 else 'weak / none'
        print(f'\n"{t}": {n} completions -> demand signal: {level}' + (f' (+{len(deep)} deeper phrases)' if deep else ''))
        for x in s[:10]: print('   ', x)

if __name__ == '__main__':
    main()
