from django.urls import path
from . import views


urlpatterns = [
    path("", views.RecipeListViewHome.as_view(), name="recipes-home"),
    path("recipes/search/", views.search, name="recipes-search"),
    path("recipes/<int:id>/", views.recipe, name="recipes-recipe"),
    path("recipes/category/<int:id>/", views.category, name="recipes-category"),
]
