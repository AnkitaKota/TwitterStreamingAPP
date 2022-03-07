import unittest
from unittest import mock

from pymongo import MongoClient
from pytest_mock_resources import create_mongo_fixture
import mongomock
from unittest.mock import patch
from twitter_streaming_app.Twitter_dbconnection import twitter_db_connection


mongo = create_mongo_fixture()
mocked_mongo = mongomock.MongoClient()
class MyTestCase(unittest.TestCase):
    @mock.patch("pymongo.collection.Collection.find")
    def test_create_custom_connection(self,mock_find):
        mock_find.return_value = 1






