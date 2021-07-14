from django.urls import path
from . import views

urlpatterns = [
    path("compile/", views.run_code, name="run_code"),
    path("user-code/", views.select_code , name="select_code"),
    path("is-complete/", views.is_passed , name="is_passed"),
    path("check-code/", views.check_code , name="check_code"),

]
