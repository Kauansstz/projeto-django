from django.shortcuts import render, get_list_or_404
from .models import Recipe
from django.db.models import Q
from django.http import Http404
from django.core.paginator import Paginator
from utils.paginitions import make_pagination_range


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    try:
        current_page = int(request.GET.get("page", 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(recipes, 9)
    page_obj = paginator.get_page(current_page)
    pagination_page = make_pagination_range(paginator.page_range, 4, current_page)

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
