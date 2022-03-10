from pymongo import MongoClient
import configparser
import json
from pymongo.errors import ConnectionFailure


class DBConnector(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.db_user_name = config['database']['mangodb_user_name']
        self.db_user_password = config['database']['mangodb_password']
        self.db_name = config['database']['mangodb_dbname']

    # Creates a connection
    def create_connection(self):
        print(self.db_user_name)
        connection_string = 'mongodb+srv://' + self.db_user_name + ':' + self.db_user_password + '@cluster0.nf7ja.mongodb.net/' + self.db_name + '?retryWrites=true&w=majority'
        return MongoClient(connection_string)

    # For explicitly opening database connection
    def __enter__(self):
        self.dbconn = self.create_connection()
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbconn.close()
