
import praw

reddit = praw.Reddit(client_id='my client id',
                     client_secret='NmypxsH7PRM7sspRZd7oViZv2t4',
                     user_agent='my user agent')

def retrieve_reddits(t_id, id_provided, n_posts):
    tweets_list = []

    if id_provided:
        tweets = api.GetUserTimeline(user_id=t_id, count=n_posts)
    else:
        tweets = api.GetUserTimeline(screen_name=t_id, count=n_posts)


    for tweet in tweets:
        tweets_list.append(tweet._json['text'])

    text = ". ".join(tweets_list)
    return text