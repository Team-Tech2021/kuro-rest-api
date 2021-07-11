from django.contrib.auth.models import AbstractUser
from editor_api.models import *

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

