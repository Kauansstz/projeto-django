from django.urls import path
from .views import (
    register_view,
    register_create,
    login_create,
    login_view,
    logout_view,
    dashboad,
)


app_name = "authors"

urlpatterns = [
    path("register/", register_view, name="register"),  # type: ignore
    path("register/create/", register_create, name="register_create"),  # type: ignore
    path("login/", login_view, name="login"),  # type: ignore
    path("login/create/", login_create, name="login_create"),  # type: ignore
    path("logout/", logout_view, name="logout"),  # type: ignore
    path("dashboad/", dashboad, name="dashboad"),
]
