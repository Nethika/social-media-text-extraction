# Social Media Data 

**Retrived, Cleaned, anonymized and stored social media data.**

## From:


- twitter
- reddit
- face_book
- instagram


# To Run:
```
python main.py -t 613601697
python main.py -tn MSCloud
python main.py -tn realDonaldTrump
```

# MongoDB on Docker:
```
mongo.bat
```

# Mongo Help to view stored data:

```
docker exec -ti mongo mongo
> show dbs
> use social_media
> show collections
> db.twitter.find().pretty()

```

# Requirements:

```
python-twitter==3.3
spacy==2.0.12
textacy==0.6.2
pymongo==3.0.3
```

# Arguments

```
usage: main.py [-h] [-t TWITTER_ID] [-tn TWITTER_NAME] [-f FACE_BOOK_ID] [-fn FACE_BOOK_NAME] [-i INSTAGRAM_ID] [-in INSTAGRAM_NAME]

optional arguments:
  -h,                   --help                          show this help message and exit
  -t TWITTER_ID,        --twitter_id TWITTER_ID         twitter id
  -tn TWITTER_NAME,     --twitter_name TWITTER_NAME     twitter sreen name
  -f FACE_BOOK_ID,      --face_book_id FACE_BOOK_ID     face book id
  -fn FACE_BOOK_NAME,   --face_book_name FACE_BOOK_NAME facebook name
  -i INSTAGRAM_ID,      --instagram_id INSTAGRAM_ID     instagram_id
  -in INSTAGRAM_NAME,   --instagram_name INSTAGRAM_NAME instagram name

```

** One argument is given at one time **                        