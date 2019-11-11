#!/usr/bin/env python
# coding: utf-8



#initi block
#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import json
from time import sleep
import pandas as pd
import time
import datetime as dt

#fill with Twitter API credentials
credentials={}
credentials['consumer_key']=''
credentials['consumer_secret']= ''
credentials['access_token']=''
credentials['access_token_secret']= ''

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
api = tweepy.API(auth, wait_on_rate_limit=True)

#read csv with quotes
df = pd.read_csv('quotes.csv')

#process dataframe
df['all_quote'] = df['Quote'] + ' -' + df['Author']
df.drop(['Quote','Author'], axis=1)
pd.options.display.max_colwidth = 200
df = df.dropna()

time_interval = 10

while True:
    quote = (df['all_quote'].sample(n = 1)).to_string()
    quote = quote.lstrip("0123456789=,")
    api.update_status(quote)
    time.sleep(time_interval)

