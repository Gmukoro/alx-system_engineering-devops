#!/usr/bin/python3
"""Recursive function to query hot articles on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after} if after else {}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
        after = data.get("after", None)
        children = data.get("children", [])

        for child in children:
            hot_list.append(child.get("data", {}).get("title"))

        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list

    except ValueError:
        return None
