from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig

from .views import UserCreateApiView, UserListApiView

app_name = UsersConfig.name


urlpatterns = [
    path("create/", UserCreateApiView.as_view(), name="users_create"),
    path("list/", UserListApiView.as_view(), name="users_list"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
