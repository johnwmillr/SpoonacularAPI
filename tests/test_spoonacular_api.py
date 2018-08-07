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

    """ EXTRACT Endpoints """

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

    """ SEARCH Endpoints """

    def test_autocomplete_ingredient_search(self):
        """Test the 'autocomplete ingredient search' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'intolerances': 'egg', 'metaInformation': 'false', 'number': '10', 'query': 'appl'}
        response = self.api.autocomplete_ingredient_search(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_autocomplete_recipe_search(self):
        """Test the 'autocomplete recipe search' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'number': '10', 'query': 'chicken'}
        response = self.api.autocomplete_recipe_search(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_comparable_products(self):
        """Test the 'get comparable products' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'upc': '033698816271'}
        response = self.api.get_comparable_products(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_dish_pairing_for_wine(self):
        """Test the 'get dish pairing for wine' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'wine': 'merlot'}
        response = self.api.get_dish_pairing_for_wine(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_ingredient_substitutes(self):
        """Test the 'get ingredient substitutes' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'ingredientName': 'butter'}
        response = self.api.get_ingredient_substitutes(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_ingredient_substitutes_by_id(self):
        """Test the 'get ingredient substitutes by id' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'id': '1001'}
        response = self.api.get_ingredient_substitutes_by_id(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_random_recipes(self):
        """Test the 'get random recipes' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'limitLicense': 'false', 'number': '1', 'tags': 'vegetarian,dessert'}
        response = self.api.get_random_recipes(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_similar_recipes(self):
        """Test the 'get similar recipes' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'id': '156992'}
        response = self.api.get_similar_recipes(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_wine_description(self):
        """Test the 'get wine description' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'wine': 'malbec'}
        response = self.api.get_wine_description(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_wine_pairing(self):
        """Test the 'get wine pairing' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'food': 'steak', 'maxPrice': '50'}
        response = self.api.get_wine_pairing(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_get_wine_recommendation(self):
        """Test the 'get wine recommendation' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'maxPrice': '50', 'minRating': '0.7', 'number': '3', 'wine': 'merlot'}
        response = self.api.get_wine_recommendation(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_search_grocery_products_by_upc(self):
        """Test the 'search grocery products by upc' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'upc': '041631000564'}
        response = self.api.search_grocery_products_by_upc(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_search_recipes_by_ingredients(self):
        """Test the 'search recipes by ingredients' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'fillIngredients': 'false', 'ingredients': 'apples,flour,sugar', 'limitLicense': 'false', 'number': '5', 'ranking': '1'}
        response = self.api.search_recipes_by_ingredients(**testArgs)
        self.assertEqual(response.status_code, 200, msg)

    def test_search_site_content(self):
        """Test the 'search site content' endpoint (GET)"""
        msg = "Response status is not 200"
        testArgs = {'query': 'past'}
        response = self.api.search_site_content(**testArgs)
        self.assertEqual(response.status_code, 200, msg)
