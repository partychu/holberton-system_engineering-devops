#!/usr/bin/python3
"""
Queries Reddit API and returns # of subs
"""

import requests


def number_of_subscribers(subreddit):
    """ Returns number of subscribers """
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0)'
    }
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return 0
    else:
        return r.json()['data']['subscribers']
