import tweepy 
import speech_recognition as sr

consumer_key=input("ENTER THE CONSUMER KEY ")
consumer_secret=input("ENTER THE SECRET CONSUMER KEY ")
access_token=input("ENTER THE ACCESS TOKEN ")
access_token_secret=input("ENTER THE SECRET ACCESS TOKEN ")


r=sr.Recognizer()

with sr.Microphone() as source:
    print('Say Something ! :')
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        print('here is what u said : {}'.format(text))
    except:
        print('SORRY COULD NOT HEAR WHAT YOU SAID !')



def OAuth():
    try:
        auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = OAuth()

api=tweepy.API(oauth)

api.update_status(text)
print('TWEET IS POSTED !!!')