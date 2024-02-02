from django.shortcuts import render, get_list_or_404
from .models import Recipe
from django.db.models import Q
from django.http import Http404
from utils.paginitions import make_pagination
from django.views.generic import ListView
import os

PER_PAGE = int(os.environ.get("PER_PAGE", 6))


class RecipeListViewBase(ListView):
    model = Recipe
    paginate_by = None  # type: ignore
    context_object_name = "recipes"
    ordering = ["-id"]
    template_name = "recipes/pages/home.html"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(is_published=True)
        return qs

    def get_context_data(self, *args, **kwargs):
        ct = super().get_context_data(*args, **kwargs)
        page_obj, pagination_page = make_pagination(
            self.request, ct.get("recipes"), PER_PAGE
        )
        ct.update(
            {
                "recipes": page_obj,
                "pagination_page": pagination_page,
            }
        )
        return ct


class RecipeListViewHome(RecipeListViewBase):
    template_name = "recipes/pages/home.html"


class RecipeListViewCategory(RecipeListViewBase):
    template_name = "recipes/pages/category.html"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(category__id=self.kwargs.get("id"))
        return qs


class RecipeListViewSearch(RecipeListViewBase):
    template_name = "recipes/pages/search.html"

    def get_queryset(self, *args, **kwargs):
        search_term = self.request.GET.get("q", "")
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            Q(
                Q(title__icontains=search_term) | Q(description__icontains=search_term),
            ),
        )
        return qs

    def get_context_data(self, *args, **kwargs):
        ct = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get("q", "")
        ct.update(
            {
                "page_title": f'Search for "{search_term}" ',
                "search_term": search_term,
                "additional_url_query": f"&q={search_term}",
            }
        )
        return ct


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
