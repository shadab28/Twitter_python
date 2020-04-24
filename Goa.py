#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import csv
import io
#python 2 compatibility 
import tweepy
#twitter api, needs authentication 
import re
#regular expressions library 

consumer_key = r"QX5f1rtJNAfpF7SsWYqz08Nts"
consumer_secret = r"q9T8ACJFjonY8AAkG0ENaReZtpqoZF3kYzCqmQFrt70envXKN8"
access_token = r"2295859188-fh0fR9DMXuJX7NJNtdEpF77sg4O6iSf8YSTdObg"
access_token_secret = r"sMxWgIbqhBPYftTDJkCAcIhMd9QQZI95MJDRbZJsjlZbD"


# In[2]:


#function 
def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    #auth - is an object here ,
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth) #api is also an object 
    
    """wrtie in df - then convert into csv file using to save function"""
    #get the name of the spreadsheet we will write to
    fname = '_'.join(re.findall(r"#(\w+)",hashtag_phrase))

    #open the spreadsheet we will write to
    with io.open('%s.csv' % (fname), 'w') as file: 
        #io is a library which is used when any python2 expression is used in python3 compiler 

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count','Source','lang','retweet_count', 'place'])

              
        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search , q=hashtag_phrase,tweet_mode='extended').items(1000):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'].encode('utf-8') for e in tweet._json['entities']['hashtags']], tweet.user.followers_count, tweet.source, tweet.lang, tweet.retweet_count, tweet.user.location.encode('utf-8')])


# In[3]:



    
hashtag_phrase = input('Hashtag Phrase ')

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)


# In[4]:


import pandas as pd 

df = pd.read_csv(r"C:\Users\Vishwas Rawat\Desktop\Untitled Folder 1\goa.csv")


# In[5]:


df.describe()


# In[6]:


df.columns


# In[7]:


df.username


# In[16]:


def Remove_extra_text(x,txt):
    x = x.str.replace(txt,'')
    return x
df.username = Remove_extra_text(df.username,'b')


# In[18]:


df.username = Remove_extra_text(df.username,"'")


# In[19]:


df.username


# In[21]:


df.tweet_text = Remove_extra_text(df.tweet_text,'b')


# In[23]:


df.tweet_text = Remove_extra_text(df.tweet_text,"'")


# In[24]:


df.tweet_text


# In[ ]:




