import pandas as pd
from pymongo import MongoClient
from bson import BSON
from bson import json_util
import json
import sys

import twitter

api = twitter.Api(consumer_key='w0IGurbZveIRODYtdvkZpYL3e',
  consumer_secret='haQ57SPr88NHvZMwPlygWBbts0Dz8zYxnw0AWvlSX1oiOHjp3b',
  access_token_key='975089079212761090-7cDtUFXK7G9ZOagX1JbYcc8VqQQ9ht7',
  access_token_secret='gdkRfX7kdPB33B62n3M5jrF7OWUn82dQEp5G74ViDw32L')

#print(api.VerifyCredentials())


client = MongoClient('localhost', 27017)
db = client['Indecopi']

#search = api.GetSearch("Indecopi")

t = api.GetUserTimeline(screen_name="IndecopiOficial", count=150)
tweets = [i.AsDict() for i in t]


i = 0
for t in tweets:
    if "in_reply_to_status_id" in t.keys():
        try:
            originalTweet = api.GetStatus(status_id=t["in_reply_to_status_id"])
            print(originalTweet)
            originalTweet = originalTweet.AsDict()
            originalTweet["Response_Indecopi"] = t
            print(json.dumps(originalTweet, indent=2))
            #db.Tweets.insert(originalTweet)
            i += 1
        except:
            print("Unexpected error:", sys.exc_info()[0])
print(i)


#for tweet in search:
#    print(tweet.id, tweet.text)
