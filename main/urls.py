from django.urls import path
from . import views
from  editor_api import admin

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("info/<str:section>", views.info, name="index"),
#     path("login/", views.login_view, name="login"),
#     # path("admin/", admin.admin.site.urls , name='home'),
#     # path("accounts/login/", views.login_view, name="login_sys"),
#     path("github/authorized/", views.github, name="github"),
#     path("logout/", views.logout_view, name="logout"),


# ]
from .views import CustomUserCreate, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]
