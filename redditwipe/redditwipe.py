#!/usr/bin/python

import praw

ITEMTYPE_POSTS = "posts"
ITEMTYPE_COMMENTS = "comments"
REDDIT_ACCESS_NUM = 999999999

USER_AGENT = 'reddit-wipe'


def delete_comments(reddit_user, limit_num):
    comments_deleted = 0

    for access_num in range(0, REDDIT_ACCESS_NUM):
        
        comments = reddit_user.get_comments(limit=None)

        if not any(True for _ in comments):
            print("No comments")
            break
        
        for current_comment in comments:
            current_comment.edit("Deleted")
            current_comment.delete()

            comments_deleted += 1
            print("Comment deleted")

            if comments_deleted == limit_num:
                return


def delete_posts(reddit_user, limit_num):

    posts_deleted = 0

    for access_num in range(0, REDDIT_ACCESS_NUM):

        posts = reddit_user.get_submitted(limit=None)

        if not any(True for _ in posts):
            print("No more posts")
            break

        for current_post in posts:
            if current_post.selftext:
                current_post.edit("Deleted")

            current_post.delete()
            posts_deleted += 1
            print("Post deleted")

            if posts_deleted == limit_num:
                return


def login():
    username = input("Username: ")
    password = input("Password: ")
    
    reddit = praw.Reddit(USER_AGENT)
    reddit.login(username, password, disable_warning=True)
    reddit_user = reddit.get_redditor(username)

    return reddit_user


reddit_user = login()
print("Logged in\n")

item_type = input("Delete posts or comments: ")
limit = input("Limit (leave blank for no limit): ")
limit = int(limit)


if not limit:
    limit = -1

if item_type == ITEMTYPE_COMMENTS:
    delete_comments(reddit_user, limit)
elif item_type == ITEMTYPE_POSTS:
    delete_posts(reddit_user, limit)

