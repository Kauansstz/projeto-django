from django.urls import reverse
from unittest.mock import patch
from .test_recipe_base import RecipeTestBase


class RecipeHomeTest(RecipeTestBase):
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse("recipes-home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("recipes-home"))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    def test_recipe_home_template_show_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse("recipes-home"))
        self.assertIn(
            "<h1 class='response'>No Recipes Found Here</h1>",
            response.content.decode("utf-8"),
        )

    def test_recipe_home_is_paginated(self):
        for i in range(9):
            kwargs = {"author_data": {"username": f"u{i}"}, "slug": f"r{i}"}
            self.make_recipe(**kwargs)
        with patch("recipes.views.PER_PAGE", new=3):
            response = self.client.get(reverse("recipes-home"))
            recipes = response.context["recipes"]
            paginatior = recipes.paginator
            self.assertEqual(paginatior.num_pages, 3)
            self.assertEqual(len(paginatior.get_page(1)), 3)
            self.assertEqual(len(paginatior.get_page(2)), 3)
            self.assertEqual(len(paginatior.get_page(3)), 3)
