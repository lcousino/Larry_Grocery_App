# # Day 3: Lists and Tuples
# # Lists
# my_list=[1, "apple", 3.5]
# print(my_list)

# # Index
# my_list[0]
# print(my_list)

# # Slice
# my_list[1:3]
# print(my_list)

# # Add
# my_list.append("banana")
# print(my_list)

# # Remove
# my_list.remove("apple")
# print(my_list)

# # Sort
# my_int_list=[5, 9, 3, 11]
# my_int_list.sort()
# print(my_list)

# # Extend
# list_a=[1, "apple", 3.5]
# list_b=["banana", "tomato"]
# list_a.extend(list_b)
# print(my_list)

# # Insert at specific index
# my_list.insert(1, "banana")
# print(my_list)

# # Tuples
# my_tuple = (10, 20, "orange")
# print(my_tuple)

# # Index
# print(my_tuple[0])

# # Slice
# print(my_tuple[0:2])

# # Length
# len(my_tuple)

# # Concatenate
# print(my_tuple + (30, 40))
# ========================================
# List Practice Exercises

# 1.
# favorite_movies = ["Star Wars", "The Godfather", "Casino", "The Matrix", "Love Actually"]
# print(favorite_movies)
# favorite_movies.append("The Hangover")
# print(favorite_movies)
# favorite_movies.remove("The Godfather")
# print(favorite_movies)

# # 2.
# numbers =[10, 20, 30, 40, 50]
# print(numbers)
# print(numbers[3:5])

# # 3.
# colors = ["red", "blue", "green"]
# print(colors)
# colors.insert(1, "yellow")
# colors.append("purple")
# print(colors)

# # Tuple Practice Exercises

# # 1.
# dimensions = (10, 5, 20)
# print(dimensions[1])

# # 2.
# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
# print(numbers[2:6])

# # 3.
# fruits = ("apple", "banana")
# vegitables = ("carrot", "lettuce")
# groceries = fruits + vegitables
# print(groceries)

# ======================================================

# Dictionaries

# Syntax
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# # Access values
# print(my_dict['name'])

# # Adding or updating values
# a_dict = {'name': 'John', 'age': 25}
# a_dict['city'] = 'New York'
# a_dict['age'] = 26
# print(a_dict)

# # Removing values
# b_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# b_dict.pop('age')
# print(b_dict)

# ========================================================
# Dictionary Practice Exercerises
# 1
# book = {'tite': '1984', 'author': 'George Orwell', 'year': 1949}
# print(book['author'])

# #2
# profile = {}
# profile.update({'name': 'Alice', 'age': 30, 'city': 'Paris'})
# print(profile)
# profile['city'] = 'London'
# print(profile)

# #3
# student = {'name': 'Emma', 'grade': 'A', 'subject': 'Math'}
# print(student)
# student.pop('subject')
# print(student)
# print(student.keys())
# print(student.values())
# ============================================================

# Sets
# Syntax
# my_set = {'apple', 'banana', 'cherry'}
# print(my_set)

# # Adding
# my_set.add('orange')
# print(my_set)

# # Removing
# my_set.remove('orange')
# print(my_set)

# # Discard
# my_set.discard('banana')
# print(my_set)

# # Set Operations
# # Union
# set1 = {'apple', 'banana'}
# set2 = {'banana', 'orange'}
# print(set1.union(set2))

# #  Intersection
# print(set1.intersection(set2))

# # Diffence
# set1.add('cherry')
# print(set1.difference(set2))

# =========================================
# Set Practice Exercise

# 1
# fruits = {'apple', 'banana', 'cherry'}
# print(fruits)
# fruits.add('orange')
# print(fruits)
# fruits.discard('banana')
# print(fruits)

# 2
# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# print(set_a)
# print(set_b)
# print(set_a.union(set_b))
# print(set_a.intersection(set_b))

# # 3
# set_x = {'cat', 'dog', 'fish'}
# set_y = {'dog', 'bird'}
# print(set_x)
# print(set_y)
# print(set_x.difference(set_y))

# ============================================
# Day 3 Required Assignments

# Exercise 1
# 1
bananas_tuple = ('bananas', 0.73, 8)
cherries_tuple = ('cherries', 1.16, 4)
apples_tuple = ('apples', 1.27, 5)
# 2
grocery_list = []
print(grocery_list)
grocery_list = [bananas_tuple] + [cherries_tuple] + [apples_tuple]
print(grocery_list)
print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[-1])

#3
bananas_total_cost = grocery_list[0][1] * grocery_list[0][2]
cherries_total_cost = grocery_list[1][1] * grocery_list[1][2]
apples_total_cost = grocery_list[2][1] * grocery_list[2][2]
print(f'Total cost of {grocery_list[0][0]}: ${bananas_total_cost}')
print(f'Total cost of {grocery_list[1][0]}: ${cherries_total_cost}')
print(f'Total cost of {grocery_list[2][0]}: ${apples_total_cost}')

# Exercise 2
# 1
bananas_dict = {'name': 'bananas', 'price': 0.73, 'quantity': 8, 'total_cost': 5.84}
cherries_dict = {'name': 'cherries', 'price': 1.16, 'quantity': 4, 'total_cost': 4.64}
apples_dict = {'name': 'apples', 'price': 1.27, 'quantity': 5, 'total_cost': 6.35}
print(f'Total cost of {bananas_dict['name']}: ${bananas_dict['total_cost']}')
print(f'Total cost of {cherries_dict['name']}: ${cherries_dict['total_cost']}')
print(f'Total cost of {apples_dict['name']}: ${round(apples_dict['total_cost'],2)}')

# Exercise 3
# 1
num_list = [16, 47, 1, 3, 5, 9, 15, 2]
print(num_list)
print(num_list[1:])
print(num_list[:3])
print(num_list[-3])

# 2
num_list.sort()
print(num_list)

#3
print(len(num_list))

# Exercise 4
# 1
dairy_products = {'milk', 'butter', 'cream', 'yogurt', 'cheese'}
print(dairy_products)
desserts = {'jello', 'chocolate', 'candy', 'cookies', 'muffins'}
print(desserts)

# 2
dairy_products.add('ice creame')
print(dairy_products)
desserts.add('ice creame')
print(desserts)

# 3
dairy_products.remove('cream')
print(dairy_products)
desserts.discard('jello')
print(desserts)

# 4
print(dairy_products.intersection(desserts))









