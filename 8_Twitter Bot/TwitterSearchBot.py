import tweepy
import time

auth = tweepy.OAuthHandler( 'ivQpSsqbDOgGP8f9HOKkbXXpZ', 'nhkt7mbrHDxTe2ixqZXxcofD9lD5rZfIT6g6J7Jbayuy4rgXlI')
auth.set_access_token('836965566900551680-4jHAZmklimSkMRwIBfmkI0y5KLNhr2y', 'yHhLtPAQKLjtueUtSMUpCTHeTd3z9pESDmgPl4lf3H8F5')

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