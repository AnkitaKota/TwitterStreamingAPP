"""Main module."""

import tweepy
import configparser
import logging
import time
from tweepy import Stream
from twitter_streaming_app.twitter_processing import processing
tracklist = ['#justinbieber']


'''This class is meant for performing oauth authentication to Twitter. Once
we achieve successful connection, the stream of data will be filtered by keyword: #justinbieber'''
class twitter_auth:
    def auth(self):
        logger = logging.getLogger()

        # Read all configs

        config = configparser.ConfigParser()
        config.read('config.ini')
        api_key = config['twitter']['api_key']
        api_key_secret = config['twitter']['api_key_secret']
        access_token = config['twitter']['access_token']
        access_token_secret = config['twitter']['access_token_secret']

        # authentication using tweepy

        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)



        # test authentication
        if api.verify_credentials():
            print("Authentication OK")
            twitter_processing = processing()
            stream = Stream(auth, twitter_processing)
            stream.filter(track=tracklist)
        else:
            print("error during Authentication")

    def twitter_db_connect(self):
        print("mango DB Connection")
