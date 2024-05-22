#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Python/requests"}
    params = {"limit": 10}

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            print("None")
            return

        try:
            data = response.json().get("data")
            if not data or not data.get("children"):
                print("None")
                return

            for post in data.get("children", []):
                print(post.get("data", {}).get("title"))
        except (ValueError, KeyError):
            print("None")
    except requests.RequestException:
        print("None")
