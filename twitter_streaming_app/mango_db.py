import pymongo
from pymongo import MongoClient
from twitter_streaming_app.Twitter_dbconnection import twitter_db_connection
from twitter_streaming_app.DBConnector import DBConnector
from pymongo.errors import ConnectionFailure

''' Operations to perform CRUD '''
class crud(object):

    '''Save only unique twitter records in Mango DB. To Achieve this, I have created unique index'''

    def insert(cls,collections, insert_db_data):
        #Execute Query on Singleton Object
        #collections = cls.db_connection()

        try:
            rec_id1 = collections.insert_one(insert_db_data)
            return rec_id1.acknowledged
        except pymongo.errors.DuplicateKeyError as duplicateRecord:
            print(duplicateRecord)
            return False

    def read(self, id):
        print("Get records with Twitter ID")

    def update(self,id):
        print("Update the records corresponding to ID")

    def delete(self,id):
        print("Delete the corresponding ID")
