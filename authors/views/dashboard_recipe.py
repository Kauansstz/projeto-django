from django.views import View
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from recipes.models import Recipe
from django.http import Http404
from authors.forms.recipe_form import AuthorRecipeForm


class DashboardRecipe(View):
    def get(self, request, id):
        recipe = Recipe.objects.filter(
            is_published=False,
            author=request.user,
            pk=id,
        ).first()
        if not recipe:
            raise Http404()

        form = AuthorRecipeForm(
            request.POST or None,
            instance=recipe,
            files=request.FILES or None,
        )

        if form.is_valid():
            recipe = form.save(commit=False)

            recipe.authors = request.user
            recipe.preparation_steps_is_html = False
            recipe.is_published = False

            recipe.save()

            messages.success(request, "Sua receita foi salva com sucesso!")
            return redirect(reverse("authors:dashboad_recipe_edit", args=(id,)))

        return render(
            request,
            "authors/pages/dashboard_recipe.html",
            {
                "recipes": recipe,
                "form": form,
            },
        )
