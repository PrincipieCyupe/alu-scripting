#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Fetches and prints the first 10 hot post titles of a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if status code indicates failure
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data")
        if not data:
            print(None)
            return

        posts = data.get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post["data"].get("title", None))

    except Exception:
        print(None)

