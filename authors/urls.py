from django.urls import path
from . import views


app_name = "authors"

urlpatterns = [
    path("register/", views.register_view, name="register"),  # type: ignore
    path("register/create/", views.register_create, name="register_create"),  # type: ignore
    path("login/", views.login_view, name="login"),  # type: ignore
    path("login/create/", views.login_create, name="login_create"),  # type: ignore
    path("logout/", views.logout_view, name="logout"),  # type: ignore
    path("dashboard/", views.dashboad, name="dashboard"),
    path(
        "dashboard/recipe/new/",
        views.DashboardRecipe.as_view(),
        name="dashboard_recipe_new",
    ),
    path(
        "dashboard/recipe/delete/",
        views.DashboardRecipeDelete.as_view(),
        name="dashboard_recipe_delete",
    ),
    path(
        "dashboard/recipe/<int:id>/edit/",
        views.DashboardRecipe.as_view(),
        name="dashboard_recipe_edit",
    ),
]
