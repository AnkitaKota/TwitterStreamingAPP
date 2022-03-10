import json
import unittest
import pytest
import mongomock
from unittest import mock
import configparser
from twitter_streaming_app.twitter_auth import twitter_auth


class TweepyAPIAuthTest(unittest.TestCase):
    twitter_auth = mock
    configparser = mock
    tweepy = mock

    def test_auth(self):
        print("Authentication Testing")
        auth = twitter_auth().authentication()
        self.assertFalse(auth)

if __name__ == '__main__':
    unittest.main()
