from unittest.mock import MagicMock
import requests
from app import search
import unittest
from os import environ


class AppTest(unittest.TestCase):

    def testApiShouldReturn401(self):
        response = requests.get('http://0.0.0.0/search', params={'query': 'victor'})
        self.assertEqual(401, response.status_code)
    
    def testApiShouldReturn422(self):
        response = requests.get('http://0.0.0.0/search', headers={'Authorization': environ['TOKEN']})
        self.assertEqual(422, response.status_code)