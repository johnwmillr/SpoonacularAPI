import os
import unittest
from spoonacular import api

# Import API keys from environment variables
api_key_name = "SPOONACULAR_API_KEY"
api_key = os.environ.get(api_key_name, None)
assert api_key is not None, "Must declare environment variable: {key_name}".format(
    key_name=api_key_name)
api = api.API(api_key, timeout=5, sleep_time=2)


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n---------------------\nSetting up {} API tests...\n".format("Spoonacular"))
        cls.api = api

    def test_analyze_a_recipe_search_query(self):
        """Test the 'analyze a recipe search query' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'q': 'salmon with fusilli and no nuts'}
        response = self.api.analyze_a_recipe_search_query(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_analyze_recipe_instructions(self):
        """Test the 'analyze recipe instructions' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'instructions': 'Put the garlic in a pan and then add the onion.'}
        response = self.api.analyze_recipe_instructions(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_detect_food_in_text(self):
        """Test the 'detect food in text' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'text': 'I like to eat delicious tacos. Only cheeseburger with cheddar are better than that. But then again, pizza with pepperoni, mushrooms, and tomatoes is so good!'}
        response = self.api.detect_food_in_text(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_extract_recipe_from_website(self):
        """Test the 'extract recipe from website' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'forceExtraction': 'false', 'url': 'http://www.melskitchencafe.com/the-best-fudgy-brownies/'}
        response = self.api.extract_recipe_from_website(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_parse_ingredients(self):
        """Test the 'parse ingredients' endpoint (POST)"""
        msg = "Response status is not 200"
        testArgs = {'ingredientList': '3 oz pork shoulder', 'servings': '2', 'includeNutrition': 'false'}
        response = self.api.parse_ingredients(**testArgs)
        self.assertEqual(response.status_code, 200, msg)
