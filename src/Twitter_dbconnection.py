from enum import unique
import pymongo
from pymongo import MongoClient
import configparser
import json
from pymongo.errors import ConnectionFailure

'''This class is meant for connecting to Mango DB and for saving the data
Note: The future version will be a service to make it more decoupled
Steps: Create Interface as in future it can be SQL server or other Server i.e any server
Create Models -> DTO'''

class twitter_db_connection:
    def db_config(self):
        config = configparser.ConfigParser()
        config.read('./src/config.ini')
        db_user_name = config['database']['mangodb_user_name']
        db_user_password = config['database']['mangodb_password']
        db_name = config['database']['mangodb_dbname']
        connectionString = 'mongodb+srv://' + db_user_name + ':' + db_user_password + '@cluster0.nf7ja.mongodb.net/' + db_name + '?retryWrites=true&w=majority'
        # collection.create_index('twitter_id')  #This will restrict from storing in duplicate twitters
        client = MongoClient(connectionString)
        try:
            db = client.TwitterStreamingDB
            collections = db.twittertweets
            return db
        #    self.insert(collections, insert_db_data)
        except ConnectionFailure:
            print("Server not available")






















