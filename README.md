# Python wrapper for the Spoonacular API 🥄🍎
---
[![Build Status](https://travis-ci.org/johnwmillr/SpoonacularAPI.svg?branch=master)](https://travis-ci.org/johnwmillr/SpoonacularAPI)
![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)

This Python wrapper makes it easy to download data from [Spoonacular's](https://spoonacular.com/) marvelous food and recipes API.

I'm relying heavily on my [DocScraper](https://github.com/johnwmillr/DocScraper) code to generate the Python files in this wrapper. I'll be adding support for additional endpoints as I have time.

## Usage
```python
import spoonacular as sp
api = sp.API("your_api_key_here")

# Parse an ingredient
response = api.parse_ingredients("3.5 cups King Arthur flour")
data = response.json()[0]
print(data['name'])

# Detect text for mentions of food
response = api.detect_food_in_text("I really want a cheeseburger.")
data = response.json()[0]
print(data)
```

## Documentation
 - [Spoonacular website](https://spoonacular.com/food-api)
 - [RapidAPI](https://rapidapi.com/spoonacular/api/Recipe%20-%20Food%20-%20Nutrition)
 - [DocScraper](https://github.com/johnwmillr/DocScraper)

## Collaboration
Please feel free to collaborate with a pull request or by opening an issue.
