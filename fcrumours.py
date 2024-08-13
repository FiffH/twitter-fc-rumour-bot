import tweepy
import tkinter
from config import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK.")
except:
    print("Authentication failed.")


# find relevant tweets
query = "Brentford transfer OR Brentford signing OR Brentford sign OR Brentford interested"

potential_tweets = api.search_tweets(q=query, lang="en", count = 5)

for tweet in potential_tweets:
    print(tweet.text)