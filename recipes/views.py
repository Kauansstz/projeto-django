from django.shortcuts import render, get_list_or_404
from .models import Recipe
from django.db.models import Q
from django.http import Http404
from utils.paginitions import make_pagination

import os

PER_PAGE = int(os.environ.get("PER_PAGE", 6))


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    page_obj, pagination_page = make_pagination(request, recipes, PER_PAGE)

    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": page_obj,
            "pagination_page": pagination_page,
        },
    )


def category(request, id):
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=id, is_published=True).order_by("-id")
    )
    page_obj, pagination_page = make_pagination(request, recipes, PER_PAGE)
    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": page_obj,
            "pagination_page": pagination_page,
            "title": f"{recipes[0].category} - Category | ",
        },
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
            Q(title__icontains=search_term) | Q(description__icontains=search_term),
        ),
        is_published=True,
    ).order_by("-id")

    page_obj, pagination_page = make_pagination(request, recipes, PER_PAGE)

    return render(
        request,
        "recipes/pages/search.html",
        {
            "page_title": f'Search for "{search_term}" ',
            "recipes": page_obj,
            "pagination_page": pagination_page,
            "additional_url_query": f"&q={search_term}",
        },
    )
