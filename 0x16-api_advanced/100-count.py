#!/usr/bin/python3
"""def count_words(subreddit, word_list)"""

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


def count_words(subreddit, word_list):
    """ recursive function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords

    Args:
        subreddit
        world_list
    """
    try:
        g = r.get('https://api.reddit.com/r/{}/hot'.format(subreddit),
                  headers={'user-agent':
                           'python:v3.8.5 (by /u/sebasvalencia726)'}
                  )
        g.raise_for_status()
        the_list = recurse(subreddit)
        new_list = []
        lenght = len(word_list)
        for i in range(lenght):
            new_list.append(0)
        new_dict = dict(zip(word_list, new_list))
        res = [word for line in the_list for word in line.split()]
        for word in word_list:
            if word in res:
                new_dict[word] += 1
        if all(value == 0 for value in new_dict.values()):
            print()
        else:
            for key, val in new_dict.items():
                print('{}: {}'.format(key, val))
    except Exception as e:
        print()
