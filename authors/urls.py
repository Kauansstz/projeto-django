from django.urls import path
from .views import (
    register_view,
    register_create,
    login_create,
    login_view,
    logout_view,
    dashboad_recipe_edit,
    dashboad,
    dashboard_recipe_new,
    dashboad_recipe_delete,
)


app_name = "authors"

urlpatterns = [
    path("register/", register_view, name="register"),  # type: ignore
    path("register/create/", register_create, name="register_create"),  # type: ignore
    path("login/", login_view, name="login"),  # type: ignore
    path("login/create/", login_create, name="login_create"),  # type: ignore
    path("logout/", logout_view, name="logout"),  # type: ignore
    path("dashboard/", dashboad, name="dashboard"),
    path("dashboard/recipe/new/", dashboard_recipe_new, name="dashboard_recipe_new"),
    path(
        "dashboard/recipe/<int:id>/edit/",
        dashboad_recipe_edit,
        name="dashboard_recipe_edit",
    ),
    path(
        "dashboard/recipe/<int:id>/delete/",
        dashboad_recipe_delete,
        name="dashboard_recipe_delete",
    ),
]
