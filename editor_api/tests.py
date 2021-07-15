from django.test import TestCase
from .models import *
from main.models import User


class APITest(TestCase):
    """ Test module for APIs model """

    def setUp(self):
        self.user = User.objects.create(
        username='Eren', email="eren@gmail.com", first_name='Eren', password='Attack@123')
        self.problem = Problem.objects.create(
        title = "sum_num",
        description = "sum two numbers",
        hint = "use plus sign",
        starter = "def sum_num(a,b):"
        )
        self.Code= Code.objects.create(
        user = self.user,
        problem = self.problem,
        code = "return a+b"
        )

    def test_user_name(self):
        self.assertEqual(
           str(self.user) , "Eren")
    def test_problem(self):
            self.assertEqual(
           str(self.problem.title) , "sum_num")
    def test_user_code(self):
        self.assertEqual(
            str(Code.objects.get(user=self.user , problem=self.problem).code),"return a+b")


