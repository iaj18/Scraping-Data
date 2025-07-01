# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:04:57 2021

@author: isabe
"""

import praw
import pandas as pd

reddit = praw.Reddit(client_id='x', client_secret='x', user_agent='x')

posts = []
crypto_subreddit = reddit.subreddit('CryptoCurrencies')
for post in crypto_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'url', 'num_comments', 'body', 'created'])

about = crypto_subreddit.description
members = crypto_subreddit.subscribers

cryptoTech = reddit.subreddit('CryptoTechnology')
tech = []
for post in crypto_subreddit.hot(limit=10):
    tech.append([post.title, post.score, post.url, post.num_comments, post.selftext, post.created])
tech = pd.DataFrame(tech,columns=['title', 'score', 'url', 'num_comments', 'body', 'created'])
