# spoonacular 🥄🍎
---
[![Build Status](https://travis-ci.org/johnwmillr/SpoonacularAPI.svg?branch=master)](https://travis-ci.org/johnwmillr/SpoonacularAPI)
![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)

Want to parse a list of [ingredients](https://rapidapi.com/spoonacular/api/Recipe%20-%20Food%20-%20Nutrition/functions/Parse%20Ingredients) within a recipe? Or are you looking for a random [food joke](https://rapidapi.com/spoonacular/api/Recipe%20-%20Food%20-%20Nutrition/functions/Get%20a%20Random%20Food%20Joke)?

`spoonacular` provides a simple Python interface to the marvelous food and recipes API from [Spoonacular](https://spoonacular.com/).

## Installation
Clone the repository and install the ackage with these steps:
1. Clone this repo:
`$git clone https://github.com/johnwmillr/SpoonacularAPI.git`
2. Enter the cloned directory:
`$cd SpoonacularAPI`
3. Install:
`$python setup.py install`

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
