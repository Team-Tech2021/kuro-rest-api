from django.urls import path
from . import views
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
from django.urls import include, path

urlpatterns = [
    # path("<int:problem_id>/", views.index, name="index"),
    path("compile/", views.run_code, name="run_code"),
    path("user-code/", views.select_code , name="select_code"),
    path("re/" , include(router.urls))

]
