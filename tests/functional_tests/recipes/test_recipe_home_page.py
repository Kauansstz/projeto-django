from base import RecipeBaseFunctionalTest
from selenium.webdriver.common.by import By


class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        self.sleep(6)
        body = self.browser.find_element(By.TAG_NAME, "body")
        self.assertIn("No Recipes Found Here", body.text)
