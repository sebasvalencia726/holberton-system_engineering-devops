#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
for a given subreddit"""

import requests as r


def number_of_subscribers(subreddit):
    """function that queries the Reddit API

    Args:
        subreddit

    Returns:
        number of subscribers for a given subreddit
    """
    try:
        g = r.get('https://api.reddit.com/r/{}/about'.format(subreddit),
                  headers={'user-agent':
                           'python:v3.8.5 (by /u/sebasvalencia726)'}
                  )
        g.raise_for_status()
        return g.json().get('data').get('subscribers')
    except Exception as e:
        return 0
