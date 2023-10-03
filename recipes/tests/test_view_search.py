from django.test import TestCase
from django.urls import reverse


class RecipeSearchTest(TestCase):
    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse("recipes-search")
        response = self.client.get(url)
        self.assertAlmostEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escape(self):
        url = reverse("recipes-search") + "?q=Teste"
        response = self.client.get(url)
        self.assertIn("Search for &quot;Teste&quot;", response.content.decode("utf-8"))
