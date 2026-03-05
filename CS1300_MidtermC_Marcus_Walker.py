#CS1300 Midterm C
#Problem 1: Distance Converter
# This program asks the user for a distance and the unit (km or mi).
# It converts the distance to the other unit and prints the result
# formatted to two decimal places.

# Ask the user for the distance value and convert it to a float
distance = float(input("Enter the distance value: "))

# Ask the user for the unit (km or mi)
# .lower() makes the program accept KM, Km, etc.
unit = input("Enter the unit (km or mi): ").lower()

# If the unit is kilometers, convert to miles
if unit == "km":
    miles = distance * 0.621371
    print(f"{miles:.2f} mi")

# If the unit is miles, convert to kilometers
elif unit == "mi":
    km = distance * 1.60934
    print(f"{km:.2f} km")

# If the user enters an invalid unit, print an error message
else:
    print("Invalid unit.")
    
    
# ------------------------------
# Problem 2: Text Statistics Tool
# ------------------------------

sentence = input("Enter a sentence: ")

total_chars = len(sentence)

words = sentence.split()
total_words = len(words)

vowels = "aeiou"
vowel_count = 0
consonant_count = 0
non_space_chars = 0

for char in sentence.lower():
    if char != " ":
        non_space_chars += 1

    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

avg_word_length = non_space_chars / total_words

print("Total characters:", total_chars)
print("Total words:", total_words)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Average word length:", format(avg_word_length, ".2f"))
print("Longest word:", longest_word)



# ------------------------------
# Problem 3: Grade Book Manager
# ------------------------------

assignments = ["Quiz 1", "Homework 1", "Lab 1", "Quiz 2", "Homework 2"]
scores = [85, 92, 78, 88, 95]

print("=== GRADE BOOK ===")

i = 0
while i < len(assignments):
    print(i+1, ".", assignments[i], "-", scores[i])
    i += 1

print("==================")

# find highest and lowest
highest = scores[0]
lowest = scores[0]
high_name = assignments[0]
low_name = assignments[0]

i = 0
while i < len(scores):

    if scores[i] > highest:
        highest = scores[i]
        high_name = assignments[i]

    if scores[i] < lowest:
        lowest = scores[i]
        low_name = assignments[i]

    i += 1

print("Highest:", high_name, "(", highest, ")")
print("Lowest:", low_name, "(", lowest, ")")

# average
total = 0
i = 0

while i < len(scores):
    total += scores[i]
    i += 1

average = total / len(scores)

print("Average:", format(average, ".2f"))

# letter grades
print("Letter Grades:")

i = 0
while i < len(scores):

    score = scores[i]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(assignments[i], "-", grade)

    i += 1


# append new assignment
assignments.append("Lab 2")
scores.append(90)

# remove quiz 1
index = assignments.index("Quiz 1")
assignments.pop(index)
scores.pop(index)

# pop last assignment
removed_assignment = assignments.pop()
removed_score = scores.pop()

print("Removed:", removed_assignment, removed_score)

print("Final Grade Book:")
print(assignments)
print(scores)

print("Length:", len(assignments))



# ------------------------------
# Problem 4: Shipping Cost Calculator
# ------------------------------

weight = float(input("Enter package weight (lbs): "))
destination = input("Enter destination (domestic/international): ").lower()
premium = input("Premium member? (yes/no): ").lower()

cost = 0

if destination == "domestic":

    if weight <= 5:
        cost = 5.00

    elif weight <= 20:
        cost = 5 + (weight - 5) * 0.75

    else:
        cost = 16.25 + (weight - 20) * 0.50

elif destination == "international":

    if weight <= 5:
        cost = 15.00

    elif weight <= 20:
        cost = 15 + (weight - 5) * 2.00

    else:
        cost = 45 + (weight - 20) * 1.50

else:
    print("Invalid destination.")

if premium == "yes":
    cost = cost * 0.5

print("--- Shipping Label ---")
print("Weight:", format(weight, ".2f"), "lbs")
print("Destination:", destination.capitalize())
print("Premium member:", premium.capitalize())
print("Shipping cost: $", format(cost, ".2f"))
print("----------------------")



# ------------------------------
# Problem 5: Attendance Tracker
# ------------------------------

students = ["Maria", "James", "Priya", "Tom", "Lena", "Oscar"]
attended = [18, 12, 20, 15, 9, 17]

print("=== ATTENDANCE ROSTER ===")

i = 0

while i < len(students):

    percent = (attended[i] / 20) * 100

    print(i+1, ".", students[i], "-", attended[i], "/20 (", format(percent, ".1f"), "%)", sep="")

    i += 1

print("=========================")

# best and worst
best = attended[0]
worst = attended[0]
best_student = students[0]
worst_student = students[0]

i = 0

while i < len(attended):

    if attended[i] > best:
        best = attended[i]
        best_student = students[i]

    if attended[i] < worst:
        worst = attended[i]
        worst_student = students[i]

    i += 1

print("Best attendance:", best_student)
print("Worst attendance:", worst_student)

# class average
total = 0

i = 0
while i < len(attended):
    total += attended[i]
    i += 1

avg = (total / len(attended)) / 20 * 100

print("Class average:", format(avg, ".1f"), "%")

# status
i = 0

while i < len(attended):

    percent = attended[i] / 20 * 100

    if percent >= 90:
        status = "Excellent"
    elif percent >= 75:
        status = "Good"
    elif percent >= 60:
        status = "At Risk"
    else:
        status = "Intervention Required"

    print(students[i], "-", status)

    i += 1

# update roster
students.append("Nina")
attended.append(16)

index = students.index("Lena")

students.pop(index)
attended.pop(index)

print("Updated roster length:", len(students))