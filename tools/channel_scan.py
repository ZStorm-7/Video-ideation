#!/usr/bin/env python3
"""Scan a creator's channel -> creator/past-videos.md (step 1). Needs a free YouTube Data API key (see tools/yt.py).

    python3 tools/channel_scan.py @yourhandle [--out creator/past-videos.md] [--limit 500]

Lists every upload (Shorts and long-form separately) with views, date, length, views vs the median of the same format,
and flags hits (>= 2x median) and flops (<= 0.5x median).
"""
import argparse, datetime as dt, os
import yt

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('handle'); ap.add_argument('--out', default=os.path.join(yt.ROOT, 'creator', 'past-videos.md')); ap.add_argument('--limit', type=int, default=500)
    a = ap.parse_args()
    ch = yt.channel(handle=a.handle if a.handle.startswith('@') else None, cid=None if a.handle.startswith('@') else a.handle)
    ids = yt.playlist_ids(ch['contentDetails']['relatedPlaylists']['uploads'], a.limit); shorts = yt.shorts_ids(ch['id'])
    rows = []
    for v in yt.videos(ids):
        f = yt.fmt_of(v, shorts)
        rows.append(dict(date=v['snippet']['publishedAt'][:10], fmt=f, title=v['snippet']['title'], views=int(v['statistics'].get('viewCount', 0)),
                         url=('https://youtube.com/shorts/' if f == 'short' else 'https://youtube.com/watch?v=') + v['id']))
    med = {f: yt.median([r['views'] for r in rows if r['fmt'] == f]) for f in ('short', 'long')}
    for r in rows:
        m = med[r['fmt']]; r['x'] = r['views'] / m if m else 0
        r['flag'] = 'hit' if r['x'] >= 2 else 'flop' if r['x'] <= 0.5 else ''
    rows.sort(key=lambda r: r['date'], reverse=True)
    subs = int(ch['statistics'].get('subscriberCount', 0))
    md = [f"# Past videos: {ch['snippet']['title']}", f"Updated: {dt.date.today()} · {subs:,} subscribers · "
          f"Shorts median: {int(med['short']):,} views ({sum(r['fmt'] == 'short' for r in rows)} Shorts) · "
          f"Long-form median: {int(med['long']):,} views ({sum(r['fmt'] == 'long' for r in rows)} long)", '',
          '| Date | Format | Title | Views | vs median | Flag | Link |', '|---|---|---|---|---|---|---|']
    md += [f"| {r['date']} | {r['fmt']} | {r['title'].replace('|', '/')} | {r['views']:,} | {r['x']:.1f}x | {r['flag']} | {r['url']} |" for r in rows]
    os.makedirs(os.path.dirname(a.out), exist_ok=True); open(a.out, 'w', encoding='utf-8').write('\n'.join(md) + '\n')
    hits = sorted((r for r in rows if r['flag'] == 'hit'), key=lambda r: -r['x'])[:5]
    print(f"{a.out}: {len(rows)} videos. Top hits: " + '; '.join(f"{r['title'][:40]} ({r['x']:.1f}x)" for r in hits))

if __name__ == '__main__':
    main()
