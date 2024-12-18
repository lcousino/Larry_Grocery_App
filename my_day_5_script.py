# Day 5 - Functions and Modules
# =============================
# def my_first_function():
#     print("This is my first function")

# my_first_function()
# --------------------------

# # Function Exercises
# # 1
# def welcome_message():
#     print("Welcome to Larry's Shopping Cart")

# welcome_message()

# #2
# def favorite_food():
#     print("My favorite food is pasta!")
# favorite_food()

# # 3
# def show_sum():
#     print(5 + 10)
# show_sum()
# ------------------------------

# Parameters and Values
# Define function
# def print_grocert_list_items(grocery_list):
#     # 4 - Improve function
#     print("We need to buy the following: ")
#     for item in grocery_list:
#         print(item)

# # Test list
# fruits_grocery_list = ['apple', 'banana', 'grapes']
# veggie_list = ['kale', 'eggplant', 'spinach', 'broccoli']
# misc_items = ['shampoo', 'dishsoap', 'sponges']

# # Call function
# # Test 1
# print_grocert_list_items(fruits_grocery_list)
# # Test 2
# print_grocert_list_items(veggie_list)
# # Test 3
# print_grocert_list_items(misc_items)

# 4 - see above

# # 5 
# #  Extend functionality with added parameter
# def print_grocert_list_items(grocery_list, nice_to_have_list=None):
#     # 4 - Improve function
#     print("We need to buy the following: ")
#     for item in grocery_list:
#         print(item)

# # Test list
# fruits_grocery_list = ['apple', 'banana', 'grapes']
# veggie_list = ['kale', 'eggplant', 'spinach', 'broccoli']
# misc_items = ['shampoo', 'dishsoap', 'sponges']

# # Call function
# print_grocert_list_items(fruits_grocery_list)

# # 6 & 7
# #  Extend functionality with added parameter
# def print_grocert_list_items(grocery_list, nice_to_have_list=None):
#     # 4 - Improve function
#     print("We need to buy the following: ")
#     for item in grocery_list:
#         print(item)
#     if nice_to_have_list != None:
#         print("\nIf possible, it would be nice to buy the following as well: ")
#         for item in nice_to_have_list:
#             print(item)

# # Test list
# fruits_grocery_list = ['apple', 'banana', 'grapes']
# veggie_list = ['kale', 'eggplant', 'spinach', 'broccoli']
# misc_items = ['shampoo', 'dishsoap', 'sponges']
# desserts_list = ['tiramisu', 'ice cream', 'candy bar']

# # Call function
# print_grocert_list_items(fruits_grocery_list, desserts_list)

# More examples
# def check_availability_in_store(item_name, stock_staus, store_name):
#     if stock_staus:
#         print(f"{item_name} are available at {store_name}.")
#     else:
#         print(f"{item_name} is out of stock at {store_name}.")

# # check_availability("Bananas", True)
# # check_availability("Milk", False)
# check_availability_in_store("Apples", True, "Super Mercado")
# check_availability_in_store("Eggs", False, "Organic Foods")

# def check_freshness(item_name, days_since_purchase):
#     if days_since_purchase <= 3:
#         return f"{item_name} is fresh."
#     else:
#         return f"{item_name} might be past it's prime."

# message = check_freshness("Lettuce", 3)
# print(message)

# print(check_freshness("Tomatoes", 7))
# ------------------------------------------
# Practice Exercises
# # 1
# def find_item(item_name, is_available):
#     if is_available:
#         return f"{item_name} is available."
#     else:
#         return f"{item_name} is not available."

# message = find_item("Orange Juice", True)
# print(message)
# message = find_item("Bread", False)
# print(message)

# # 2
# def favorite_snack(snack_name, quantity_left):
#     if quantity_left:
#         return f"You have some {snack_name} left to enjoy!"
#     else:
#         return f"You are out of {snack_name}."

# print(favorite_snack("Chips", 3))
# print(favorite_snack("Cookies", 0))

# # 3
# def item_location(item_name, store_section):
#     return f"You can find {item_name} in the {store_section}."

# print(item_location("Milke", "Dairy Aisle"))
# print(item_location("Apples", "Produce Section"))
# -----------------------------------
# Scope and Lifetime of Variables
# 1
# # Global Variable
# food = "Pizza"

# def favorite_food():
#     food = "Sushi" # <--- Local variable
#     print("Local food: ", food)

# favorite_food()
# print("Global food: ", food) 

# # 2 Variable lifetime in Functions
# def counter():
#     count = 0 # <--- Local variable
#     count += 1
#     print("Count: ", count)

# counter()
# counter()

# # 3 Combining Scope and Lifetime
# user_name = "Larry" # <-- Global variable

# def name_change():
#     user_name = "LCousino" # <-- Local variable
#     print("Inside the function: ", user_name)

# name_change()
# print("Outside function: ", user_name)
# ---------------------------------------

# Modules
# Key concepts
# # import built in modules
# import math # built in module
# print(math.sqrt(16))  # Output is 4.0

# Ex 1 Custome Modules completed with files module_a.py and module_b.py

# # 2
# from datetime import date
# print(date.today())