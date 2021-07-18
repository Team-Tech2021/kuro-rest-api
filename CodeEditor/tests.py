from django.test import TestCase
import requests
import json
from main.models import User
from rest_framework import status
from django.urls import reverse

class FunctionsTest(TestCase):

    def test_create_user(self):

        url = reverse('token_obtain_pair')
        u = User.objects.create_user(username='user', email='user@gmail.com', password='koko@123')
        u.is_active = True
        u.save()

        resp = self.client.post(url, {'username':'user', 'password':'koko@123'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        u.is_active = True
        u.save()

        self.assertTrue('access' in resp.data)
        token = resp.data['access']
        headers = {
  'Authorization': f'Bearer {token}',
  'Content-Type': 'application/json'
}
        url = 'http://127.0.0.1:8000/problems/check-code/'
        payload = {
"code":"def%20nth_fib%28n%29%3A%0A%09%22%22%22correct%20implementation%20for%20thistwice%20test%22%22%22%0A%09if%20n%20%3D%3D%202%3A%0A%09%09return%201%0A%09elif%20n%20%3D%3D%201%3A%0A%09%09return%200%0A%09else%3A%0A%09%09return%20nth_fib%28n-1%29%20%2B%20nth_fib%28n-2%29",
"problem":1
}
        data = json.dumps(payload)
        response2 = requests.post(url, data=data, headers=headers)
        json_data = json.loads(response2.text)
        self.assertTrue( "test" in json_data['data'][0] or  "tests" in json_data['data'][0] )

