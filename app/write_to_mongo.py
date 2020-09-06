from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.social_media

def write_mongodb(twitter_id,prep_text,emotion):

    result = db.twitter.insert_one(
    {
    "user": twitter_id,
    "text": prep_text,
    "emotions": emotion
    }
    )

    return result