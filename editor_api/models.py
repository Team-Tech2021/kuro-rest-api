# from django.contrib.auth import get_user_model
from django.db import models
# from django.contrib.auth.models import User

from django.conf import settings

# Create your models here.

class Problem(models.Model):
        title = models.CharField(max_length=255)
        description = models.TextField()
        starter = models.TextField()
        def __str__(self):
            return f"{self.title}"


class Code(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , default=None)
    problem = models.OneToOneField(Problem ,on_delete=models.CASCADE ,default=None)
    code = models.TextField()


class Passed(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , default=None)
    problem = models.OneToOneField(Problem  , on_delete=models.CASCADE , default=None)





