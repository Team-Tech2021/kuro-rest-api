from django.test import TestCase
from .models import User


class UserTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        self.user = User.objects.create(
            username='Eren', email="eren@gmail.com", first_name='Eren', password='Attack@123')


    def test_user_name(self):
        self.assertEqual(
           str(self.user) , "Eren")
    def test_user_email(self):
            self.assertEqual(
           str(self.user.email) , "eren@gmail.com")


