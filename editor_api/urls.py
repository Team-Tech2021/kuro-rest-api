from django.urls import path
from .views import *

urlpatterns = [
    path("profile/", ProfileList.as_view(), name="ptofile_list"),
    path("profile/<int:pk>/", ProfileDetail.as_view(), name="ptofile_detail"),
    path("passed/", PassedList.as_view(), name="passed_list"),
    path("passed/<int:pk>/", PassedDetail.as_view(), name="passed_detail"),
    path("code/", CodeList.as_view(), name="code_list"),
    path("problems/", problems, name="problems_api"),
    path("code/<int:pk>/",CodeDetail.as_view(), name="code_detail"),

]

