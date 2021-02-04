#!/usr/bin/python3
"""top_ten(subreddit)"""

import requests as r


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit
    """
    try:
        g = r.get('https://api.reddit.com/r/{}/hot'.format(subreddit),
                  headers={'user-agent':
                           'python:v3.8.5 (by /u/sebasvalencia726)'}
                  )
        g.raise_for_status()
        for number in range(0, 10):
            print(g.json().get('data').get('children')
                  [number].get('data').get('title'))
    except Exception as e:
        print(None)
