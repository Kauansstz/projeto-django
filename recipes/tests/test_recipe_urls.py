from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        home_url = reverse("recipes-home")
        self.assertEqual(home_url, "/")

    def test_recipe_url_is_correct(self):
        url = reverse("recipes-category", kwargs={"id": 1})
        self.assertEqual(url, "/recipes/category/1/")

    def test_recipe_detail_url_is_correct(self):
        url = reverse("recipes-recipe", kwargs={"id": 1})
        self.assertEqual(url, "/recipe/1/")
