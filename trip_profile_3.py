#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
import tweepy
import matplotlib.pyplot as plt
import seaborn as sb
import json


# In[35]:


consumer_key = r"QX5f1rtJNAfpF7SsWYqz08Nts"
consumer_secret = r"q9T8ACJFjonY8AAkG0ENaReZtpqoZF3kYzCqmQFrt70envXKN8"
access_token = r"2295859188-fh0fR9DMXuJX7NJNtdEpF77sg4O6iSf8YSTdObg"
access_token_secret = r"sMxWgIbqhBPYftTDJkCAcIhMd9QQZI95MJDRbZJsjlZbD" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# In[41]:


hashtag_phrase = input('Hashtag Phrase ')


# In[42]:


all_tweets_info = tweepy.Cursor(api.search, q = hashtag_phrase, tweet_mode='extended').items(200)


# In[43]:


searched_tweets = [status for status in all_tweets_info]


# In[44]:


COLS = {"tweet_id", 'tweet_created_at', "tweet_source" , 'tweet_lang' ,'tweet_hashtags', 
        "tweet_user_mentions_id", "tweet_truncated" , "tweet_full_text", "tweet_retweeted" , 
        "user_id_str" , 'user_name', 'user_screen_name', 'user_profile_description',
        'user_statuses_count' , 'user_followers_count' ,'user_friends_count', 'user_listed_count' ,
        'user_profile_created_at', 'user_verified' ,
        'user_location' , 'user_time_zone', "geo_enabled", 'user_timeline_lang' ,'geo' , 'coordinates' ,'place' 
       }

df =  pd.DataFrame(columns = COLS)


# In[45]:


df


# In[46]:


for tweet in searched_tweets: 
    df = df.append({"tweet_id" : tweet.id_str,
                    'tweet_created_at' : tweet.created_at,
                    'tweet_source' : tweet.source, 
                    'tweet_lang' : tweet.lang,
                    'tweet_hashtags' : (e['text'].encode('utf-8') for e in tweet._json['entities']['hashtags']),
                    "tweet_user_mentions_id" : (e['user_mentions'].encode('utf-8') for e in tweet._json['entities']['hashtags']),
                    "tweet_truncated" : tweet.truncated,
                    "tweet_full_text" : tweet.full_text.replace('\n',' ').encode('utf-8'),
                    "tweet_retweeted" : tweet.retweeted,
                    "user_id_str" : tweet.user.id_str, 
                    'user_name' : tweet.user.name.encode('utf-8'), 
                    'user_screen_name' : tweet.user.screen_name.encode('utf-8'),
                    'user_profile_description' : tweet.user.description.encode('utf-8'), 
                    'user_statuses_count' : tweet.user.statuses_count,
                    'user_followers_count' : tweet.user.followers_count,
                    'user_friends_count' : tweet.user.friends_count,
                    'user_listed_count' : tweet.user.listed_count,
                    'user_profile_created_at' : tweet.user.created_at,
                    'user_verified' : tweet.user.verified,  
                    'user_location' : tweet.user.location, 
                    'user_time_zone' : tweet.user.time_zone, 
                    'geo_enabled' : tweet.user.geo_enabled,
                    'user_timeline_lang' :tweet.user.lang,
                    'geo' : tweet.geo,
                    'coordinates' : tweet.coordinates,
                    'place' :tweet.place
                   }, ignore_index = True)


# In[47]:


df


# In[48]:


df.head()


# In[49]:


df.tweet_full_text


# In[51]:


df.tweet_created_at


# In[52]:


df.user_name


# In[54]:


df.describe()


# In[55]:


df.info()


# In[ ]:




