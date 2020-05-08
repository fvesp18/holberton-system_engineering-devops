#!/usr/bin/python3
""" Queries Reddit API and returns number of subs """
import json
import requests

def number_of_subscribers(subreddit):
    end = "https://reddit.com/r/{}/about.json".format(
                            subreddit)
    subs = requests.get(end, headers={"User-agent": "another-one"}).json()
    if subreddit is None:
        return(0)
    try:
        count = subs["data"]["subscribers"]
        return(count)
    except KeyError:
        return(0)
