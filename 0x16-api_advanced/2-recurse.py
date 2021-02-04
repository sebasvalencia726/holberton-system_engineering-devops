#!/usr/bin/python3
"""recurse(subreddit, hot_list=[])"""

import requests as r


def recurse(subreddit, hot_list=[], count=0):
    """Recursive function that queries the Reddit API

    Args:
        subreddit
        hot_list

    Returns:
        returns a list containing the titles
        of all hot articles for a given subreddit, otherwise return None.
    """
    try:
        g = r.get('https://api.reddit.com/r/{}/hot'.format(subreddit),
                  headers={'user-agent':
                           'python:v3.8.5 (by /u/sebasvalencia726)'}
                  )
        g.raise_for_status()
        try:
            hot_list.append(g.json().get('data').get('children')
                            [count].get('data').get('title'))
            return recurse(subreddit, hot_list, count=count + 1)
        except IndexError:
            return hot_list
    except Exception as e:
        return None
