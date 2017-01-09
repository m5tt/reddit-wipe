#!/usr/bin/env python

import argparse
import itertools
import socket

import praw

CLIENT_ID = 'Et5pP8DWesue1w'
CLIENT_SECRET = '9pLeMTBl7rNdykNCD_Fa3YD7sOI'

CONTENT_TYPE_COMMENT = 'comments'
CONTENT_TYPE_SUBMISSION = 'submissions'

TEST_URL = 'www.google.com'
USER_AGENT = 'reddit-wipe'


def delete_content(content, replace_str='', match_item=None):
    for item in content:
        if match_item:
            delete_item = match_item(item)
        else:
            delete_item = True

        if delete_item:
            item.edit(replace_str)
            item.delete()


def get_content(user, exclude):
    if exclude == CONTENT_TYPE_COMMENT:
        content = user.submissions.new(limit=None)
    elif exclude == CONTENT_TYPE_SUBMISSION:
        content = user.comments.new(limit=None)
    else:
        content = itertools.chain(user.comments.new(limit=None),
                                  user.submissions.new(limit=None))

    return content


def login():
    username = input("Username: ")
    password = input("Password: ")

    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT,
                         username=username,
                         password=password)

    return reddit


def is_connected():
    try:
        host = socket.gethostbyname(TEST_URL)
        socket.create_connection((host, 80), 4)
        return True
    except socket.error:
        return False

def main():
    if is_connected():
        user = login().user.me()
        print("Logged in\n")

        content = get_content(user, '')
        delete_content(content)
    else:
        pass


if __name__ == '__main__':
    main()


