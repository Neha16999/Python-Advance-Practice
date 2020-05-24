import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)

#To see the public tweets in  your timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
