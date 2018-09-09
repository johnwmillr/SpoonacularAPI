# Spoonacular API
# Copyright 2018 John W. Miller
# See LICENSE for details.

"""
API details and documentation: https://spoonacular.com/food-api
"""

endpoint_quotas = {
  "classify_a_grocery_product": {
    "name": "Classify a Grocery Product",
    "requests": {
      "amount": "0",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "1",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "classify_cuisine": {
    "name": "Classify Cuisine",
    "requests": {
      "amount": "0",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "1",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "classify_grocery_products_batch": {
    "name": "Classify Grocery Products (Batch)",
    "requests": {
      "amount": "0",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "1",
      "qualifier": "per product"
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "convert_amounts": {
    "name": "Convert Amounts",
    "requests": {
      "amount": "0",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "1",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "create_recipe_card": {
    "name": "Create Recipe Card",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "generate_meal_plan": {
    "name": "Generate Meal Plan",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "map_ingredients_to_grocery_products": {
    "name": "Map Ingredients to Grocery Products",
    "requests": {
      "amount": "1",
      "qualifier": "per ingredient"
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "match_recipes_to_daily_calories": {
    "name": "Match Recipes to Daily Calories",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "quick_answer": {
    "name": "Quick Answer",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "summarize_recipe": {
    "name": "Summarize Recipe",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "visualize_equipment": {
    "name": "Visualize Equipment",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "visualize_ingredients": {
    "name": "Visualize Ingredients",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "visualize_recipe_nutrition": {
    "name": "Visualize Recipe Nutrition",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "visualize_product_nutrition": {
    "name": "Visualize Product Nutrition",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "visualize_menu_item_nutrition": {
    "name": "Visualize Menu Item Nutrition",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "visualize_price_breakdown": {
    "name": "Visualize Price Breakdown",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "analyze_a_recipe_search_query": {
    "name": "Analyze a Recipe Search Query",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "analyze_recipe_instructions": {
    "name": "Analyze Recipe Instructions",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "detect_food_in_text": {
    "name": "Detect Food in Text",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "extract_recipe_from_website": {
    "name": "Extract Recipe from Website",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "parse_ingredients": {
    "name": "Parse Ingredients",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per parsed ingredient"
    }
  },
  "autocomplete_ingredient_search": {
    "name": "Autocomplete Ingredient Search",
    "requests": {
      "amount": "0",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "1",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "autocomplete_recipe_search": {
    "name": "Autocomplete Recipe Search",
    "requests": {
      "amount": "0",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "1",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_ingredient_substitutes": {
    "name": "Get Ingredient Substitutes",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_ingredient_substitutes_by_id": {
    "name": "Get Ingredient Substitutes by Id",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_random_recipes": {
    "name": "Get Random Recipes",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "get_similar_recipes": {
    "name": "Get Similar Recipes",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "search_food_videos": {
    "name": "Search Food Videos",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "search_menu_items": {
    "name": "Search Menu Items",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "search_grocery_products": {
    "name": "Search Grocery Products",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "search_grocery_products_by_upc": {
    "name": "Search Grocery Products by UPC",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "search_recipes": {
    "name": "Search Recipes",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "search_recipes_by_ingredients": {
    "name": "Search Recipes by Ingredients",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "search_recipes_by_nutrients": {
    "name": "Search Recipes by Nutrients",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "search_recipes_complex": {
    "name": "Search Recipes Complex",
    "requests": {
      "amount": "3",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "1",
      "qualifier": "per result"
    }
  },
  "search_site_content": {
    "name": "Search Site Content",
    "requests": {
      "amount": "0",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "1",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_a_random_food_joke": {
    "name": "Get a Random Food Joke",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_analyzed_recipe_instructions": {
    "name": "Get Analyzed Recipe Instructions",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_food_information": {
    "name": "Get Food Information",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_product_information": {
    "name": "Get Product Information",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_menu_item_information": {
    "name": "Get Menu Item Information",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_random_food_trivia": {
    "name": "Get Random Food Trivia",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_recipe_information": {
    "name": "Get Recipe Information",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_recipe_information_bulk": {
    "name": "Get Recipe Information Bulk",
    "requests": {
      "amount": "1",
      "qualifier": "per recipe"
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "get_conversation_suggests": {
    "name": "Get Conversation Suggests",
    "requests": {
      "amount": "0",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "1",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  },
  "talk_to_a_chatbot": {
    "name": "Talk to a chatbot",
    "requests": {
      "amount": "1",
      "qualifier": ""
    },
    "tinyrequests": {
      "amount": "0",
      "qualifier": ""
    },
    "results": {
      "amount": "0",
      "qualifier": ""
    }
  }
}
