import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

search_str = 'BanTikTok'
num_of_count = 2

for tweet in tweepy.Cursor(api.search, search_str).items(num_of_count):
    try:
        tweet.favorite()
        #tweet.retweet()
        print("I liked that tweet")
    except  tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break        
