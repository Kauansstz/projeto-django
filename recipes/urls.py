from django.urls import path
from . import views


urlpatterns = [
    path("", views.RecipeListViewHome.as_view(), name="recipes-home"),
    path(
        "recipes/search/", views.RecipeListViewSearch.as_view(), name="recipes-search"
    ),
    path("recipes/<int:id>/", views.RecipeDetail.as_view(), name="recipes-recipe"),
    path(
        "recipes/category/<int:pk>/",
        views.RecipeListViewCategory.as_view(),
        name="recipes-category",
    ),
    path(
        "recipes/api/v1/",
        views.RecipeListViewHomeApi.as_view(),
        name="recipes_api_v1",
    ),
]
