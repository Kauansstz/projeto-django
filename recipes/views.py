from django.shortcuts import render, get_list_or_404
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.http import Http404

def home(request):
    recipes = Recipe.objects.filter( is_published = True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        
    })
    
def category(request, id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id= id, is_published = True ).order_by('-id'))
    # category_name = getattr(recipes.first(), 'category', None)
    # if not recipes:
    #     raise Http404('Página inexistente')
    return render(request, 'recipes/pages/category.html', context={
            'recipes': recipes,
            'title': f'{recipes[0].category.name} - Category | '
        })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })


    
