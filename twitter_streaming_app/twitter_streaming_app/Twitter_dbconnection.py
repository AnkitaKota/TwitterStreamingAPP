from enum import unique

import pymongo
from pymongo import MongoClient
import configparser
import json
class twitter_db_connection:
    def config(self,insert_db_data):
        config = configparser.ConfigParser()
        config.read('config.ini')
        db_user_name = config['database']['mangodb_user_name']
        db_user_password = config['database']['mangodb_password']
        db_name = config['database']['mangodb_dbname']
        connectionString = 'mongodb+srv://' + db_user_name + ':' + db_user_password + '@cluster0.nf7ja.mongodb.net/' + db_name + '?retryWrites=true&w=majority'
        self.insert(connectionString,insert_db_data)



    def insert(self, connectionString,insert_db_data):
        client = MongoClient(connectionString)

        # collection.create_index('twitter_id')  #This will restrict from storing in duplicate twitters

        client = MongoClient(connectionString)
        db = client.TwitterStreamingDB
        collections = db.twittertweets
        try:
            rec_id1 = collections.insert_one(insert_db_data)
            return rec_id1.acknowledged
        except pymongo.errors.DuplicateKeyError as duplicateRecord:
            print(duplicateRecord)
            return False;



















#collection.insert_one(TwitterRecord)
