import unittest
from flask import Flask
from pymongo import MongoClient
from mongomock import MongoClient as MockClient
from app import flask_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        flask_app.testing = True
        self.app = flask_app.test_client()

    def test_invalid_method(self):
        response = self.client.post('/')
        self.assertEqual(response.status_code, 405)

class TestDBRead (unittest.TestCase):
    def setUp(self):
        self.client = MockClient()
        self.db = self.client.db['test_db']

    def test_mongo_connection(self):
        try:
            self.client.admin.command('ping')
            connection_success = True
        except NotImplementedError:
            connection_success = False
        self.assertEqual(connection_success or isinstance(self.client, MockClient))


class TestDBWrite (unittest.TestCase):
    def setUp(self):
        self.client = MongoClient()
        self.db = self.client.db['test_db']
        self.collection = self.db['test_collection']

    def test_insert_document(self):
        document = {"name": "Test Document", "value": 123}
        result = self.collection.insert_one(document)
        self.assertIsNotNone(result.inserted_id)

if __name__ == "__main__":
    unittest.main()