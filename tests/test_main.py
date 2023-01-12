from app import create_app
import unittest

# How to run this file ?

# ../quickflask$ python -m unittest tests.test_main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_main(self):
        rv = self.client.get('/')
        assert rv.status == '200 OK'

    def test_404(self):
        rv = self.client.get('/unknownendpoint')
        self.assertEqual(rv.status, '404 NOT FOUND')
