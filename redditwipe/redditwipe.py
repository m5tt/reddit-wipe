#!/usr/bin/env python

import re
import time
import socket
import signal
import argparse
import itertools

import praw

CLIENT_ID = 'Et5pP8DWesue1w'
CLIENT_SECRET = '9pLeMTBl7rNdykNCD_Fa3YD7sOI'

TEST_URL = 'www.google.com'
USER_AGENT = 'reddit-wipe'

CONTENT_TYPE_COMMENT = 'comments'
CONTENT_TYPE_SUBMISSION = 'submissions'

COOLDOWN_COUNT = 1000       # reddit limitation
COOLDOWN_TIME = 10


def ctrl_c_exit(signum, frame):
    """
    always bothers me when ctrl c raises a bunch of exceptions for no reason
    so exit cleanly
    """

    print()
    exit(0)


def delete_content(user, exclude, item_matcher, replace_str)
    content = get_content(user, exclude)

    while len(list(content)):
        for item in content:
            if item_matcher(item):
                item.edit(replace_str)
                item.delete()
        time.sleep(COOLDOWN_TIME)
        content = get_content(user, exclude)


def get_content(user, exclude):
    if exclude == CONTENT_TYPE_COMMENT:
        content = user.submissions.new()
    elif exclude == CONTENT_TYPE_SUBMISSION:
        content = user.comments.new()
    else:
        content = itertools.chain(user.comments.new(),
                                  user.submissions.new())

    return content


def get_item_matcher(keyword, pattern):
    if (not keyword) and (not pattern):
        return lambda item: True
    elif keyword:
        return lambda item: item == keyword
    else:
        return lambda item: re.search(pattern, item)


def login():
    username = input("Username: ")
    password = input("Password: ")

    return praw.Reddit(client_id=CLIENT_ID,
                       client_secret=CLIENT_SECRET,
                       user_agent=USER_AGENT,
                       username=username,
                       password=password)


def is_connected():
    try:
        host = socket.gethostbyname(TEST_URL)
        socket.create_connection((host, 80), 4)
        return True
    except socket.error:
        return False


def get_args():
    arg_parser = argparse.ArgumentParser(description='A command line reddit content deleter')

    arg_parser.add_argument('--exclude', choices=[CONTENT_TYPE_COMMENT, CONTENT_TYPE_SUBMISSION],
                            default='', required=False, type=str, help='exclude either comments or submissions')
    arg_parser.add_argument('--replace-str', default='', required=False, type=str,
                            help='What to replace the comment body with before deleting')
    match_group = arg_parser.add_mutually_exclusive_group()
    match_group.add_argument('--keyword', default='', required=False, type=str,
                             help='Delete only comments containing a keyword')
    match_group.add_argument('--pattern', default='', required=False, type=str,
                             help='Delete only comments that match a regex pattern')

    return arg_parser.parse_args()


def main():
    signal.signal(signal.SIGINT, ctrl_c_exit)
    args = get_args()

    if is_connected():
        try:
            user = login().user.me()
            print("Logged in\n")
        except:                             # praw's exceptions are all wacked out so just do this
            print('Error: failed to login')
        else:
            item_matcher = get_item_matcher(args.keyword, args.pattern)
            delete_content(user, args.exclude, item_matcher, args.replace_str)

            print('All done')
    else:
        print('No internet connection')

if __name__ == '__main__':
    main()


