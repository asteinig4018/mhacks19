import tweepy
import json

auth = tweepy.OAuthHandler('DsnUpznpBpU2KOao6Fh8TcR6G', 'RYGCyC2XJJ47k6EFaUQZLige5Gl4bPLUKdfDjgR7CzcycTmT3Q')
auth.set_access_token('1182929356550598656-kvqWqMEeMvOmTqvgLLMLq1WyjCS2s5', 'hYQ3txDXnyBmqN99pfkfMGZsHo6tFdXNulImrzpGsrKry')

api = tweepy.API(auth)

public_tweets = api.trends_place(23424977)
print(public_tweets)


#json.dump(twitter_trends, public_tweets)
with open('twitter_trends.json', 'w') as f:
    json.dump(public_tweets, f)
