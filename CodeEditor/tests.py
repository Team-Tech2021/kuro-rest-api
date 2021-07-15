from django.test import TestCase
# Create your tests here.
from rest_framework.test import APIRequestFactory
# from django.http import requests
import requests
import json

class FunctionsTest(TestCase):
    def test_tokens(self):

            '''try it with a real user and the server running'''


            self.url = "http://127.0.0.1:8000/api/token/"
            # self.payload = json.dumps({
            # "username": "kuro",
            # "password": "koko@123"
            # })
            # self.headers = {
            # 'Content-Type': 'application/json'
            # }

            # self.response = requests.request("POST", self.url, headers=self.headers, data=self.payload)

            # first = self.response.text.split(':')
            # assert first[0] == '{"refresh"'

