from .base import RecipeBaseFunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from unittest.mock import patch


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, "body")
        self.sleep()
        self.assertIn("No Recipes Found Here", body.text)

    def test_recipe_search_input_can_find_correct_recipes(self):
        recipes = self.make_recipe_in_batch()
        title_need = "This is what I need"
        recipes[0].title = title_need
        recipes[0].save()

        # usuário abre a página
        self.browser.get(self.live_server_url)

        # Vê um campo de busca com o texto "Search for a recipe"
        search_input = self.browser.find_element(
            By.XPATH, '//input[@placeholder="Search for a recipe"]'
        )
        # Clica neste imput
        search_input.click()

        search_input.send_keys(title_need)
        search_input.send_keys(Keys.ENTER)

        self.assertIn(
            title_need,
            self.browser.find_element(By.CLASS_NAME, "main-content-list").text,
        )

        self.sleep(6)
