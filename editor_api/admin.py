from django.contrib import admin
from .models import Problem, Profile , Passed , Code

# Register your models here.
admin.site.register(Profile)
admin.site.register(Passed)
admin.site.register(Code)
admin.site.register(Problem)



