import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


def limit_handle(cursor):
    try:
        while True:
            yield  cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)        
    except StopIteration:
        print("Done for Now !")    
        

#generous bot
for followers in limit_handle(tweepy.Cursor(api.followers).items()):
    print(followers.name)
    if followers.name == "Bootstrap Jungle" or followers.followers_count > 10:
        followers.unfollow()
        print("UnFollowed")
    else:
        print("No need to follow")    



