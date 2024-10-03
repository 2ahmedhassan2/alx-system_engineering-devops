#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for the given subreddit. If an invalid subreddit is given, return 0."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    
    try:
        # Make the request with no redirects allowed
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the status code is in the 200 range (valid response)
        if response.status_code == 200:
            # Try to extract the number of subscribers
            data = response.json().get("data", {})
            return data.get("subscribers", 0)
        else:
            return 0  # Invalid subreddit or other error
    except Exception:
        # In case of any request errors (network issues, invalid JSON, etc.)
        return 0
