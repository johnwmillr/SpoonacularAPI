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
    session.headers = {
        "Application": "PySpoon",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"}

    def __init__(self, api_key, format_='json', timeout=5, sleep_time=1.5):
        """ Spoonacular API Constructor

        :param api_key: key provided by Spoonacular
        :param timeout: time before quitting on response (seconds)
        :param sleep_time: time to wait between requests
        """

        assert api_key != '', 'Must supply a non-empty API key.'
        self.API_KEY = api_key
        self.session.headers["X-Mashape-Key"] = self.API_KEY
        self.api_root = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/"
        self.timeout = timeout
        self._sleep_time = sleep_time

    def _make_request(self, path, method='GET', params_=None):
        """Make a request to the API"""

        uri = self.api_root + path
        if params_:
            params_['text_format'] = self.FORMAT
        else:
            params_ = {'text_format': self.FORMAT}

        # Make the request
        try:
            response = self.session.request(method.upper(), uri,
                                            timeout=self.timeout,
                                            params=params_)
        except socket.timeout as e:
            print("Timeout raised and caught: {}".format(e))

        assert response.status_code == 200, "API response is not 200: {r}".format(r=response.reason)
        time.sleep(self.sleep_time)
        return response.json()['response']

    def parse_ingredients(self, ingredientList, servings=1, includeNutrition=False):
        endpoint = "recipes/parseIngredients?includeNutrition={val}".format(val=includeNutrition)
        params = {"ingredientList": ingredientList, "servings": servings}
        return self._make_request(endpoint, method='POST', params_=params)
