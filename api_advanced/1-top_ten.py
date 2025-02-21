#!/usr/bin/python3
"""
Module that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10 hot posts for a subreddit.
    If the subreddit is invalid or has no posts, prints None.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if subreddit is invalid (Reddit returns 404 for invalid subreddits)
        if response.status_code == 404:
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

