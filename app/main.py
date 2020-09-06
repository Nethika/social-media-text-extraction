import twitter_records
import text_preprocess
import write_to_mongo
import text_analyze
import argparse
import sys



def main():

    print(len(sys.argv))

    if not len(sys.argv) > 1:
        print ("A social media id or name should be entered to continue!")
    
    if len(sys.argv) > 3:
        print ("May be do one extraction at a time for now?")
        sys.exit(0)

    # Twitters per person
    n_twitters = 10

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--twitter_id", help="twitter id")
    parser.add_argument("-tn", "--twitter_name", help="twitter sreen name")
    parser.add_argument("-r", "--reddit_id", help="reddit id")
    parser.add_argument("-rn", "--reddit_name", help="reddit name")
    parser.add_argument("-f", "--face_book_id", help="face book id")
    parser.add_argument("-fn", "--face_book_name", help="facebook name")
    parser.add_argument("-i", "--instagram_id", help="instagram_id")
    parser.add_argument("-in", "--instagram_name", help="instagram name")
    args = parser.parse_args()

    # Twitter
    if args.twitter_id or args.twitter_name:
        if args.twitter_id: 
            id_pro = True
            twit_id = args.twitter_id
        else: 
            id_pro = False
            twit_id = args.twitter_name
        print("entered twiter id/name:",twit_id) 
        text = twitter_records.retrieve_tweets(t_id= twit_id,id_provided=id_pro,n_posts=n_twitters)
        text = text_preprocess.preprocess_text(text)
        emotions = text_analyze.emotion_values(text)
        print(text)
        res = write_to_mongo.write_mongodb(twitter_id = twit_id, prep_text = text, emotion = emotions)
        print (res)

    # Reddit
    if args.reddit_id:
        reddit_id = args.reddit_id
        print("Entered Reddit id:",face_book_id) 
        print ("Sorry! Reddit Api is not ready yet!")
    if args.reddit_name:
        reddit_name = args.reddit_name
        print("Entered Reddit name:",face_book_name) 
        print ("Sorry! Reddit Api is not ready yet!")


    # Face Book
    if args.face_book_id:
        face_book_id = args.face_book_id
        print("Entered Face Book id:",face_book_id) 
        print ("Sorry! FaceBook Api is not ready yet!")
    if args.face_book_name:
        face_book_name = args.face_book_name
        print("Entered Face Book name:",face_book_name) 
        print ("Sorry! FaceBook Api is not ready yet!")

    # Instagram
    if args.instagram_id:
        instagram_id = args.instagram_id
        print("entered instagram id:",instagram_id) 
        print ("Sorry! Instagram Api is not ready yet!")
    if args.instagram_name:
        instagram_name = args.instagram_name
        print("entered instagram name:",instagram_name)
        print ("Sorry! Instagram Api is not ready yet!")


if __name__ == '__main__':
    main()