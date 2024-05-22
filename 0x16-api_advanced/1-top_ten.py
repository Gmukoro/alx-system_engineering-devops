#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            print("None")
            return

        try:
            results = response.json().get("data")
            if results is None or not results.get("children"):
                print("None")
                return

            for child in results.get("children", []):
                print(child.get("data", {}).get("title"))
        except ValueError:
            print("None")
    except requests.RequestException:
        print("None")
