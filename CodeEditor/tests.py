from django.test import TestCase
import requests
import json
from main.models import User
from rest_framework import status
from django.urls import reverse
import environ
environ.Env.read_env()
env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "PRODUCTION"),
    ALLOW_ALL_ORIGINS=(bool, False),
    ALLOWED_HOSTS=(list, ['127.0.0.1', 'localhost']),
    ALLOWED_ORIGINS=(list, []),
    DATABASE_ENGINE=(str, "django.db.backends.sqlite3"),
    DATABASE_NAME=(str,  "db.sqlite3"),
    DATABASE_USER=(str, ""),
    DATABASE_PASSWORD=(str, ""),
    DATABASE_HOST=(str, ""),
    DATABASE_PORT=(int, 5432),
)
ENVIRONMENT = env.str("ENVIRONMENT")

class FunctionsTest(TestCase):
    def test_create_user(self):
        self.host_url = tuple(env.list("ALLOWED_HOSTS"))[0]
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
        if self.host_url == '127.0.0.1' or self.host_url == 'localhost' :
            url = 'http://127.0.0.1:8000/problems/check-code/'

        else:
            url = 'https://kuro-space-rest-api.herokuapp.com/'
        payload = {
"code":"def%20nth_fib%28n%29%3A%0A%09%22%22%22correct%20implementation%20for%20thistwice%20test%22%22%22%0A%09if%20n%20%3D%3D%202%3A%0A%09%09return%201%0A%09elif%20n%20%3D%3D%201%3A%0A%09%09return%200%0A%09else%3A%0A%09%09return%20nth_fib%28n-1%29%20%2B%20nth_fib%28n-2%29",
"problem":1
}
        data = json.dumps(payload)
        response2 = requests.post(url, data=data, headers=headers)
        json_data = json.loads(response2.text)
        self.assertTrue( "test" in json_data or  "tests" in json_data['data'][0] )

