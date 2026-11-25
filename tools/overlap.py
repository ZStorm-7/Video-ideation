#!/usr/bin/env python3
"""Repeat check (step 5a): flags ideas too close to the creator's past videos or the outliers' topics. No key needed.

    python3 tools/overlap.py --ideas ideas.txt [--past creator/past-videos.md] [--outliers creator/outliers.md] [--threshold 0.5]
    python3 tools/overlap.py --idea "Why your Wi-Fi is slower upstairs"

ideas.txt: one idea (angle or working title) per line. Similarity = share of the idea's meaningful words (stop words
removed, simple stemming, hyphens joined) shared with the other title, measured both ways; >= threshold = flagged.
"""
import argparse, os, re
import yt

STOP = set("""a an the and or but so to of in on at for with from by as is are was were be it its this that these those i you he she we they
my your our their do does did have has had not no what when where who why how which if up out into about all any some one two three
very really just than then there here can will would could should vs versus explained explain""".split())

def words(t):
    t = re.sub(r"(\w)[-_.](\w)", r"\1\2", t.lower())  # wi-fi -> wifi, e-mail -> email
    return {re.sub(r"(ing|ed|es|s)$", '', w) for w in re.findall(r"[a-z0-9']+", t) if w not in STOP and len(w) > 2}

def titles(md):
    if not md or not os.path.exists(md): return []
    out = []
    for line in open(md, encoding='utf-8'):
        cells = [c.strip() for c in line.split('|')]
        if len(cells) > 4 and not set(cells[1]) <= set('-: ') and cells[1].lower() not in ('date', 'found'):
            t = next((c for c in cells if len(c) > 12 and not c.startswith('http') and not re.fullmatch(r'[\d,.x /]+', c)), '')
            t = re.sub(r'\]\(.*?\)', '', t).strip('[]')
            if t: out.append(t)
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--ideas'); ap.add_argument('--idea', action='append', default=[])
    ap.add_argument('--past', default=os.path.join(yt.ROOT, 'creator', 'past-videos.md')); ap.add_argument('--outliers', default=os.path.join(yt.ROOT, 'creator', 'outliers.md'))
    ap.add_argument('--threshold', type=float, default=0.5); a = ap.parse_args()
    ideas = a.idea + ([l.strip() for l in open(a.ideas, encoding='utf-8') if l.strip()] if a.ideas else [])
    refs = [('your video', t) for t in titles(a.past)] + [('outlier', t) for t in titles(a.outliers)]
    if not refs: print('(no past videos / outliers found: nothing to compare against)')
    for idea in ideas:
        iw = words(idea)  # similarity both ways: an idea that contains a whole past title is a repeat even with extra words
        best = max(((max(len(iw & words(t)) / max(1, len(iw)), len(iw & words(t)) / max(1, len(words(t)))), src, t) for src, t in refs), default=(0, '', ''))
        tag = 'REPEAT?' if best[0] >= a.threshold else 'ok'
        print(f"{tag:8} {best[0]:4.0%}  {idea[:70]}" + (f"   ~ {best[1]}: {best[2][:60]}" if best[0] >= a.threshold else ''))

if __name__ == '__main__':
    main()
