import tweepy
import tkinter

consumer_key = 'U3gMFdibOGwZydmLrq4QDXND2'
consumer_secret = 'ejUSd5ISd1q43FnCQ4ua9fMI2O5wSLDYilIa4eAAeJFtKlt2ro'
access_token = '788354959846805504-YU1u6Of14yOr55vnEciVQfqYubDsTag'
access_token_secret = 'ctvhZs76A0czlbObaVm5pW5O3KffGmtkgmqVHAzCdSPp0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK.")
except:
    print("Authentication failed.")