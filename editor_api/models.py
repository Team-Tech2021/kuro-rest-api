from django.db import models
from main.models import User



class Problem(models.Model):
        title = models.CharField(max_length=255)
        description = models.TextField()
        hint = models.TextField()
        starter = models.TextField()
        def __str__(self):
            return f"{self.title}"

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    problem = models.ForeignKey(Problem ,on_delete=models.CASCADE )
    code = models.TextField()


class Passed(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    problem = models.ForeignKey(Problem  , on_delete=models.CASCADE )

class Test(models.Model):
    problem = models.ForeignKey(Problem ,on_delete=models.CASCADE)
    code = models.TextField()



