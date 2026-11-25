#!/usr/bin/env python3
"""Find outlier videos (step 3). Needs a free YouTube Data API key (see tools/yt.py).

    python3 tools/find_outliers.py --q "how computers work" --q "science explained" --format short --days 7
    python3 tools/find_outliers.py --q "how computers work" --format long --days 30 --save <notes>/outliers.md
    python3 tools/find_outliers.py --count --q "exact angle" --days 7        # saturation: recent uploads on an angle

Rules: channel >= 10,000 subscribers; views >= 10x subscribers and/or >= 10x the channel's average views (its last 15
videos of the same format); published within --days; same format. Quota: each --q costs ~100 units (+ ~3 per channel
for the average), well inside the free 10,000/day.
"""
import argparse, datetime as dt, os
import yt

MIN_SUBS, RATIO = 10_000, 10.0

def search(q, days, fmt, pages=1, lang=None, region=None):
    after = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%SZ'); ids, tok = [], None
    for _ in range(pages):
        kw = dict(part='id', q=q, type='video', order='viewCount', publishedAfter=after, maxResults=50, videoDuration='short' if fmt == 'short' else 'medium')
        if lang: kw['relevanceLanguage'] = lang
        if region: kw['regionCode'] = region
        if tok: kw['pageToken'] = tok
        r = yt.get('search', **kw); ids += [i['id']['videoId'] for i in r.get('items', [])]; tok = r.get('nextPageToken')
        if not tok: break
    return ids

def channel_stats(cids, fmt):
    out = {}
    for i in range(0, len(cids), 50):
        for c in yt.get('channels', part='statistics,contentDetails', id=','.join(cids[i:i + 50])).get('items', []):
            st = c['statistics']; subs = None if st.get('hiddenSubscriberCount') else int(st.get('subscriberCount', 0))
            avg = None
            if subs and subs >= MIN_SUBS:  # only spend quota on channels that can qualify
                vs = yt.videos(yt.playlist_ids(c['contentDetails']['relatedPlaylists']['uploads'], 40))
                xs = [int(v['statistics'].get('viewCount', 0)) for v in vs if (yt.iso_dur(v['contentDetails']['duration']) <= 180) == (fmt == 'short')][:15]
                avg = sum(xs) / len(xs) if len(xs) >= 3 else None
            out[c['id']] = (subs, avg)
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--q', action='append', required=True); ap.add_argument('--format', choices=['short', 'long'], default='short')
    ap.add_argument('--days', type=int); ap.add_argument('--save'); ap.add_argument('--count', action='store_true')
    ap.add_argument('--lang', default='en', help='audience language (relevanceLanguage), e.g. en, es, hi'); ap.add_argument('--region', help='e.g. US, GB, IN'); a = ap.parse_args()
    days = a.days or (7 if a.format == 'short' else 30)
    if a.count:
        for q in a.q:
            n = len(search(q, days, a.format, pages=2, lang=a.lang, region=a.region)); print(f'{n}{"+" if n >= 100 else ""} uploads matching "{q}" in the last {days} days (a sample: treat as a lower bound)')
        return
    rows, seen = [], set()
    for q in a.q:
        vs = [v for v in yt.videos(search(q, days, a.format, lang=a.lang, region=a.region)) if (yt.iso_dur(v['contentDetails']['duration']) <= 180) == (a.format == 'short')]
        cs = channel_stats(sorted({v['snippet']['channelId'] for v in vs}), a.format)
        for v in vs:
            subs, avg = cs.get(v['snippet']['channelId'], (None, None)); views = int(v['statistics'].get('viewCount', 0))
            if not subs or subs < MIN_SUBS or v['id'] in seen: continue
            rs, ra = views / subs, (views / avg if avg else 0)
            if rs >= RATIO or ra >= RATIO:
                seen.add(v['id']); rows.append(dict(id=v['id'], title=v['snippet']['title'], ch=v['snippet']['channelTitle'], subs=subs, views=views, avg=avg,
                                                    rs=rs, ra=ra, date=v['snippet']['publishedAt'][:10], fmt=a.format, q=q))
    rows.sort(key=lambda r: -max(r['rs'], r['ra']))
    url = lambda r: ('https://youtube.com/shorts/' if r['fmt'] == 'short' else 'https://youtube.com/watch?v=') + r['id']
    for r in rows[:25]:
        print(f"subs {r['rs']:5.1f}x {'✓' if r['rs'] >= RATIO else ' '} avg {r['ra']:5.1f}x {'✓' if r['ra'] >= RATIO else ' '}  {r['views']:>11,} views  {r['subs']:>9,} subs  {r['date']}  {r['title'][:50]}  {url(r)}")
    if not rows: print('No outliers passed the rules (>= 10k subs, >= 10x). Try adjacent-niche keywords or more --days.')
    if a.save and rows:
        new = not os.path.exists(a.save); os.makedirs(os.path.dirname(a.save) or '.', exist_ok=True)
        with open(a.save, 'a', encoding='utf-8') as f:
            if new: f.write('# Outliers\n\n| Found | Format | Title + link | Channel | Subs | Views | Channel avg | Ratio (subs / avg) | Niche |\n|---|---|---|---|---|---|---|---|---|\n')
            for r in rows[:10]:
                f.write(f"| {dt.date.today()} | {r['fmt']} | [{r['title'].replace('|', '/')}]({url(r)}) | {r['ch']} | {r['subs']:,} | {r['views']:,} | {int(r['avg'] or 0):,} | {r['rs']:.1f}x / {r['ra']:.1f}x | {r['q']} |\n")
        print('appended the top 10 to', a.save, '(keep the best 5, from at least 3 channels)')

if __name__ == '__main__':
    main()
