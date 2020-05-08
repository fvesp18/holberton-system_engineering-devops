#!/usr/bin/python3
""" Queries Reddit API and returns top ten hot posts """
import json
import requests


def top_ten(subreddit):
    end = "https://reddit.com/r/{}/hot.json?limit=10".format(
                            subreddit)
    posts = requests.get(end, headers={"User-agent": "another-one"}).json()
    if subreddit is None:
        print(None)
    try:
        for post in range(0, 10):
            print(posts['data']['children'][post]['data']['title'])
    except KeyError:
        print(None)
