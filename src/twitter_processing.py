import json
import nltk
from tweepy import OAuthHandler, StreamListener, Stream
import time
from dateutil import parser
from src.Twitter_dbconnection import twitter_db_connection
from src.mango_db import crud
import logging
logger = logging.getLogger()
db_data= {}

'''Here we are using tweepy streaming library wherein we have stream listener which will keep polling for new records  '''


class processing(StreamListener):
    total_tweets = 0
    unique_tweetcount = 0

    def on_connect(self):
        print("You are connected to the Twitter API")

    def on_error(self, status_code):
        if status_code != 200:
            print("error found")
            # returning false disconnects the stream
            return False

    def on_data(self, data):
        try:
            db = twitter_db_connection().db_config()
            print("The No. of unique tweets consumed:",db.twittertweets.count_documents({}))
            logger.info("The No. of unique tweets consumed: %d " % db.twittertweets.count_documents({}))

            raw_data = json.loads(data)
            self.total_tweets += 1
            print("Total Tweets: ",self.total_tweets)
            logger.info("Total Tweets: %d " % (self.total_tweets))
            logger.info("The No. of unique tweets consumed: %d " % (self.unique_tweetcount))

            if 'text' in raw_data:
                db_data['twitter_id']= raw_data['id']
                db_data['username'] = raw_data['user']['screen_name']
                db_data['created_at'] = str(parser.parse(raw_data['created_at']))
                tweet = raw_data['text']
                db_data['tweet'] = raw_data['text']
                db_data['retweet'] = raw_data['retweet_count']
                db_data['location'] = raw_data['user']['location']
                logger.info("Json converted Response of Twitter Data" , db_data)


                # Parsing each word in words
                tokens = nltk.word_tokenize(tweet)
                filter_key_words = ['music', 'Music', 'MUSIC', '#music', '#MUSIC', '#Music']
                filter_words_check = bool(sum(map(lambda word_check: word_check in filter_key_words,tokens)))

                # check if the music word is present in the tweet
                if filter_words_check == True:
                    #Store in Mango DB
                    print("Justin Biebier's music Tweet found  at: '{str(parser.parse(raw_data['created_at']))}' ")
                    crud().insert(db.twittertweets,db_data)
                else:
                    print("Duplicate Tweet found or the tweet is not associated with Music  ")

        except AttributeError as e:
            print(e)


