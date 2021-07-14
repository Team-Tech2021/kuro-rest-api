from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path("", views.index, name="index"),
    # path("login/", views.login_view, name="login"),
    # path("accounts/login/", views.login_view, name="login_sys"),
    # path("github/authorized/", views.github, name="github"),
    path("signup/", SignUpView.as_view(), name= "sign_up"),
    path("logout/", views.logout_view, name="logout")

]

