from django.test import TestCase
from django.urls import reverse


class RecipeViewTest(TestCase):
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

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse("recipes-search")
        response = self.client.get(url)
        self.assertAlmostEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escape(self):
        url = reverse("recipes-search") + "?q=Teste"
        response = self.client.get(url)
        self.assertIn("Search for &quot;Teste&quot;", response.content.decode("utf-8"))
