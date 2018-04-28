import dotenv
import os
import time
import tweepy

# pulled from .env file
auth = tweepy.OAuthHandler(os.getenv("consumer_key"), os.getenv("consumer_secret"))
auth.set_access_token(os.getenv("access_token"), os.getenv("access_token_secret"))

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    time.sleep(0.1)
    print tweet.text

user = api.get_user("BlackNerd")

print user.screen_name
print user.followers_count
for friend in user.friends():
    time.sleep(0.2)
    print friend.screen_name
