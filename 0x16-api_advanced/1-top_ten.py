#!/usr/bin/python3
"""
Queries Reddit API and returns top 10 posts
"""

import requests


def top_ten(subreddit):
    """ Returns top 10 posts """
    headers = {'User-Agent': 'Mozilla/5.0)'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        print(None)
        return
    try:
        posts = r.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    except:
        print(None)
