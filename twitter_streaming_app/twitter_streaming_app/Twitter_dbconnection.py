from enum import unique
import pymongo
from pymongo import MongoClient
import configparser
import json

'''This class is meant for connecting to Mango DB and for saving the data
Note: The future version will be a service to make it more decoupled
Steps: Create Interface as in future it can be SQL server or other Server
Create Models -> DTO'''

class twitter_db_connection:
    def config(self,insert_db_data):
        config = configparser.ConfigParser()
        config.read('config.ini')
        db_user_name = config['database']['mangodb_user_name']
        db_user_password = config['database']['mangodb_password']
        db_name = config['database']['mangodb_dbname']
        connectionString = 'mongodb+srv://' + db_user_name + ':' + db_user_password + '@cluster0.nf7ja.mongodb.net/' + db_name + '?retryWrites=true&w=majority'
        self.insert(connectionString,insert_db_data)


    '''Save only unique twitter records in Mango DB. To Achieve this, I have created unique index'''
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
