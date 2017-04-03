#! /usr/bin/env python3
import praw
import os
import time
import secrets

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
MESSAGE_TEMPLATE = """Obligatory. \n 

***** \n 
I am a bot. Message me to contact my creator."""

reddit = praw.Reddit(client_id = secrets.CLIENT_ID, client_secret = secrets.CLIENT_SECRET, user_agent = USER_AGENT)

for submission in reddit.subreddit("xkcd").new(limit = 20):
    if "LFC" in submission.title:
        print("Title: ", submission.title)
        print("URL: ", submission.url)
