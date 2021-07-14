# from django.contrib.auth import get_user_model
from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from project.settings import AUTH_USER_MODEL


# Create your models here.

class Problem(models.Model):
        title = models.CharField(max_length=255)
        description = models.TextField()
        starter = models.TextField()
        def __str__(self):
            return f"{self.title}"


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    avator = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user}"


class Code(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE , default=None)
    problem = models.OneToOneField(Problem ,on_delete=models.CASCADE ,default=None)
    code = models.TextField()


class Passed(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL , on_delete=models.CASCADE , default=None)
    problem = models.OneToOneField(Problem  , on_delete=models.CASCADE , default=None)





