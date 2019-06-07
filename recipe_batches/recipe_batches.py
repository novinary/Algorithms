#!/usr/bin/python

# Check if length of recipe is greater than length of ingredients, if it's true then return 0
# For each item in recipe and ingredients, get a new count by diving no. of ingredient items by no. of recipe items
# Check if initial count of 0 is less than new count or if count is equal to 0 then set initial count as new count and return count

import math

def recipe_batches(recipe, ingredients):
  count = 0

  if len(recipe) > len(ingredients):    
    return 0

  # print(len(recipe),(ingredients))

  for item in recipe and ingredients:
    max = ingredients[item] // recipe[item]    #floor division to get the division result
    # print(max)

    if max < count or count == 0:
      count = max
    return count

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'sugar': 48, 'flour': 51}
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))