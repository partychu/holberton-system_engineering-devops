#!/usr/bin/python3
"""
Queries Reddit API and returns # of subs
"""

import requests


def top_ten(subreddit):
    """ Returns number of subscribers """
    headers = {'User-Agent': 'Mozilla/5.0)'}
    url = 'http://www.reddit.com/r/{}/top.json?limit=10'.format(subreddit)
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return 0
    else:
        for post in r.json()['data']['children']:
            x = post['data']['title']
            print(x)
