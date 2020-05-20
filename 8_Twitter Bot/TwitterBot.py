import tweepy
import time

auth = tweepy.OAuthHandler( 'ivQpSsqbDOgGP8f9HOKkbXXpZ', 'nhkt7mbrHDxTe2ixqZXxcofD9lD5rZfIT6g6J7Jbayuy4rgXlI')
auth.set_access_token('836965566900551680-4jHAZmklimSkMRwIBfmkI0y5KLNhr2y', 'yHhLtPAQKLjtueUtSMUpCTHeTd3z9pESDmgPl4lf3H8F5')

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



