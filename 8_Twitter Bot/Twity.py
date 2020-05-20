import tweepy
import time

auth = tweepy.OAuthHandler( 'ivQpSsqbDOgGP8f9HOKkbXXpZ', 'nhkt7mbrHDxTe2ixqZXxcofD9lD5rZfIT6g6J7Jbayuy4rgXlI')
auth.set_access_token('836965566900551680-4jHAZmklimSkMRwIBfmkI0y5KLNhr2y', 'yHhLtPAQKLjtueUtSMUpCTHeTd3z9pESDmgPl4lf3H8F5')

api = tweepy.API(auth)
user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)

#To see the public tweets in  your timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)