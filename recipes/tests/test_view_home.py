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
        self.make_recipe_in_batch(qtd=8)

        with patch("recipes.views.PER_PAGE", new=3):
            response = self.client.get(reverse("recipes-home"))
            recipes = response.context["recipes"]
            paginator = recipes.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)

    def test_invalid_page_query_uses_page_one(self):
        self.make_recipe_in_batch(qtd=8)

        with patch("recipes.views.PER_PAGE", new=3):
            response = self.client.get(reverse("recipes-home") + "?page=12A")
            self.assertEqual(response.context["recipes"].number, 1)
            response = self.client.get(reverse("recipes-home") + "?page=2")
            self.assertEqual(response.context["recipes"].number, 2)
            response = self.client.get(reverse("recipes-home") + "?page=3")
            self.assertEqual(response.context["recipes"].number, 3)
