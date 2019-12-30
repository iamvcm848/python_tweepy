import tweepy 


consumer_key=input("ENTER THE CONSUMER KEY ")
consumer_secret=input("ENTER THE SECRET CONSUMER KEY ")
access_token=input("ENTER THE ACCESS TOKEN ")
access_token_secret=input("ENTER THE SECRET ACCESS TOKEN ")


def OAuth():
    try:
        auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = OAuth()

api=tweepy.API(oauth)

api.update_status('I am posting a tweet using Python !!!')
print('TWEET IS POSTED !!!')