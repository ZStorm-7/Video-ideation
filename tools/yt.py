"""Shared helpers for the optional tools (Python 3.8+, standard library only).

YouTube Data API v3 key: free (console.cloud.google.com -> enable "YouTube Data API v3" -> Credentials -> API key).
Put it in the environment as YT_API_KEY, or in a .env file next to this repo's README (git-ignored):  YT_API_KEY=...
Free quota: 10,000 units/day. A search costs 100 units; video/channel/playlist lookups cost 1.
"""
import json, os, re, statistics, sys, urllib.error, urllib.parse, urllib.request

API = 'https://www.googleapis.com/youtube/v3/'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def key():
    if os.environ.get('YT_API_KEY'): return os.environ['YT_API_KEY']
    env = os.path.join(ROOT, '.env')
    if os.path.exists(env):
        for line in open(env, encoding='utf-8'):
            k, _, v = line.strip().partition('=')
            if k.strip() == 'YT_API_KEY' and v.strip(): return v.strip().strip('"\'')
    return None

def get(ep, **q):
    k = key(); h = {'User-Agent': 'idea-scout'}
    if k: h['X-Goog-Api-Key'] = k
    url = API + ep + '?' + urllib.parse.urlencode(q)
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60))
    except urllib.error.HTTPError as e:
        sys.exit(f'YouTube Data API error {e.code}: {e.read()[:200]!r}\n'
                 'Missing or wrong key? Set YT_API_KEY (see docs/integrations.md), or use the no-key route in the workflow.')

def iso_dur(s):
    m = re.match(r'P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', s or '')
    d, h, mi, se = [int(x or 0) for x in m.groups()] if m else (0, 0, 0, 0)
    return d * 86400 + h * 3600 + mi * 60 + se

def playlist_ids(pid, limit=None):
    ids, tok = [], None
    while True:
        q = dict(part='contentDetails', playlistId=pid, maxResults=50)
        if tok: q['pageToken'] = tok
        try: r = get('playlistItems', **q)
        except SystemExit: return ids
        ids += [x['contentDetails']['videoId'] for x in r.get('items', [])]; tok = r.get('nextPageToken')
        if not tok or (limit and len(ids) >= limit): return ids[:limit] if limit else ids

def videos(ids):
    out = []
    for i in range(0, len(ids), 50):
        out += get('videos', part='snippet,statistics,contentDetails', id=','.join(ids[i:i + 50])).get('items', [])
    return out

def channel(handle=None, cid=None):
    q = {'forHandle': handle} if handle else {'id': cid}
    r = get('channels', part='snippet,statistics,contentDetails', **q).get('items') or sys.exit('channel not found')
    return r[0]

def shorts_ids(channel_id):
    """The channel's Shorts shelf playlist (UUSH...). Undocumented but widely used; empty if unavailable."""
    return set(playlist_ids('UUSH' + channel_id[2:]))

def fmt_of(v, shorts):
    d = iso_dur(v['contentDetails']['duration'])
    return 'short' if (v['id'] in shorts if shorts else d <= 180) else 'long'

def median(xs): return statistics.median(xs) if xs else 0
