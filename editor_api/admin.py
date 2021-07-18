from django.contrib import admin
from .models import Problem,  Passed , Code ,Test

# Register your models here.
admin.site.register(Passed)
admin.site.register(Code)
admin.site.register(Problem)
admin.site.register(Test)





