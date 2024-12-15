# # print("Hello, World!")

# # Day 2 Exercise
# # =======================================================
# # Exercise 1
# bread = 3.25
# steak = 8.40
# milk = 2.51
# total_cost = bread + steak + milk

# print(f"Your total is: ${total_cost}")
# # =======================================================
# # Exercise 2

# # Obtain store name from user
# store_name = input("What's the name of your favorite grocery store?")

# # Welcome user to their favorite store
# print(f"Welcome to {store_name}!")
# # ========================================================
# # Exercise 3
# milk = int("3")
# bread = 2.5
# total = str(milk + bread)
# print("The total cost is: $" + total)

# ====================================================
# ====================================================

# Day 4

# Syntax - Key Operations
# price = 50
# if price < 30:
#     print('This is affordable.')
# elif price < 40:
#     print('This is a bit expensive.')
# else:
#     print('This is too expensive')

# Nested conditionals
# weather = 'sunny'
# temperature = 75

# # Condition 1: check if weather is sunny or not
# if weather == 'sunny':
#     # Condition 2: if sunny, check if temperature is above 70
#     if temperature > 70:
#         print('Wear sunglasses amd a t-shirt')
#     else:
#         print('Wear sunglasses and a light jacket.')
# else:
#     print('Bring an umbrella.')
# ---------------------------------------------
# Practice exercises
# 1
# Prompt user for an integer
# number = int(input('Give me a number: '))

# # Condition to determin if odd or even
# if number % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# 2
# Prompt user for the temperature
# temperature = int(input('Enter the current temperature in Farenheit: '))

# # Confitional to determin if it is cold, hot or warm
# if temperature <= 40:
#     print("Baby it's cold outside.")
# elif temperature > 40 and temperature <= 72:
#     print('It is a nice and warm.')
# else:
#     print('It is hot!')

# 3
# # Prompt user for information
# age = int(input('Enter your age: '))
# citizenship = input("Are you a U.S. citizen? (yes or no): ").lower()

# # Nested conditions
# if age >= 18:
#     if citizenship == 'yes':
#         print('You are eligible to vote.')
#     elif citizenship == 'no':
#         print('Sorry, only U.S. citizens are eligible to vote.')
#     else:
#         print('You did not provide a valid answer to your citizenship status.')
# else:
#     print('Sorry, you are to young to vote sport! Maybe next election.')
# ------------------------------------------

# Loops

# For and while Loops Syntax
# for item in sequence:
    # Code to execute for each item
# while condition:
    # Code to execute as long as a condition is true

# # For loop key operations
# items = ['apple', 'banana', 'cherry']

# for item in items:
#     print(item)

# # While loop key operations
# count = 0
# while count < 5:
#     print('Counting: ', count)
#     count += 1

# #  Nested loops example
# shape_list = ["circle", "square", "triangle"]
# color_list = ["red", "yellow", "green"]

# # Outer loop: iterate over each shape
# for shape in shape_list:
#     # Inner loop: iterate over each color
#     for color in color_list:
#         print(f"{shape} is {color}")
# ----------------------------------------
# Loops practice exercises
# 1
# list
# grocery_list = ["hot dogs", "buns", "onions", "chili sauce", "ketchup", "mustard", "sweet pickle relish"]

# # For loop to print each item from the list
# for grocery in grocery_list:
#     print(grocery)

# 2
# grocery_list = []

# while True:
#     decision = input('Do you wish to add an item? yes or no: ').lower()
#     if decision == "no":
#         break

#     grocery_list.append(input("Enter the name of the grocery to add: "))

# print(grocery_list)

# # 3
# grocery_dict = {"name": "apple", "price": 1.14, "quantity": 3, "total_cost": 3.42}

# for grocery in grocery_dict:
#     print(f"You have {grocery_dict['quantity']} {grocery_dict['name']}, each costing ${grocery_dict['price']}. Total cost is: ${grocery_dict['total_cost']}")
    
# --------------------------
# Loop control

# Break - stops a loop when condition met
# for item in ["apple", "lemon", "banana", "mango"]:
#     if item == "banana":
#         break
# print(f"A {item} is yellow and sweet.")

# Continue - skips the current loop iteration
# yellow_fruits = ["lemon", "banana"]
# red_fruits = []

# for item in ["apple", "lemon", "banana", "cherry"]:
#     if item in yellow_fruits:
#         continue
#     red_fruits.append(item)

# print(red_fruits)

# for item in ["apple", "lemon", "banana", "cherry"]:
#     if item == "lemon":
#         pass # DOES NOTHING
#     print(item)
# ------------------------------
# Loop Control Practice Exercises
# 1
# for tool in ["screw driver", "pliers", "hammer", "electrical tape"]:
#     if tool == "hammer":
#         break
# print(f"{tool} found.")

# # 2
# meat = ["steak", "bacon"]
# fruits = []

# for grocery in ["steak", "bacon", "strawberry", "passion fruit"]:
#     if grocery in meat:
#         continue
#     fruits.append(grocery)
# print(fruits)

# # 3
# for stuff in ["baseball", "dart", "canoe", "drill"]:
#     if stuff == "drill":
#         pass
#     print(stuff)
# -----------------------------

# Debugging and error messages

# # Try and Except
# # Syntax
# try:
#     # Code to try
# except ErrorType:
#     # Code to execute if error occurs

# # Key Concepts
# try:
#     result = 10 / 0
# except:
#     print("You can't dived by zero.")
# ---------
# Practice exercises
# # 1
# number = input("Enter any number: ")

# try:
#     float(number)
#     print(f"You entered the number: {number}")
# except ValueError:
#     print("Error occurred: the input is not a number.")

# # 2
# a = 10
# b = 5

# # Step 1: Attempt to double the value of 'b' by assigning it to 'double_b'
# double_b = b * 2

# # Step 2: Try to add 'a' and 'double_b' and store the result in 'total'
# total = a + double_b

# print("The total is:", total)
# ------------------------------------
# Day 4 Required Assignments

# # Exercise 1
# grocery_item = []
# grocery_item.append(input("Enter the name of the item to add to your grocery list: "))
# food_items = ["apple", "bread", "milk"]
# non_food_items = ["soap", "detergent", "paper towels"]

# for item in grocery_item:
#     if item in food_items:
#         print(f"{item} is on the food items list.")
#     elif item in non_food_items:
#         print(f"{item} is on the non-food items list.")
#     else:
#         print(f"{item} is not on any know list.")


# # Exercise 2
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}
# ]

# shopping_list = []
# budget = 30.0
# total_cost = 0.0
# index = 0

# while total_cost <= budget:
#     item = items_list[index]
#     item_total_cost = item["cost"] * item["amount"]
#     if total_cost + item_total_cost > budget:
#         break
#     shopping_list.append(item["name"])
#     total_cost += item_total_cost
#     index += 1

# print(shopping_list)

# # Exercise 3
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}
# ]

# shopping_list = []
# budget = 30.0
# total_cost = 0.0
# index = 0

# while total_cost <= budget:
#     item = items_list[index]
#     item_total_cost = item["cost"] * item["amount"]
#     if total_cost + item_total_cost > budget:
#         break
#     shopping_list.append(item["name"])
#     total_cost += item_total_cost
#     index += 1
#     for name in shopping_list:
#         print(name)
#     print("----------")
# print(shopping_list)

# # Exercise 4
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}
# ]

# shopping_list = []
# budget = 30.0
# total_cost = 0.0
# index = a

# while total_cost <= budget:
#     item = items_list[index]
#     item_total_cost = item["cost"] * item["amount"]
#     if total_cost + item_total_cost > budget:
#         break
#     shopping_list.append(item["name"])
#     total_cost += item_total_cost
#     index += 1
#     for name in shopping_list:
#         print(name)
#     print("----------")
#     if "burger buns" in shopping_list and "fries" in shopping_list and "burger patties" in shopping_list:
#         print(f"We can make burgers and fries for {total_cost}")
#         break
# print(shopping_list)

# # Exercise 5
# items_list = [
#     {"name": "fries", "cost":6.25, "amount": 1},
#     {"name": "burger patties", "cost":13.50, "amount": 1},
#     {"name": "burger buns", "cost":3.50, "amount": 2},
#     {"name": "tomato", "cost":1.50, "amount": 2},
#     {"name": "lettuce", "cost":5, "amount": 1},
#     {"name": "Ketchup", "cost":3.47, "amount": 1},
#     {"name": "pickles", "cost":4.25, "amount": 1}
# ]

# shopping_list = []
# budget = 30.0
# total_cost = 0.0
# index = a

# while total_cost <= budget:
#     item = items_list[index]
#     item_total_cost = item["cost"] * item["amount"]
#     if total_cost + item_total_cost > budget:
#         break
#     shopping_list.append(item["name"])
#     total_cost += item_total_cost
#     index += 1
#     try:
#         int(index)
#     except ValueError:
#         print("Error: the index must be an integer")
#     for name in shopping_list:
#         print(name)
#     print("----------")
#     if "burger buns" in shopping_list and "fries" in shopping_list and "burger patties" in shopping_list:
#         print(f"We can make burgers and fries for {total_cost}")
#         break
# print(shopping_list)

# Exercise 6
items_list = [
    {"name": "Ice Cream", "cost":5.25, "amount": 1},
    {"name": "Hot Fudge", "cost":0.99, "amount": 1},
    {"name": "Whip Cream Topping", "cost": 0.25, "amount": 1},
]

shopping_list = []
budget = 30.0
total_cost = 0.0
index = 0

while total_cost <= budget:
    item = items_list[index]
    item_total_cost = item["cost"] * item["amount"]
    if total_cost + item_total_cost > budget:
        break
    shopping_list.append(item["name"])
    total_cost += item_total_cost
    index += 1
    try:
        int(index)
    except ValueError:
        print("Error: the index must be an integer")
    for name in shopping_list:
        print(name)
    print("----------")
    if "Ice Cream" in shopping_list and "Hot Fudge" in shopping_list and "Whip Cream Topping" in shopping_list:
        print(f"We can make a hot fudge sunday for ${total_cost}")
        break
print(shopping_list)