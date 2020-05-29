import os
import json
import tweepy
from tweepy.auth import OAuthHandler

CONSUMER_KEY = os.environ.get('CONSUMER_API')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

#print(dir(tweepy))
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
#status_update = 'Tweeted using Twitter API !! #Tweepy'
#api.update_status(status_update)
#tweets = api.user_timeline()
#for tweet in tweets:
#    print((tweet.text).encode('utf8'))
#    print(tweet.text)
user = api.get_user('Angel_Chris20')
msg = api.rate_limit_status()
print(msg)


#for frnd in user.friends():
#    print(frnd.screen_name)
