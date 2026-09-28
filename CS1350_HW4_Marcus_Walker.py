# CS1350 - WEEK 2 PRACTICE EXERCISES
# Week 2 Lecture 1: Dictionary III
# Week 2 Lecture 2: Sets

# WEEK 2 LECTURE 1 - DICTIONARY III

# UNIT 3.1 - ITERATING THROUGH DICTIONARIES

# ---------------- BEGINNER ----------------

inventory = {"apples": 50, "bananas": 30, "oranges": 25}

# 1. Print each product name using default iteration
print("Unit 3.1 - Beginner")

for product in inventory:
    print(product)

# 2. Calculate total items using values()
total_items = sum(inventory.values())
print("Total items:", total_items)

# 3. Print each product with quantity using items()
for product, quantity in inventory.items():
    print(product, quantity)


# ---------------- INTERMEDIATE ----------------

print("\nUnit 3.1 - Intermediate")

prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}

# 1. Print products sorted alphabetically
print("Products alphabetically:")

for product in sorted(prices):
    print(product, prices[product])

# 2. Print products sorted by price (cheapest first)
print("Products by price:")

for product in sorted(prices, key=prices.get):
    print(product, prices[product])

# 3. Find and print the most expensive item using items()
most_expensive = ""
highest_price = 0

for product, price in prices.items():
    if price > highest_price:
        highest_price = price
        most_expensive = product

print("Most expensive:", most_expensive, highest_price)


# ---------------- ADVANCED ----------------

print("\nUnit 3.1 - Advanced")

temps = {
    "Mon": 72,
    "Tue": 68,
    "Wed": 75,
    "Thu": 80,
    "Fri": 65
}

# 1. Calculate average temperature using values()
average_temp = sum(temps.values()) / len(temps)

print(f"Average temperature: {average_temp:.2f}")

# 2. Find hottest and coldest days in a single loop
hottest_day = ""
coldest_day = ""
hottest_temp = float("-inf")
coldest_temp = float("inf")

for day, temp in temps.items():

    if temp > hottest_temp:
        hottest_temp = temp
        hottest_day = day

    if temp < coldest_temp:
        coldest_temp = temp
        coldest_day = day

print("Hottest:", hottest_day, hottest_temp)
print("Coldest:", coldest_day, coldest_temp)

# 3. Count how many days were above average
above_average = 0

for temp in temps.values():
    if temp > average_temp:
        above_average += 1

print("Days above average:", above_average)


# UNIT 3.2 - ADVANCED ITERATION & NESTED DICTIONARIES

# ---------------- BEGINNER ----------------

print("\nUnit 3.2 - Beginner")

products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}

# 1. Print laptop's price
print("Laptop price:", products["laptop"]["price"])

# 2. Print each product with its stock level
for product, info in products.items():
    print(product, "stock:", info["stock"])


# ---------------- INTERMEDIATE ----------------

print("\nUnit 3.2 - Intermediate")

# 1. Create dictionary using zip()
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

country_capitals = {}

for country, capital in zip(countries, capitals):
    country_capitals[country] = capital

print(country_capitals)

# 2. Add tablet to products
products["tablet"] = {
    "price": 449,
    "stock": 30
}

print("Products after adding tablet:", products)

# 3. Safely remove all products with stock < 20
for product, info in list(products.items()):
    if info["stock"] < 20:
        del products[product]

print("Products after removing low stock:", products)


# ---------------- ADVANCED ----------------

print("\nUnit 3.2 - Advanced")

company = {
    "Engineering": {
        "Alice": 95000,
        "Bob": 85000
    },
    "Marketing": {
        "Carol": 75000,
        "Dave": 70000
    }
}

# 1. Print all employees with salaries
for department, employees in company.items():

    print(department)

    for employee, salary in employees.items():
        print(employee, salary)

# 2. Calculate average salary per department
for department, employees in company.items():

    total_salary = sum(employees.values())
    average_salary = total_salary / len(employees)

    print(
        department,
        "average salary:",
        f"{average_salary:.2f}"
    )

# 3. Find highest-paid employee across all departments
highest_employee = ""
highest_salary = 0

for department, employees in company.items():

    for employee, salary in employees.items():

        if salary > highest_salary:
            highest_salary = salary
            highest_employee = employee

print(
    "Highest-paid employee:",
    highest_employee,
    highest_salary
)

# UNIT 3.3 - DICTIONARY PATTERNS & TRANSFORMATIONS

# ---------------- BEGINNER ----------------

print("\nUnit 3.3 - Beginner")

# 1. Map numbers 1-5 to cubes
cubes = {
    number: number ** 3
    for number in range(1, 6)
}

print("Cubes:", cubes)

# 2. Convert Fahrenheit temperatures to Celsius
temps = {
    "Mon": 72,
    "Tue": 68,
    "Wed": 75
}

celsius = {
    day: (temp - 32) * 5 / 9
    for day, temp in temps.items()
}

print("Celsius:", celsius)


# ---------------- INTERMEDIATE ----------------

print("\nUnit 3.3 - Intermediate")

scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}

# 1. Create passing dictionary
passing = {
    name: score
    for name, score in scores.items()
    if score >= 70
}

print("Passing:", passing)


# 2. Convert scores to letter grades
def to_letter(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


letter_grades = {
    name: to_letter(score)
    for name, score in scores.items()
}

print("Letter grades:", letter_grades)


# 3. Invert student IDs
student_ids = {
    "Alice": 101,
    "Bob": 102
}

id_lookup = {
    student_id: name
    for name, student_id in student_ids.items()
}

print("ID lookup:", id_lookup)


# ---------------- ADVANCED ----------------

print("\nUnit 3.3 - Advanced")

sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]

# 1. Calculate total sales by region
sales_by_region = {}

for region, person, amount in sales:

    sales_by_region[region] = (
        sales_by_region.get(region, 0) + amount
    )

print("Sales by region:", sales_by_region)


# 2. Calculate total sales by salesperson
sales_by_person = {}

for region, person, amount in sales:

    sales_by_person[person] = (
        sales_by_person.get(person, 0) + amount
    )

print("Sales by salesperson:", sales_by_person)


# 3. Create nested dictionary
sales_nested = {}

for region, person, amount in sales:

    if region not in sales_nested:
        sales_nested[region] = {}

    sales_nested[region][person] = (
        sales_nested[region].get(person, 0) + amount
    )

print("Nested sales:", sales_nested)

# WEEK 2 LECTURE 2 - SETS

# UNIT 1 - SET THEORY AND PYTHON SETS

# ---------------- BEGINNER ----------------

print("\nUnit 1 Sets - Beginner")

# 1. Create a set containing vowels
vowels = {"a", "e", "i", "o", "u"}

print("Vowels:", vowels)

# 2. Create set from list and count elements
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

unique_numbers = set(numbers)

print("Unique numbers:", unique_numbers)
print("Number of elements:", len(unique_numbers))

# 3. Correct way to create empty set
empty = set()

print("Empty set:", empty)


# ---------------- INTERMEDIATE ----------------

print("\nUnit 1 Sets - Intermediate")

# 1. Unique characters in mississippi
text = "mississippi"

unique_characters = set(text)

print("Unique characters:", unique_characters)
print("Number of unique letters:", len(unique_characters))

# 2. Remove duplicate emails
emails = [
    "a@b.com",
    "c@d.com",
    "a@b.com",
    "e@f.com",
    "c@d.com"
]

unique_emails = list(set(emails))

print("Unique emails:", unique_emails)

# 3. Lists cannot be elements of a set because they are unhashable
# s = {[1, 2], [3, 4]}
# This would cause a TypeError.


# ---------------- ADVANCED ----------------

print("\nUnit 1 Sets - Advanced")

# 1. Compare membership in a set vs list
number_set = set(range(1000000))
number_list = list(range(1000000))

print("999999 in set:", 999999 in number_set)
print("999999 in list:", 999999 in number_list)

# Set membership is generally faster because sets use hash tables.

# 2. Create frozenset and use as dictionary key
frozen = frozenset([1, 2, 3])

frozen_dictionary = {
    frozen: "Numbers"
}

print("Frozenset dictionary:", frozen_dictionary)

# 3. Create set of unique graph nodes
edges = [
    (1, 2),
    (2, 3),
    (1, 3),
    (3, 4)
]

nodes = set()

for first, second in edges:
    nodes.add(first)
    nodes.add(second)

print("Unique nodes:", nodes)

# UNIT 2 - SET OPERATIONS

# ---------------- BEGINNER ----------------

print("\nUnit 2 Sets - Beginner")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1. Union
print("Union:", a | b)

# 2. Intersection
print("Intersection:", a & b)

# 3. Difference
print("Only in a:", a - b)


# ---------------- INTERMEDIATE ----------------

print("\nUnit 2 Sets - Intermediate")

morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

# 1. Employees who work all shifts
all_shifts = (
    morning_shift
    & evening_shift
    & weekend_shift
)

print("All shifts:", all_shifts)

# 2. Employees who work at least one shift
any_shift = (
    morning_shift
    | evening_shift
    | weekend_shift
)

print("At least one shift:", any_shift)

# 3. Employees who only work morning
morning_only = (
    morning_shift
    - evening_shift
    - weekend_shift
)

print("Morning only:", morning_only)

# 4. Employees who work exactly one shift
exactly_one = (
    (morning_shift - evening_shift - weekend_shift)
    | (evening_shift - morning_shift - weekend_shift)
    | (weekend_shift - morning_shift - evening_shift)
)

print("Exactly one shift:", exactly_one)


# ---------------- ADVANCED ----------------

print("\nUnit 2 Sets - Advanced")

prereqs_met = {
    "Alice",
    "Bob",
    "Carol",
    "Dave"
}

has_space = {
    "Bob",
    "Carol",
    "Eve",
    "Frank"
}

paid_tuition = {
    "Alice",
    "Carol",
    "Eve"
}

# 1. Students eligible for enrollment
eligible = (
    prereqs_met
    & has_space
    & paid_tuition
)

print("Eligible:", eligible)

# 2. Met prerequisites but haven't paid
not_paid = prereqs_met - paid_tuition

print("Prereqs met but not paid:", not_paid)

# 3. Missing at least one required criterion
all_students = prereqs_met | has_space | paid_tuition

missing_requirement = (
    all_students - eligible
)

print("Missing at least one requirement:", missing_requirement)

# UNIT 3 - SET METHODS, COMPREHENSIONS & PATTERNS

# ---------------- BEGINNER ----------------

print("\nUnit 3 Sets - Beginner")

# 1. Create set, add 4, remove 1
numbers = {1, 2, 3}

numbers.add(4)
numbers.remove(1)

print("Modified set:", numbers)

# 2. Even numbers from 0-20
even_numbers = {
    number
    for number in range(21)
    if number % 2 == 0
}

print("Even numbers:", even_numbers)

# 3. Safely remove element that doesn't exist
numbers.discard(100)

print("After discard:", numbers)

# remove(100) would cause a KeyError if 100 is not in the set.


# ---------------- INTERMEDIATE ----------------

print("\nUnit 3 Sets - Intermediate")

# 1. Remove duplicates while preserving order
numbers = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]

seen = set()
unique_numbers = []

for number in numbers:

    if number not in seen:
        seen.add(number)
        unique_numbers.append(number)

print("Unique in order:", unique_numbers)


# 2. Extract unique words
sentence = "To be or not to be that is the question"

unique_words = {
    word
    for word in sentence.lower().split()
}

print("Unique words:", unique_words)


# 3. Find missing numbers
expected = set(range(1, 11))

actual = {
    1, 2, 4, 5, 7, 8, 10
}

missing = expected - actual

print("Missing numbers:", missing)


# ---------------- ADVANCED ----------------

print("\nUnit 3 Sets - Advanced")

# 1. Function to find duplicates
def find_duplicates(lst):

    seen = set()
    duplicates = set()

    for item in lst:

        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates


print(
    "Duplicates:",
    find_duplicates([1, 2, 2, 3, 3, 3, 4])
)


# 2. Employee skills
alice = {
    "Python",
    "SQL",
    "Excel",
    "Tableau"
}

bob = {
    "Python",
    "Java",
    "SQL",
    "AWS"
}

carol = {
    "Python",
    "R",
    "SQL",
    "Tableau"
}

# Skills all three have
common_skills = alice & bob & carol

print("Skills all three have:", common_skills)

# Skills only Alice has
alice_only = alice - bob - carol

print("Skills only Alice has:", alice_only)

# All unique skills
all_skills = alice | bob | carol

print("All unique skills:", all_skills)


# 3. Function returning common characters
def common_chars(first_string, second_string):

    first_set = set(first_string)
    second_set = set(second_string)

    return first_set & second_set


print(
    "Common characters:",
    common_chars("hello", "world")
)
