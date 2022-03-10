"""Main module."""

import tweepy
import configparser
import logging
from tweepy import Stream
from src.twitter_processing import processing
tracklist = ['#justinbieber']


'''This class is meant for performing oauth authentication to Twitter. Once
we achieve successful connection, the stream of data will be filtered by keyword: #justinbieber'''

"""
    Constructs twitter api object with all required keys, tokens.

    @return: tweepy API object
    @rtype: tweepy.api.API
    """

class twitter_auth:

    def authentication(self):
        logger = logging.getLogger()

        # Read all configs

        config = configparser.ConfigParser()
        config.read('./src/config.ini')
        api_key = config['twitter']['api_key']
        api_key_secret = config['twitter']['api_key_secret']
        access_token = config['twitter']['access_token']
        access_token_secret = config['twitter']['access_token_secret']

        # authentication using tweepy

        self.auth = tweepy.OAuthHandler(api_key, api_key_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        if api.verify_credentials():
            print("Authentication OK")
            return True
        else:
            print("error during Authentication")


    def filter_stream_data(self):
        twitter_processing = processing()
        stream = Stream(self.auth, twitter_processing)
        stream.filter(track=tracklist)



