from django.urls import path
from .views import *

urlpatterns = [
    path("passed/", PassedList.as_view(), name="passed_list"),
    path("passed/<int:pk>/", PassedDetail.as_view(), name="passed_detail"),
    path("code/", CodeList.as_view(), name="code_list"),
    path("code/<int:pk>/",CodeDetail.as_view(), name="code_detail"),
    path("problem/", ProblemList.as_view(), name="problems_list"),
    path("problem/<int:pk>/", ProblemDetail.as_view(), name="problems_detail"),

]

