#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns the
number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    :param subreddit: The subreddit to query
    :return: The number of subscribers or 0 if the subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; AcmeInc/1.0)"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, TypeError, ValueError):
            return 0
    else:
        return 0

