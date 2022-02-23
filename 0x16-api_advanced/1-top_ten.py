#!/usr/bin/python3
"""
Queries Reddit API and returns top 10 posts
"""

import requests


def top_ten(subreddit):
    """ Returns top 10 posts """
    headers = {'User-Agent': 'Mozilla/5.0)'}
    url = 'http://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(None)
    if r.json()['data']['after'] is None:
        print(None)
    else:
        for post in r.json()['data']['children']:
            print(post['data']['title'])
