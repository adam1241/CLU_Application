#pip install pytest if not already installed

import pytest
from LUIS import LUISengine 
from dotenv import load_dotenv
import os

# Loading environment variables 
load_dotenv()

# Retrieving values of environment variables 
app_id = os.getenv('app_id')
subscription_key = os.getenv('subscription_key')
endpoint = os.getenv('endpoint')

# Define the test cases with input texts related to recipe cooking
@pytest.mark.parametrize("query, expected_intent", [
    ("How do I make spaghetti carbonara?", "FindRecipe"),
    ("What are the ingredients for chicken curry?", "ListIngredients"),
    ("Where can I find fresh basil for pesto?", "IngredientSource"),
    ("Is this recipe suitable for beginners?", "DifficultyLevel"),
    ("What can I use as a substitute for eggs?", "Substitutions"),
    ("What is the nutritional information for this dish?", "NutritionalInformation"),
    ("Does this recipe contain any allergens?", "AllergenInformation"),
    ("How would you rate this recipe?", "RecipeRating"),
    ("How long does it take to bake a cake?", "CookTime"),
    ("Can you recommend a recipe for lasagna?", "FindRecipe"),
    ("What spices should I add to my chili?", "ListIngredients"),
    ("Are there any gluten-free options for this dish?", "DietaryRestrictions"),
    ("Where can I buy organic tomatoes?", "IngredientSource"),
    ("How do I grill a steak?", "CookingInstructions"),
    ("Is this recipe suitable for advanced cooks?", "DifficultyLevel"),
    ("What are the calories in this meal?", "NutritionalInformation"),
    ("What's the user rating for this recipe?", "RecipeRating"),
    ("How much time do I need to roast potatoes?", "CookTime"),
    ("How can I make a vegan version of this dish?", "FindRecipe"),
    ("Where can I find locally sourced cheese?", "IngredientSource"),
    ("How do I bake a cake without eggs?", "CookingInstructions"),
    ("Is this recipe suitable for experienced chefs?", "DifficultyLevel"),
    ("What can I use instead of butter in baking?", "Substitutions"),
    ("What are the macros for this meal?", "NutritionalInformation"),
    ("Does this dish contain shellfish?", "AllergenInformation"),
    ("What's the average rating for this recipe?", "RecipeRating"),
    ("How much time is needed to boil pasta?", "CookTime"),
    ("What's the best recipe for chocolate chip cookies?", "FindRecipe"),
    ("Can you list the ingredients for tomato soup?", "ListIngredients"),
    ("Are there any low-sodium options for this dish?", "DietaryRestrictions"),
    ("How do I bake a pie crust?", "CookingInstructions"),
    ("Is this recipe suitable for intermediate cooks?", "DifficultyLevel"),
    ("What can I substitute for sugar in baking?", "Substitutions"),
    ("What are the vitamins in this dish?", "NutritionalInformation"),
    ("Does this dish contain dairy products?", "AllergenInformation"),
    ("What's the highest rating for this recipe?", "RecipeRating"),
    ("How much time does it take to grill chicken?", "CookTime"),
    ("Can you suggest a recipe for beef stew?", "FindRecipe"),
    ("Are there any vegetarian options for this dish?", "DietaryRestrictions"),
    ("Where can I find farm-fresh vegetables?", "IngredientSource"),
    ("How do I roast vegetables in the oven?", "CookingInstructions"),
    ("Is this recipe suitable for children?", "DifficultyLevel"),
    ("What can I use instead of flour in baking?", "Substitutions"),
    ("What are the minerals in this dish?", "NutritionalInformation"),
    ("What's the lowest rating for this recipe?", "RecipeRating"),
    ("How much time do I need to bake bread?", "CookTime"),
    ("Can you recommend a recipe for chicken parmesan?", "FindRecipe"),
    ("What ingredients are in a classic Caesar salad?", "ListIngredients"),
    ("Are there any vegan options for this dish?", "DietaryRestrictions"),
    ("Where can I find organic olive oil?", "IngredientSource"),
    ("Is this recipe suitable for a party?", "DifficultyLevel"),
    ("What can I use instead of eggs in cooking?", "Substitutions"),
    ("What are the protein sources in this dish?", "NutritionalInformation"),
    ("Does this dish contain eggs?", "AllergenInformation"),
    ("What's the most recent rating for this recipe?", "RecipeRating"),
    ("How much time does it take to make pizza dough?", "CookTime"),
    ("Can you suggest a recipe for vegetarian chili?", "FindRecipe"),
    ("What ingredients do I need for guacamole?", "ListIngredients"),
    ("Are there any dairy-free options for this dish?", "DietaryRestrictions"),
    ("Where can I find locally sourced meat?", "IngredientSource"),
    ("Is this recipe suitable for a romantic dinner?", "DifficultyLevel"),
    ("What can I use instead of cream in cooking?", "Substitutions"),
    ("What are the carbohydrates in this dish?", "NutritionalInformation"),
    ("What's the overall rating for this recipe?", "RecipeRating"),
    ("How much time do I need to marinate chicken?", "CookTime"),
    ("Can you recommend a recipe for vegetable stir-fry?", "FindRecipe"),
    ("What ingredients are in a classic margherita pizza?", "ListIngredients"),
    ("Where can I find locally sourced seafood?", "IngredientSource"),
    ("How do I make homemade tomato sauce?", "CookingInstructions"),
    ("Is this recipe suitable for a quick meal?", "DifficultyLevel"),
    ("What can I use instead of oil in cooking?", "Substitutions"),
    ("What are the fats in this dish?", "NutritionalInformation"),
    ("Does this dish contain wheat?", "AllergenInformation"),
    ("What's the most popular rating for this recipe?", "RecipeRating"),
    ("How much time does it take to marinate steak?", "CookTime"),
    ("Can you suggest a recipe for vegetable lasagna?", "FindRecipe"),
    ("What ingredients do I need for a fruit smoothie?", "ListIngredients"),
    ("Where can I find locally sourced honey?", "IngredientSource"),
    ("How do I make homemade pasta dough?", "CookingInstructions"),
    ("Is this recipe suitable for a family dinner?", "DifficultyLevel"),
])
def test_get_intent(query, expected_intent):
    # Mocking the LUIS engine with fake app_id, subscription_key, and endpoint
    clu_client = LUISengine(app_id, subscription_key, endpoint)
    
    # Calling the get_intent method with the provided query
    intent, _ = clu_client.get_intent(query)
    
    # Asserting that the obtained intent matches the expected intent
    assert intent == expected_intent

# Run the tests using the command 'pytest LUIS_tests.py' in the terminal
