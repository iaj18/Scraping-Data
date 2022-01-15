# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:17:34 2022

@author: isabe
"""


import praw
import pandas as pd

reddit = praw.Reddit(client_id='Mb_8nBlqu5m-Nr2n87sOrQ', client_secret='M5mgO5tg4nwcOKXkYLBpcYjPF-2SIw', user_agent='WebScraping Isabel')

posts = []
forhire = reddit.subreddit('forhire')
for post in forhire.hot(limit=1000):
    posts.append([post.title, post.score, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'num_comments', 'body', 'created (Unix time)'])
#A a larger Unix time means the post is older

about = forhire.description
members = forhire.subscribers

#%%  
title = posts['title']

titles = []
forhire = []
hiring = []
for i in range(0, len(title)):
    titles.append(title[i].lower())
    
for i in range(0, len(titles)):
    if '[for hire]' in titles[i]:
        forhire.append(titles[i])
    if '[hiring]' in titles[i]:
        hiring.append(titles[i])
#%%
    
forhire_df = pd.DataFrame(forhire, columns=['title'])
hiring_df = pd.DataFrame(hiring, columns=['title'])

for i in range(0, len(posts['title'])):
    posts['title'][i] = posts['title'][i].lower()

hiringDF = hiring_df.join(posts, lsuffix='-')