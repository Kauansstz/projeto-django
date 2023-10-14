from django.urls import path
from .views import register_view, register_create

app_name = "authors"

urlpatterns = [
    path("register/", register_view, name="register"),  # type: ignore
    path("register/create/", register_create, name="create"),  # type: ignore
]
