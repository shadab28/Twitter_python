#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd 
import csv

import io
#python 2 compatibility 
import tweepy
#twitter api, needs authentication 
import re
#regular expressions library 

from textblob import TextBlob
import string
import preprocessor as p


consumer_key = r"QX5f1rtJNAfpF7SsWYqz08Nts"
consumer_secret = r"q9T8ACJFjonY8AAkG0ENaReZtpqoZF3kYzCqmQFrt70envXKN8"
access_token = r"2295859188-fh0fR9DMXuJX7NJNtdEpF77sg4O6iSf8YSTdObg"
access_token_secret = r"sMxWgIbqhBPYftTDJkCAcIhMd9QQZI95MJDRbZJsjlZbD" 


# In[2]:


from datetime import datetime
import pytz


tz_NY = pytz.timezone('America/New_York') 

#current time 
datetime_NY = datetime.now(tz_NY)

print("NY time:", datetime_NY.strftime("%H:%M:%S"))
tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))


# In[3]:


"""
INPUTS:
    telling twitter that we are authorized to access this data
    hashtag_phrase: the combination of hashtags to search for
OUTPUTS:
    none, simply save the tweet info to a spreadsheet
"""



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


# In[7]:



    
hashtag_phrase = input('Hashtag Phrase ')

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)


# In[4]:


#code to get tweets of a specific user 

access_key = access_token
access_secret = access_token_secret

# Function to extract tweets 
def get_tweets(username): 
		
		# Authorization to consumer key and consumer secret 
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

		# Access to user's access key and access secret 
		auth.set_access_token(access_key, access_secret) 

		# Calling api 
		api = tweepy.API(auth) 

		# 200 tweets to be extracted 
		number_of_tweets=100  #sample number that we reach on conclusion 
        
		tweets = api.user_timeline(screen_name=username) 

		# Empty Array 
		tmp=[] 

		# create array of tweet information: username, 
		# tweet id, date/time, text 
		tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
		for j in tweets_for_csv: 

			# Appending tweets to the empty array tmp 
			tmp.append(j) 

		# Printing the tweets 
		print(tmp) 


# Driver code 
if __name__ == '__main__': 

	# Here goes the twitter handle for the user 
	# whose tweets are to be extracted. 
	get_tweets("@iamsrk") 


# In[ ]:


class StreamListener(tweepy.StreamListener):
    """tweepy.StreamListener is a class provided by tweepy used to access
    the Twitter Streaming API to collect tweets in real-time.
    """


# In[8]:


import pandas as pd 

df = pd.read_csv(r"C:\Users\Vishwas Rawat\Desktop\Untitled Folder 1\shimla.csv")


# In[9]:


df.describe()


# In[10]:


df.columns


# In[11]:


df.username


# In[12]:


df.timestamp


# In[13]:


df_date = df.timestamp.copy()


# In[14]:


df_date.describe


# In[15]:


df_date=pd.DataFrame(df_date)


# In[16]:


print(df_date.head())


# In[23]:


from datetime import datetime

datetime_str = '09/19/18 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)  # printed in default format


# In[76]:


for key, value in df_date.iteritems():
    t=value

print (t)    

    


# In[85]:


df_date.drop("date", axis = 1)


# In[86]:


df.username


# In[130]:


df_username = df.username.copy()


# In[131]:


print(df_username)


# In[122]:





# In[135]:


df_username
split_data = df_username.str.split("b'")
data = split_data.to_list()
names = ["str","extra", "username"]
new_df = pd.DataFrame(data, columns=names)


# In[133]:


type(new_df)


# In[150]:


split_data_2 = new_df.extra.str.split("'")
data_1= split_data.to_list()
names_1 = ["username"]
new_df_2 = pd.DataFrame(data_1, columns=names_1)


# In[151]:


new_df_2


# In[ ]:




