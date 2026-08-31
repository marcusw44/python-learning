# CS1350 Homework 2
# Marcus Walker

# UNIT 1.1 - WHAT ARE DICTIONARIES?

# Beginner
my_info = {
    "name": "Marcus",
    "age": 19,
    "major": "Cyber Security"
}
print("Unit 1.1 Beginner:", my_info)

# Intermediate
menu = {
    "burger": 8.99,
    "fries": 3.49,
    "pizza": 10.99,
    "soda": 1.99
}

course_credits = {
    "CS1350": 3,
    "MATH201": 3,
    "ENGL101": 3,
    "HIST101": 3
}

print("Unit 1.1 Intermediate - Menu:", menu)
print("Unit 1.1 Intermediate - Course Credits:", course_credits)

# Advanced
weekly_temps = dict(
    Monday=72,
    Tuesday=75,
    Wednesday=68,
    Thursday=70,
    Friday=73,
    Saturday=76,
    Sunday=71
)
print("Unit 1.1 Advanced - Weekly Temperatures:", weekly_temps)

# UNIT 1.2 - ACCESSING DICTIONARY ELEMENTS

# Beginner
pet = {"name": "Buddy", "type": "dog", "age": 3}
print("Unit 1.2 Beginner - Name:", pet["name"])
print("Unit 1.2 Beginner - Age:", pet["age"])

# Intermediate
print("Unit 1.2 Intermediate - Color:", pet.get("color", "unknown"))

grades = {
    "Marcus": 85,
    "Alex": 92,
    "Jordan": 78
}

student_name = "Marcus"
grade = grades.get(student_name, 0)

if grade >= 70:
    print("Unit 1.2 Intermediate -", student_name, "passed the course.")
else:
    print("Unit 1.2 Intermediate -", student_name, "did not pass the course.")

# Advanced
products = {
    "laptop": 999.99,
    "mouse": 29.99,
    "keyboard": 79.99
}

product_name = "laptop"
price = products.get(product_name)

if price is not None:
    print("Unit 1.2 Advanced - Price:", price)
else:
    print("Unit 1.2 Advanced - Product not available")

product_name = "headphones"
price = products.get(product_name)

if price is not None:
    print("Unit 1.2 Advanced - Price:", price)
else:
    print("Unit 1.2 Advanced - Product not available")

# UNIT 1.3 - MODIFYING DICTIONARIES

# Beginner
inventory = {}
inventory["apples"] = 10
inventory["bananas"] = 15
inventory["oranges"] = 8
print("Unit 1.3 Beginner - Inventory:", inventory)

# Intermediate
scores = {"Team A": 45, "Team B": 38}
scores["Team B"] = 52
scores["Team C"] = 41

team_a_score = scores.pop("Team A")
print("Unit 1.3 Intermediate - Team A score:", team_a_score)
print("Unit 1.3 Intermediate - Scores:", scores)

# Advanced
cart = {}

cart["laptop"] = 999.99
cart["mouse"] = 29.99
cart["keyboard"] = 79.99

cart["mouse"] = 24.99

removed_item = cart.pop("keyboard")
print("Unit 1.3 Advanced - Removed item price:", removed_item)

print("Unit 1.3 Advanced - Final cart:", cart)

total = sum(cart.values())
print("Unit 1.3 Advanced - Total price:", total)

# UNIT 2.1 - HOW DICTIONARIES WORK

# Beginner
# a) "student_name"
print('Unit 2.1 Beginner - a) "student_name": valid (string is immutable and hashable)')

# b) [1, 2, 3]
print("Unit 2.1 Beginner - b) [1, 2, 3]: invalid (list is mutable and unhashable)")

# c) 100
print("Unit 2.1 Beginner - c) 100: valid (number is immutable and hashable)")

# d) ("x", "y")
print('Unit 2.1 Beginner - d) ("x", "y"): valid (tuple is immutable and hashable)')

# e) {"a": 1}
print('Unit 2.1 Beginner - e) {"a": 1}: invalid (dictionary is mutable and unhashable)')

# f) frozenset({1,2})
print("Unit 2.1 Beginner - f) frozenset({1,2}): valid (frozenset is immutable and hashable)")

# Intermediate
locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}
print("Unit 2.1 Intermediate - Locations:", locations)

data = {"a": 1, "b": 2, "a": 3, "b": 4}
print("Unit 2.1 Intermediate - Data:", data)
print("Unit 2.1 Intermediate - Length:", len(data))

print("Unit 2.1 Intermediate - Hash of Marcus:", hash("Marcus"))
print("Unit 2.1 Intermediate - Hash of 100:", hash(100))

# Advanced
game_scores = {
    ("Marcus", "Game 1"): 1500,
    ("Alex", "Game 1"): 1800,
    ("Jordan", "Game 2"): 2100
}

print("Unit 2.1 Advanced - Marcus Game 1 score:",
      game_scores[("Marcus", "Game 1")])

import time

big_list = list(range(100000))
big_dict = {i: i for i in range(100000)}

search_value = 99999

start = time.time()
result = search_value in big_list
list_time = time.time() - start

start = time.time()
result = search_value in big_dict
dict_time = time.time() - start

print("Unit 2.1 Advanced - List search time:", list_time)
print("Unit 2.1 Advanced - Dictionary search time:", dict_time)

if list_time > dict_time:
    print("Unit 2.1 Advanced - Dictionary is faster by",
          list_time / dict_time, "times.")
else:
    print("Unit 2.1 Advanced - List was faster in this test.")

# UNIT 2.2 - THE keys() AND values() METHODS

temps = {
    "Monday": 72,
    "Tuesday": 75,
    "Wednesday": 68
}

# Beginner
print("Unit 2.2 Beginner - Days:", list(temps.keys()))
print("Unit 2.2 Beginner - Temperatures:", list(temps.values()))
print("Unit 2.2 Beginner - Number of days:", len(temps))

# Intermediate
print("Unit 2.2 Intermediate - Highest temperature:",
      max(temps.values()))
print("Unit 2.2 Intermediate - Lowest temperature:",
      min(temps.values()))

if "Friday" in temps:
    print("Unit 2.2 Intermediate - Friday is in the dictionary.")
else:
    print("Unit 2.2 Intermediate - Friday is not in the dictionary.")

temps.setdefault("Thursday", 70)
print("Unit 2.2 Intermediate - After setdefault:", temps)

keys_view = temps.keys()
temps["Friday"] = 74
print("Unit 2.2 Intermediate - Dynamic keys view:", keys_view)

# Advanced
prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}

total_value = sum(prices.values())
average_price = total_value / len(prices)

print("Unit 2.2 Advanced - Total value:", total_value)
print("Unit 2.2 Advanced - Average price:", average_price)

most_expensive = max(prices.items(), key=lambda x: x[1])
least_expensive = min(prices.items(), key=lambda x: x[1])

print("Unit 2.2 Advanced - Most expensive:",
      most_expensive[0], most_expensive[1])
print("Unit 2.2 Advanced - Least expensive:",
      least_expensive[0], least_expensive[1])

import sys

price_keys_view = prices.keys()
price_keys_list = list(prices.keys())

print("Unit 2.2 Advanced - View memory:",
      sys.getsizeof(price_keys_view), "bytes")
print("Unit 2.2 Advanced - List memory:",
      sys.getsizeof(price_keys_list), "bytes")

prices.update({
    "headphones": 149,
    "monitor": 249,
    "keyboard": 89
})

print("Unit 2.2 Advanced - All products:", prices)

# UNIT 2.3 - THE items() METHOD

colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

# Beginner
for fruit, color in colors.items():
    print("The", fruit, "is", color)

print("Unit 2.3 Beginner - list(colors.items()):",
      list(colors.items()))

# Intermediate
prices = {
    "coffee": 4.50,
    "tea": 3.00,
    "juice": 5.25
}

for item, price in prices.items():
    tax_price = price * 1.10
    print(f"Unit 2.3 Intermediate - {item}: ${price:.2f} + tax = ${tax_price:.2f}")

count = 0
for item, price in prices.items():
    if price > 4.00:
        count += 1

print("Unit 2.3 Intermediate - Items over $4.00:", count)

x = 10
y = 20
x, y = y, x
print("Unit 2.3 Intermediate - Swapped values:", x, y)

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print("Unit 2.3 Intermediate - First:", first)
print("Unit 2.3 Intermediate - Middle:", middle)
print("Unit 2.3 Intermediate - Last:", last)

# Advanced
scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}

best_student, best_score = max(scores.items(), key=lambda x: x[1])
print("Unit 2.3 Advanced - Highest score:",
      best_student, best_score)

passed = {}
failed = {}

for name, score in scores.items():
    if score >= 70:
        passed[name] = score
    else:
        failed[name] = score

print("Unit 2.3 Advanced - Passed:", passed)
print("Unit 2.3 Advanced - Failed:", failed)

average = sum(scores.values()) / len(scores)
print("Unit 2.3 Advanced - Class average:", average)

deviations = {}
for name, score in scores.items():
    deviations[name] = score - average

print("Unit 2.3 Advanced - Deviations:", deviations)

big_dict = {i: i * 2 for i in range(50000)}

start = time.time()
for key, value in big_dict.items():
    _ = key + value
items_time = time.time() - start

start = time.time()
for key in big_dict.keys():
    value = big_dict[key]
    _ = key + value
keys_time = time.time() - start

print("Unit 2.3 Advanced - items() time:", items_time)
print("Unit 2.3 Advanced - keys() + lookup time:", keys_time)

if items_time > 0:
    print("Unit 2.3 Advanced - items() is",
          keys_time / items_time, "times faster.")
