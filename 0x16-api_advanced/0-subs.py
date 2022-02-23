#!/usr/bin/python3
"""
Queries Reddit API and returns # of subs
"""

import requests


def number_of_subscribers(subreddit):

    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit))

    if r.status_code != 200:
        return 0
    else:
        return r.json()['data']['subscribers']
