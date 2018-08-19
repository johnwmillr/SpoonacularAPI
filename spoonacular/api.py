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
                       "X-Mashape-Host": "spoonacular-recipe-food-nutrition-v1.p.mashape.com"}

    def __init__(self, api_key, timeout=5, sleep_time=1.5, allow_extra_calls=False):
        """ Spoonacular API Constructor

        :param api_key: key provided by Spoonacular (str)
        :param timeout: time before quitting on response (seconds)
        :param sleep_time: time to wait between requests (seconds)
        :param allow_extra_calls: override the API call limit (bool)
        """

        assert api_key != '', 'Must supply a non-empty API key.'
        self.api_key = api_key
        self.session.headers["X-Mashape-Key"] = self.api_key
        self.api_root = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/"
        self.timeout = timeout
        self.sleep_time = max(sleep_time, 1)  # Rate limiting
        self.callsRemaining = self.getRemainingCallsFromApi()
        self.allow_extra_calls = allow_extra_calls

    def _make_request(self, path,
                      method='GET',
                      query_=None,
                      params_=None,
                      json_=None):
        """ Make a request to the API """

        # TODO: I should write a specific NO_API_CALLS_REMAINING error
        assert (self.haveCallsRemaining or self.allow_extra_calls), "No free API calls remaining."
        try:
            uri = self.api_root + path
            response = self.session.request(method, uri,
                                            timeout=self.timeout,
                                            data=query_,
                                            params=params_,
                                            json=json_)
        except socket.timeout as e:
            print("Timeout raised and caught: {}".format(e))
            return

        # Warn user if their API calls are running out
        self.callsRemaining = self.getRemainingCallsFromHeader(response.headers)
        time.sleep(self.sleep_time)  # Enforce rate limiting
        return response

    def getRemainingCallsFromHeader(self, headers):
        """ Extracts the remaining number of API calls from the headers"""
        return {'requests': headers['X-RateLimit-requests-Remaining'],
                'responses': headers['X-RateLimit-results-Remaining'],
                'tinyrequests': headers['X-RateLimit-tinyrequests-Remaining']}

    def getRemainingCallsFromApi(self):
        """ Returns the remaining number of API requests, results, etc. """
        self.callsRemaining = self.getRemainingCallsFromHeader(self.session.request('get', self.api_root).headers)
        return self.callsRemaining

    @property  # Not sure if this should be a property
    def minCallsRemaining(self):
        return min([int(val) for val in self.callsRemaining.values()])

    @property  # Not sure if this should be a property
    def haveCallsRemaining(self):
        """ Returns False if any category of API request has run out """
        return self.minCallsRemaining >= 10

    """ --------------- COMPUTE Endpoints --------------- """

    def classify_a_grocery_product(self, product):
        """ Given a grocery product title, this endpoint allows
            you to detect what basic ingredient it is.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#classify-a-grocery-product
        """
        endpoint = "food/products/classify"
        url_json = product
        return self._make_request(endpoint, method="POST", json_=url_json)

    def classify_cuisine(self, ingredientList, title):
        """ Classify the recipe's cuisine.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#classify-cuisine
        """
        endpoint = "recipes/cuisine"
        url_query = {"ingredientList": ingredientList, "title": title}
        url_params = {}
        return self._make_request(endpoint, method="POST", query_=url_query, params_=url_params)

    def classify_grocery_products_batch(self, products):
        """ Given a set of product jsons, get back classified products.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#classify-grocery-products-(batch)
        """
        endpoint = "food/products/classifyBatch"
        url_json = products
        return self._make_request(endpoint, method="POST", json_=url_json)

    def convert_amounts(self, ingredientName, targetUnit, sourceAmount=None, sourceUnit=None):
        """ Convert amounts like "2 cups of flour to grams".
            https://market.mashape.com/spoonacular/recipe-food-nutrition#convert-amounts
        """
        endpoint = "recipes/convert"
        url_query = {}
        url_params = {"ingredientName": ingredientName, "sourceAmount": sourceAmount, "sourceUnit": sourceUnit, "targetUnit": targetUnit}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def generate_meal_plan(self, diet=None, exclude=None, targetCalories=None, timeFrame=None):
        """ Generate a meal plan with three meals per day (breakfast,
            lunch, and dinner).
            https://market.mashape.com/spoonacular/recipe-food-nutrition#generate-meal-plan
        """
        endpoint = "recipes/mealplans/generate"
        url_query = {}
        url_params = {"diet": diet, "exclude": exclude, "targetCalories": targetCalories, "timeFrame": timeFrame}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def guess_nutrition_by_dish_name(self, title):
        """ Guess the macro nutrients of a dish given its title.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#guess-nutrition-by-dish-name
        """
        endpoint = "recipes/guessNutrition"
        url_query = {}
        url_params = {"title": title}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def map_ingredients_to_grocery_products(self, ingredients, servings):
        """ Map a set of ingredients to products you can buy in
            the grocery store.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#map-ingredients-to-grocery-products
        """
        endpoint = "food/ingredients/map"
        url_json = {"ingredients": ingredients, "servings": servings}
        return self._make_request(endpoint, method="POST", json_=url_json)

    def match_recipes_to_daily_calories(self, targetCalories, timeFrame):
        """ Find multiple recipes that, when added up reach your
            daily caloric needs.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#match-recipes-to-daily-calories
        """
        endpoint = "recipes/mealplans/generate"
        url_query = {}
        url_params = {"targetCalories": targetCalories, "timeFrame": timeFrame}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def quick_answer(self, q):
        """ Answer a nutrition related natural language question.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#quick-answer
        """
        endpoint = "recipes/quickAnswer"
        url_query = {}
        url_params = {"q": q}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def summarize_recipe(self, id):
        """ Summarize the recipe in a short text.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#summarize-recipe
        """
        endpoint = "recipes/{id}/summary".format(id=id)
        url_query = {}
        url_params = {}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def visualize_equipment(self, instructions, defaultCss=None, showBacklink=None, view=None):
        """ Visualize the equipment used to make a recipe.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#visualize-equipment
        """
        endpoint = "recipes/visualizeEquipment"
        url_query = {"defaultCss": defaultCss, "instructions": instructions, "showBacklink": showBacklink, "view": view}
        url_params = {}
        return self._make_request(endpoint, method="POST", query_=url_query, params_=url_params)

    def visualize_ingredients(self, ingredientList, servings, defaultCss=None, measure=None, showBacklink=None, view=None):
        """ Visualize ingredients of a recipe.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#visualize-ingredients
        """
        endpoint = "recipes/visualizeIngredients"
        url_query = {"defaultCss": defaultCss, "ingredientList": ingredientList, "measure": measure, "servings": servings, "showBacklink": showBacklink, "view": view}
        url_params = {}
        return self._make_request(endpoint, method="POST", query_=url_query, params_=url_params)

    def visualize_price_breakdown(self, ingredientList, servings, defaultCss=None, mode=None, showBacklink=None):
        """ Visualize the price breakdown of a recipe.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#visualize-price-breakdown
        """
        endpoint = "recipes/visualizePriceEstimator"
        url_query = {"defaultCss": defaultCss, "ingredientList": ingredientList, "mode": mode, "servings": servings, "showBacklink": showBacklink}
        url_params = {}
        return self._make_request(endpoint, method="POST", query_=url_query, params_=url_params)

    def visualize_recipe_nutrition(self, ingredientList, servings, defaultCss=None, showBacklink=None):
        """ Visualize a recipe's nutritional information.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#visualize-recipe-nutrition
        """
        endpoint = "recipes/visualizeNutrition"
        url_query = {"defaultCss": defaultCss, "ingredientList": ingredientList, "servings": servings, "showBacklink": showBacklink}
        url_params = {}
        return self._make_request(endpoint, method="POST", query_=url_query, params_=url_params)

    def visualize_recipe_nutrition_by_id(self, id, defaultCss=None):
        """ Visualize a recipe's nutrition data.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#visualize-recipe-nutrition-by-id
        """
        endpoint = "recipes/{id}/nutritionWidget".format(id=id)
        url_query = {}
        url_params = {"defaultCss": defaultCss}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    """ --------------- SEARCH Endpoints --------------- """

    def autocomplete_ingredient_search(self, query, intolerances=None, metaInformation=None, number=None):
        """ Autocomplete a search for an ingredient.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#autocomplete-ingredient-search
        """
        endpoint = "food/ingredients/autocomplete"
        url_query = {}
        url_params = {"intolerances": intolerances, "metaInformation": metaInformation, "number": number, "query": query}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def autocomplete_recipe_search(self, query, number=None):
        """ Autocomplete a partial input to possible recipe names.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#autocomplete-recipe-search
        """
        endpoint = "recipes/autocomplete"
        url_query = {}
        url_params = {"number": number, "query": query}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_comparable_products(self, upc):
        """ Find comparable products to the given one.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-comparable-products
        """
        endpoint = "food/products/upc/{upc}/comparable".format(upc=upc)
        url_query = {}
        url_params = {}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_dish_pairing_for_wine(self, wine):
        """ Get a dish that goes well with a given wine.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-dish-pairing-for-wine
        """
        endpoint = "food/wine/dishes"
        url_query = {}
        url_params = {"wine": wine}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_ingredient_substitutes(self, ingredientName):
        """ Get ingredient substitutes by ingredient name.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-ingredient-substitutes
        """
        endpoint = "food/ingredients/substitutes"
        url_query = {}
        url_params = {"ingredientName": ingredientName}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_ingredient_substitutes_by_id(self, id):
        """ Search for substitutes for a given ingredient.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-ingredient-substitutes-by-id
        """
        endpoint = "food/ingredients/{id}/substitutes".format(id=id)
        url_query = {}
        url_params = {}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_random_recipes(self, limitLicense=None, number=None, tags=None):
        """ Find random (popular) recipes.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-random-recipes
        """
        endpoint = "recipes/random"
        url_query = {}
        url_params = {"limitLicense": limitLicense, "number": number, "tags": tags}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_similar_recipes(self, id):
        """ Find recipes which are similar to the given one.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-similar-recipes
        """
        endpoint = "recipes/{id}/similar".format(id=id)
        url_query = {}
        url_params = {}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_wine_description(self, wine):
        """ Get the description of a certain wine, e.g. "malbec",
            "riesling", or "merlot".
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-wine-description
        """
        endpoint = "food/wine/description"
        url_query = {}
        url_params = {"wine": wine}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_wine_pairing(self, food, maxPrice=None):
        """ Find a wine that goes well with a food. Food can be
            a dish name ("steak"), an ingredient name ("salmon"),
            or a cuisine ("italian").
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-wine-pairing
        """
        endpoint = "food/wine/pairing"
        url_query = {}
        url_params = {"food": food, "maxPrice": maxPrice}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_wine_recommendation(self, wine, maxPrice=None, minRating=None, number=None):
        """ Get a specific wine recommendation (concrete product)
            for a given wine, e.g. "merlot".
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-wine-recommendation
        """
        endpoint = "food/wine/recommendation"
        url_query = {}
        url_params = {"maxPrice": maxPrice, "minRating": minRating, "number": number, "wine": wine}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def search_grocery_products_by_upc(self, upc):
        """ Get information about a food product given its UPC.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#search-grocery-products-by-upc
        """
        endpoint = "food/products/upc/{upc}".format(upc=upc)
        url_query = {}
        url_params = {}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def search_recipes_by_ingredients(self, ingredients, fillIngredients=None, limitLicense=None, number=None, ranking=None):
        """ Find recipes that use as many of the given ingredients
            as possible and have as little as possible missing
            ingredients. This is a whats in your fridge API endpoint.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#search-recipes-by-ingredients
        """
        endpoint = "recipes/findByIngredients"
        url_query = {}
        url_params = {"fillIngredients": fillIngredients, "ingredients": ingredients, "limitLicense": limitLicense, "number": number, "ranking": ranking}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def search_site_content(self, query):
        """ Search spoonacular's site content. You'll be able to
            find everything that you could also find using the
            search suggests on spoonacular.com. This is a suggest
            API so you can send partial strings as queries.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#search-site-content
        """
        endpoint = "food/site/search"
        url_query = {}
        url_params = {"query": query}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    """ --------------- CHAT Endpoints --------------- """

    def get_conversation_suggests(self, query, number=None):
        """ This endpoint returns suggestions for things the user
            can say or ask the chat bot.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-conversation-suggests
        """
        endpoint = "food/converse/suggest"
        url_query = {}
        url_params = {"number": number, "query": query}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def talk_to_a_chatbot(self, text, contextId=None):
        """ This endpoint can be used to have a conversation about
            food with the spoonacular chat bot. Use the chat
            suggests endpoint to show your user what he or she
            can say.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#talk-to-a-chatbot
        """
        endpoint = "food/converse"
        url_query = {}
        url_params = {"contextId": contextId, "text": text}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    """ --------------- DATA Endpoints --------------- """

    def get_a_random_food_joke(self):
        """ Get a random joke that includes or is about food.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-a-random-food-joke
        """
        endpoint = "food/jokes/random"
        url_query = {}
        url_params = {}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_analyzed_recipe_instructions(self, id, stepBreakdown=None):
        """ Get an analyzed breakdown of a recipe's instructions.
            Each step is enriched with the ingredients and the
            equipment that is used.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-analyzed-recipe-instructions
        """
        endpoint = "recipes/{id}/analyzedInstructions".format(id=id)
        url_query = {}
        url_params = {"stepBreakdown": stepBreakdown}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_food_information(self, id, amount=None, unit=None):
        """ Get information about a certain food (ingredient).
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-food-information
        """
        endpoint = "food/ingredients/{id}/information".format(id=id)
        url_query = {}
        url_params = {"amount": amount, "unit": unit}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_product_information(self, id):
        """ Get information about a packaged food product.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-product-information
        """
        endpoint = "food/products/{id}".format(id=id)
        url_query = {}
        url_params = {}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_random_food_trivia(self):
        """ Returns random food trivia.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-random-food-trivia
        """
        endpoint = "food/trivia/random"
        url_query = {}
        url_params = {}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_recipe_information(self, id, includeNutrition=None):
        """ Get information about a recipe.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-recipe-information
        """
        endpoint = "recipes/{id}/information".format(id=id)
        url_query = {}
        url_params = {"includeNutrition": includeNutrition}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def get_recipe_information_bulk(self, ids, includeNutrition=None):
        """ Get information about multiple recipes at once. That
            is equivalent of calling the Get Recipe Information
            endpoint multiple times but is faster. Note that
            each returned recipe counts as one request.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#get-recipe-information-bulk
        """
        endpoint = "recipes/informationBulk"
        url_query = {}
        url_params = {"ids": ids, "includeNutrition": includeNutrition}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    """ --------------- EXTRACT Endpoints --------------- """

    def analyze_a_recipe_search_query(self, q):
        """ Parse a recipe search query to find out its intention.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#analyze-a-recipe-search-query
        """
        endpoint = "recipes/queries/analyze"
        url_query = {}
        url_params = {"q": q}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def analyze_recipe_instructions(self, instructions):
        """ Extract ingredients and equipment from the recipe instruction
            steps.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#analyze-recipe-instructions
        """
        endpoint = "recipes/analyzeInstructions"
        url_query = {"instructions": instructions}
        url_params = {}
        return self._make_request(endpoint, method="POST", query_=url_query, params_=url_params)

    def detect_food_in_text(self, text):
        """ Detect ingredients and dishes in texts.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#detect-food-in-text
        """
        endpoint = "food/detect"
        url_query = {"text": text}
        url_params = {}
        return self._make_request(endpoint, method="POST", query_=url_query, params_=url_params)

    def extract_recipe_from_website(self, url, forceExtraction=None):
        """ Extract recipe data from a recipe blog or Web page.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#extract-recipe-from-website
        """
        endpoint = "recipes/extract"
        url_query = {}
        url_params = {"forceExtraction": forceExtraction, "url": url}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)

    def parse_ingredients(self, ingredientList, servings=1, includeNutrition=None):
        """ Extract an ingredient from plain text.
            https://market.mashape.com/spoonacular/recipe-food-nutrition#parse-ingredients
        """
        endpoint = "recipes/parseIngredients"
        url_query = {"ingredientList": ingredientList, "servings": servings}
        url_params = {"includeNutrition": includeNutrition}
        return self._make_request(endpoint, method="POST", query_=url_query, params_=url_params)
