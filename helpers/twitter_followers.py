# import the module
import tweepy
import time

consumer_key = "klhyjSVTsWGbB1uqKbFaXVRHx"
consumer_secret = "ULuVafBRzb6qxYom9QkY7zAVN3Qcl6JARLovcHGpPVjKJRzhvV"
access_token = "3243120639-94OkCCzATiYlRfW8HR1JR08BRebyqWWzJjReLK2"
access_token_secret = "5tkv9XE6hYU4oiPFduT6Fz3NHH4NM9gpWfm9x03KnXRIw"

def get_followers_for_user(user_id):
    # authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    
    # set access to user's access key and access secret 
    auth.set_access_token(access_token, access_token_secret)
    
    # calling the api 
    api = tweepy.API(auth)

    c = tweepy.Cursor(api.followers, user_id).items()
    follower_ids = []

    while True:
        try:
            follower = c.next()
            # Insert into db
            follower_ids.append(follower.id)
        except tweepy.TweepError:
            time.sleep(60 * 15)
            continue
        except StopIteration:
            break

    return follower_ids