# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:04:57 2021

@author: isabe
"""

import praw
import pandas as pd

reddit = praw.Reddit(client_id='Mb_8nBlqu5m-Nr2n87sOrQ', client_secret='M5mgO5tg4nwcOKXkYLBpcYjPF-2SIw', user_agent='WebScraping Isabel')

posts = []
crypto_subreddit = reddit.subreddit('CryptoCurrencies')
for post in crypto_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'url', 'num_comments', 'body', 'created'])

about = crypto_subreddit.description
members = crypto_subreddit.subscribers