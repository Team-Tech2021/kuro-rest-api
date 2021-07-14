from django.db import models
from project.settings import AUTH_USER_MODEL



class Problem(models.Model):
        title = models.CharField(max_length=255)
        description = models.TextField()
        hint = models.TextField()
        starter = models.TextField()
        def __str__(self):
            return f"{self.title}"


class Profile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    avator = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user}"


class Code(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE )
    problem = models.OneToOneField(Problem ,on_delete=models.CASCADE )
    code = models.TextField()


class Passed(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL , on_delete=models.CASCADE )
    problem = models.OneToOneField(Problem  , on_delete=models.CASCADE )

class Test(models.Model):
    problem = models.OneToOneField(Problem ,on_delete=models.CASCADE)
    code = models.TextField()



