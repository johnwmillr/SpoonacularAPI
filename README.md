# 🥄 spoonacular 🥄
---
[![Build Status](https://travis-ci.org/johnwmillr/SpoonacularAPI.svg?branch=master)](https://travis-ci.org/johnwmillr/SpoonacularAPI)
[![PyPI version](https://badge.fury.io/py/spoonacular.svg)](https://pypi.org/project/spoonacular/)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/spoonacular/)

Want to parse a list of [ingredients](https://rapidapi.com/spoonacular/api/Recipe%20-%20Food%20-%20Nutrition/functions/Parse%20Ingredients) within a recipe? Or are you looking for a random [food joke](https://rapidapi.com/spoonacular/api/Recipe%20-%20Food%20-%20Nutrition/functions/Get%20a%20Random%20Food%20Joke)? These are just two of many endpoints provided by the marvelous [Spoonacular](https://spoonacular.com/) food and recipes API. `spoonacular` provides a simple Python interface to this API.

## Installation
The easiest way to start using this package is to install it via [PyPI](https://pypi.python.org/pypi/spoonacular) using `pip`:

`$pip install spoonacular`

Thank you for [@sebbekarlsson](https://github.com/sebbekarlsson) for transferring ownership of the original PyPI package name.

If you'd prefer to clone and install the repository manually, follow these steps:

1. Clone this repo:
`$git clone https://github.com/johnwmillr/SpoonacularAPI.git`
2. Enter the cloned directory:
`$cd SpoonacularAPI`
3. Install:
    `$python setup.py install`

## Usage

### API Key

You'll need to sign up for an account on [RapidAPI](https://rapidapi.com/spoonacular/api/Recipe%20-%20Food%20-%20Nutrition/pricing) to start using `spoonacular`. Spoonacular is a freemium API, so you'll be able to start with 50 free calls a day. Registration requires a credit card number even for the free plan, because users are charged a small amount per call if they go over the daily limit. This package has a basic system in place to try and prevent overrage charges.

### Examples

```python
import spoonacular as sp
api = sp.API("your_api_key_here")

# Parse an ingredient
response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1)
data = response.json()
print(data[0]['name'])
>>>"flour"

# Detect text for mentions of food
response = api.detect_food_in_text("I really want a cheeseburger.")
data = response.json()
print(data['annotations'][0])
>>>{"annotation": "cheeseburger", "tag":"dish"}

# Get a random food joke
response = api.get_a_random_food_joke()
data = response.json()
print(data['text'])
>>>"People are a lot less judgy when you say you ate an 'avocado salad' instead of a bowl of guacamole."
```

## Documentation
 - [Spoonacular website](https://spoonacular.com/food-api)
 - [RapidAPI](https://rapidapi.com/spoonacular/api/Recipe%20-%20Food%20-%20Nutrition)
 - [DocScraper](https://github.com/johnwmillr/DocScraper)

## Collaboration
Please feel free to collaborate with a pull request or by opening an issue.
