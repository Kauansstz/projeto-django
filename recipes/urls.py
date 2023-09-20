

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name='recipes-recipe'),
    path('recipes/category/<int:id>/', views.category, name='recipes-category'),
]
 