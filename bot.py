#! /usr/bin/env python3
import praw
import os
import time
import datetime
import secrets
from praw.exceptions import *

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
DEBUG = False

if DEBUG:
    SUB = "testingground4bots"
else:
    SUB = "xkcd"

MESSAGE_TEMPLATE = """\^\^Obligatory. \n 

***** \n 
I am a bot. Message me to contact my creator. \n

I am open source. [Fork me on Github](https://github.com/BlitzKraft/AreYouSureItsNotSMBC)
"""

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

while(True):
    for submission in reddit.subreddit(SUB).new(limit = 20):
        if "LFC" in submission.title:
            if submission.id not in posts_replied:
                try:
                    submission.reply(MESSAGE_TEMPLATE)
                except APIException as e:
                    with open("auto_smbc_bot.log","a") as f:
                        f.write('{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()) + ": API Exception. Probably a rate limit\n");
                if DEBUG:
                    print("Replied to: ", submission.id)
                posts_replied.append(submission.id)
                with open("replied_to.txt", "a") as f:
                    f.write(submission.id + "\n")
            if DEBUG:
                print("Title: ", submission.title)
                print("URL: ", submission.url)
    time.sleep(900)
