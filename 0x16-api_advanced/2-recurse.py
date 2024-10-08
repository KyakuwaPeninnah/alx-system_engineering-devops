#!/usr/bin/python3
''' task2, Recurse it'''

import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    '''querries redit apis'''
    user_agent = {'User-agent': 'test45'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)
    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        if aft is not None:
            recurse(subreddit, hot_list, aft)
        return(hot_list)
    else:
        return(None)
