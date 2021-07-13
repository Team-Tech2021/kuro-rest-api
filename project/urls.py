
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

urlpatterns = [
    path("admin/", admin.site.urls , name='home'),
    path("api/v1/", include("editor_api.urls")),
    # path('user/', include('main.urls', namespace='users')),

    path("api-auth/", include("rest_framework.urls")),

    path(
        "api/token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("", include("main.urls" , namespace='users')),
    path("problems/", include("CodeEditor.urls")),

]
