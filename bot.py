#! /usr/bin/env python3
import praw
import os
import time
import secrets
from praw.exceptions import *

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
DEBUG = True

if DEBUG:
    SUB = "testingground4bots"
else:
    SUB = "xkcd"

MESSAGE_TEMPLATE = """\^\^Obligatory. \n 

***** \n 
I am a bot. Message me to contact my creator."""

reddit = praw.Reddit(client_id = secrets.CLIENT_ID,
             client_secret = secrets.CLIENT_SECRET,
             user_agent = USER_AGENT,
             username = secrets.REDDIT_USER,
             password = secrets.REDDIT_PASSWORD)

if not os.path.isfile("replied_to.txt"):
    posts_replied = []
else:
    with open("replied_to.txt", "r") as f:
        posts_replied = f.read()
        posts_replied = posts_replied.split("\n")
        posts_replied = list(filter(None, posts_replied))

for submission in reddit.subreddit(SUB).new(limit = 20):
    if "LFC" in submission.title:
        if submission.id not in posts_replied:
            submission.reply(MESSAGE_TEMPLATE)
            if DEBUG:
                print("Replied to: ", submission.id)
            posts_replied.append(submission.id)
            with open("replied_to.txt", "a") as f:
                f.write(submission.id + "\n")
        if DEBUG:
            print("Title: ", submission.title)
            print("URL: ", submission.url)
