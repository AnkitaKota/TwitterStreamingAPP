import json
import unittest
import pytest
import mongomock
from unittest import mock
from src.Twitter_dbconnection import twitter_db_connection
from src.mango_db import crud
import configparser

from src.twitter_auth import twitter_auth


class DBConnectionTest(unittest.TestCase):
    twitter_db_connection =mock
    configparser = mock
    objs = {
        'test_id': '1',
        'test_status': 'success'
    }


    def test_Db_InsertRecord(self):
        collection = mongomock.MongoClient().db.collection
        ret = crud().insert(collection,self.objs)
        print(ret)
        self.assertTrue(ret)  #success
        ret = crud().insert(collection, self.objs)
        self.assertFalse(ret) #Fail

    def test_Db_connection(self):
        client = mongomock.MongoClient()
        configparser.ConfigParser().read('config.ini')
       #twitter_db_connection().db_config(self.objs).assert_called()
        db = twitter_db_connection().db_config()
        self.assertEqual(db.name,"TwitterStreamingDB")


if __name__ == '__main__':
    unittest.main()


