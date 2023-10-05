from django.shortcuts import render, get_list_or_404
from .models import Recipe
from django.db.models import Q
from django.http import Http404


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,
        },
    )


def category(request, id):
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=id, is_published=True).order_by("-id")
    )
    return render(
        request,
        "recipes/pages/category.html",
        context={"recipes": recipes, "title": f"{recipes[0].category} - Category | "},
    )


def recipe(request, id):
    recipe = Recipe.objects.filter(pk=id, is_published=True).order_by("-id").first()
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={
            "recipe": recipe,
            "is_detail_page": True,
        },
    )


def search(request):
    search_term = request.GET.get("q", "").strip()
    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) | Q(decription__icontains=search_term),
        ),
        is_published=True,
    ).order_by("-id")

    return render(
        request,
        "recipes/pages/search.html",
        {
            "page_title": f'Search for "{search_term}" ',
            "recipes": recipes,
        },
    )
