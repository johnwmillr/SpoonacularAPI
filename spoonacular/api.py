# Spoonacular API
# Copyright 2018 John W. Miller
# See LICENSE for details.

"""
API details and documentation: https://spoonacular.com/food-api
"""

import requests
import socket
import time


class API(object):
    """Spoonacular API"""

    # Create a persistent requests connection
    session = requests.Session()
    session.headers = {"Application": "PySpoon",
                       "Content-Type": "application/x-www-form-urlencoded",
                       "Accept": "application/json"}

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        """ Spoonacular API Constructor

        :param api_key: key provided by Spoonacular
        :param timeout: time before quitting on response (seconds)
        :param sleep_time: time to wait between requests (seconds)
        """

        assert api_key != '', 'Must supply a non-empty API key.'
        self.API_KEY = api_key
        self.session.headers["X-Mashape-Key"] = self.API_KEY
        self.api_root = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/"
        self.timeout = timeout
        self.sleep_time = max(sleep_time, 1)  # Rate limiting
        self.calls_remaining = None  # TODO: make this work good

    def _make_request(self, path, method='GET', query_=None, params_=None):
        """Make a request to the API"""

        assert (self.calls_remaining is None or self.calls_remaining > 1), "No free API calls remaining."
        try:
            uri = self.api_root + path
            response = self.session.request(method, uri,
                                            timeout=self.timeout,
                                            data=query_,
                                            params=params_)
        except socket.timeout as e:
            print("Timeout raised and caught: {}".format(e))
            return

        # Warn user if their free API calls are running out
        self.calls_remaining = int(response.headers['X-RateLimit-requests-Remaining'])
        if self.calls_remaining < 5:
            print('\n\n---*** *** *** *** WARNING *** *** *** ***---')
            print('      ONLY {n} FREE API CALLS REMAINING'.format(n=self.calls_remaining))
            print('---*** *** *** *** WARNING *** *** *** ***---\n\n')

        # Check for bad response from API
        if response.status_code != 200:
            print("\n*WARNING*:\nAPI response is not 200: {r}".format(r=response.reason))

        time.sleep(self.sleep_time)  # Enforce rate limiting
        return response

    """ EXTRACT Endpoints """

    def analyze_a_recipe_search_query(self, q):
        """ Parse a recipe search query to find out its intention.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#analyze-a-recipe-search-query
        """
        endpoint = "recipes/queries/analyze"
        query = {}
        params = {"q": q}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def analyze_recipe_instructions(self, instructions):
        """ Extract ingredients and equipment from the recipe instruction
            steps.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#analyze-recipe-instructions
        """
        endpoint = "recipes/analyzeInstructions"
        query = {"instructions": instructions}
        params = {}
        return self._make_request(endpoint, method="POST", query_=query, params_=params)

    def detect_food_in_text(self, text):
        """ Detect ingredients and dishes in texts.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#detect-food-in-text
        """
        endpoint = "food/detect"
        query = {"text": text}
        params = {}
        return self._make_request(endpoint, method="POST", query_=query, params_=params)

    def extract_recipe_from_website(self, url, forceExtraction=None):
        """ Extract recipe data from a recipe blog or Web page.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#extract-recipe-from-website
        """
        endpoint = "recipes/extract"
        query = {}
        params = {"forceExtraction": forceExtraction, "url": url}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def parse_ingredients(self, ingredientList, servings, includeNutrition=None):
        """ Extract an ingredient from plain text.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#parse-ingredients
        """
        endpoint = "recipes/parseIngredients"
        query = {"ingredientList": ingredientList, "servings": servings}
        params = {"includeNutrition": includeNutrition}
        return self._make_request(endpoint, method="POST", query_=query, params_=params)

    """ SEARCH Endpoints """

    def autocomplete_ingredient_search(self, query, intolerances=None, metaInformation=None, number=None):
        """ Autocomplete a search for an ingredient.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#autocomplete-ingredient-search
        """
        endpoint = "food/ingredients/autocomplete"
        query = {}
        params = {"intolerances": intolerances, "metaInformation": metaInformation, "number": number, "query": query}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def autocomplete_recipe_search(self, query, number=None):
        """ Autocomplete a partial input to possible recipe names.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#autocomplete-recipe-search
        """
        endpoint = "recipes/autocomplete"
        query = {}
        params = {"number": number, "query": query}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def get_comparable_products(self, upc):
        """ Find comparable products to the given one.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-comparable-products
        """
        endpoint = "food/products/upc/{upc}/comparable"
        query = {}
        params = {"upc": upc}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def get_dish_pairing_for_wine(self, wine):
        """ Get a dish that goes well with a given wine.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-dish-pairing-for-wine
        """
        endpoint = "food/wine/dishes"
        query = {}
        params = {"wine": wine}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def get_ingredient_substitutes(self, ingredientName):
        """ Get ingredient substitutes by ingredient name.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-ingredient-substitutes
        """
        endpoint = "food/ingredients/substitutes"
        query = {}
        params = {"ingredientName": ingredientName}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def get_ingredient_substitutes_by_id(self, id):
        """ Search for substitutes for a given ingredient.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-ingredient-substitutes-by-id
        """
        endpoint = "food/ingredients/{id}/substitutes"
        query = {}
        params = {"id": id}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def get_random_recipes(self, limitLicense=None, number=None, tags=None):
        """ Find random (popular) recipes.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-random-recipes
        """
        endpoint = "recipes/random"
        query = {}
        params = {"limitLicense": limitLicense, "number": number, "tags": tags}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def get_similar_recipes(self, id):
        """ Find recipes which are similar to the given one.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-similar-recipes
        """
        endpoint = "recipes/{id}/similar"
        query = {}
        params = {"id": id}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def get_wine_description(self, wine):
        """ Get the description of a certain wine, e.g. "malbec" or "riesling"
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-wine-description
        """
        endpoint = "food/wine/description"
        query = {}
        params = {"wine": wine}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def get_wine_pairing(self, food, maxPrice=None):
        """ Find a wine that goes well with a food. Food can be a dish name ("steak"),
            an ingredient name ("salmon"), or a cuisine ("italian").
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-wine-pairing
        """
        endpoint = "food/wine/pairing"
        query = {}
        params = {"food": food, "maxPrice": maxPrice}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def get_wine_recommendation(self, wine, maxPrice=None, minRating=None, number=None):
        """ Get a specific wine recommendation (concrete product) for a given wine, e.g.
            "merlot".
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-wine-recommendation
        """
        endpoint = "food/wine/recommendation"
        query = {}
        params = {"maxPrice": maxPrice, "minRating": minRating, "number": number, "wine": wine}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def search_grocery_products_by_upc(self, upc):
        """ Get information about a food product given its UPC.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#search-grocery-products-by-upc
        """
        endpoint = "food/products/upc/{upc}"
        query = {}
        params = {"upc": upc}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def search_recipes_by_ingredients(self, ingredients, fillIngredients=None, limitLicense=None, number=None, ranking=None):
        """ Find recipes that use as many of the given ingredients as possible and have
            as little as possible missing ingredients. This is a whats in your fridge
            API endpoint.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#search-recipes-by-ingredients
        """
        endpoint = "recipes/findByIngredients"
        query = {}
        params = {"fillIngredients": fillIngredients, "ingredients": ingredients, "limitLicense": limitLicense, "number": number, "ranking": ranking}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)

    def search_site_content(self, query):
        """ Search spoonacular's site content. You'll be able to find everything that
            you could also find using the search suggests on spoonacular.com. This
            is a suggest API so you can send partial strings as queries.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#search-site-content
        """
        endpoint = "food/site/search"
        query = {}
        params = {"query": query}
        return self._make_request(endpoint, method="GET", query_=query, params_=params)
