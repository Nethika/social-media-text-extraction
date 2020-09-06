import json
import os
import twitter

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)

api = twitter.Api(consumer_key = creds['CONSUMER_KEY'],
                    consumer_secret = creds['CONSUMER_SECRET'],
                    access_token_key = creds['ACCESS_TOKEN'],
                    access_token_secret = creds['ACCESS_SECRET'])

def retrieve_tweets(t_id, id_provided, n_posts):
    tweets_list = []

    if id_provided:
        tweets = api.GetUserTimeline(user_id=t_id, count=n_posts)
    else:
        tweets = api.GetUserTimeline(screen_name=t_id, count=n_posts)


    for tweet in tweets:
        tweets_list.append(tweet._json['text'])

    text = ". ".join(tweets_list)
    return text