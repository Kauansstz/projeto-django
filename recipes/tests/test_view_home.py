from django.test import TestCase
from django.urls import reverse


class RecipeHomeTest(TestCase):
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