# MCON 141 — Homework 3
# Class 3 Concepts: if statements and Boolean logic
#
# Name: Shira Krausz
# Date: 10/7/2026
#
# DIRECTIONS
# 1. Open this file in Pyzo and save it with your own name in the filename.
# 2. Type your solution directly below each exercise's comment block.
# 3. For every exercise that asks for user input, place the input/conversion
#    statements in a try / except ValueError block.
# 4. Test every solution. If you do not use a function, leave comments stating
#    the additional tests you ran, because only the final run is visible.
# 5. All code must run without errors.
#
# EXTRA CREDIT (up to 2 points)
# Write your solutions inside functions where appropriate. For example:
#
# def check_weather(temperature):
#     if temperature > 80:
#         return "It is hot outside."
#     elif temperature < 60:
#         return "It is cold outside."
#     else:
#         return "The weather is mild."
#
# print(check_weather(75))  # should print: The weather is mild.
# print(check_weather(85))  # should print: It is hot outside.
# print(check_weather(50))  # should print: It is cold outside.


# ================================================================
# Exercise 1: What is x relative to y?
#
# Two variables are named x and y. Set y to 10 and x to 20.
#
y = 10
x = 20
if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is greater than y")
    # When I ran the code, it printed that x is greater than y. This is because yx is set to 20 which is greater than y which is set to 10.
# Write an if / elif / else statement that compares x and y:
# - If x is less than y, print: "x is less than y"
# - If x is equal to y, print: "x is equal to y"
# - If x is greater than y, print: "x is greater than y"
#
# In a comment within your code, explain the result and why it occurs.
# Also test at least two other values of x and/or y, and document those tests.

# When I ran the code, it printed that x is greater than y. This is because yx is set to 20 which is greater than y which is set to 10.
# y = 10
#x = 10

# x is equal to y
# y = 10
# x = 5
# x is less than y

# ================================================================
# Exercise 2: Is x odd or even?
#
# Use x = 20 (or define x again so this exercise runs independently).

x = 20
if x%2 == 0: # a number divided by 2 with no remainder is even
    print("x is even")
else:# a number divided by 2 with a remainder is odd
    print("x is odd")

# If x is even, print: "x is even"
# Otherwise, print: "x is odd"
#
# In a comment within your code, explain the result and why it occurs.
# Test at least one odd value as well.
#
#x = 21
#x is odd


# ================================================================
# Exercise 3: Polynomials
#
# Two factors, when multiplied together, can produce a binomial.
# Given (x + a) * (x + b), where a and b are integers:
#
#      x + a
#  *   x + b
# -------------
#        xb + ab
#   x^2 + xa
#  -------------
#   x^2 + (xb + xa) + ab'''
integer_a = (input("Enter an integer for a"))

try:
  n = int(integer_a)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {integer_a}")

integer_b = (input("Enter an integer for b"))
try:
  n = int(integer_b)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {integer_b}")
integer_a = int(integer_a)
integer_b = int(integer_b)

bx = integer_a + integer_b
cx = integer_a * integer_b
# Write a program named polynomial that asks the user for integers a and b,
# then computes and prints the expanded binomial.
print(f"(x + {integer_a}) * (x + {integer_b}) = x^2 + {bx}x + {cx}")
# Example: (x + 2) * (x + 3) = x^2 + 5x + 6'''
#
# Remember: x^2 means "x squared."
# Use try / except ValueError for user input.



# ================================================================
# Exercise 4: Analyze the polynomial
#
# Given integers a and b, expand (x + a)(x + b) into:
# x^2 + (xb + xa) + ab
#
# Then determine whether:
# - the middle-term coefficient (a + b) is positive, negative, or zero; and
# - the constant (a * b) is positive, negative, or zero.
#
# You may reuse your values of a and b from Exercise 3, but make this exercise
# run independently if possible. Use try / except ValueError for user input.
integer_a = (input("Enter an integer for a")).strip()

try:
  n = int(integer_a)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {integer_a}")

integer_b = (input("Enter an integer for b")).strip()
try:
  n = int(integer_b)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {integer_b}")

print(f"(x + {integer_a}) * (x + {integer_b}) = x^2 + ({integer_b}x + {integer_a}x) + {integer_a} * {integer_b}")

integer_a = int(integer_a)
integer_b = int(integer_b)

bx = integer_a + integer_b
cx = integer_a * integer_b

if bx < 0:
    print (f"{integer_a} + {integer_b} is negative")
elif bx == 0:
    print (f"{integer_a} + {integer_b} is 0")
else:
    print (f"{integer_a} + {integer_b} is positive")

if cx < 0:
    print (f"{integer_a} * {integer_b} is negative")
elif cx == 0:
    print (f"{integer_a} * {integer_b} is 0")
else:
    print (f"{integer_a} * {integer_b} is positive")
#Enter an integer for a 5
#Enter an integer for b -5
#(x + 5) * (x + -5) = x^2 + (-5x + 5x) + 5 * -5
#5 + -5 is 0
#5 * -5 is negative'''
#
#
#
# ================================================================
# Exercise 5: Explore the and statement
#
# Ask the user to enter integers val1 and val2.

val1 = int(input("Enter an integer for val1"))
try:
  n = int(val1)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {val1}")

val2 = int(input("Enter an integer for val2"))
try:
  n = int(val2)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {val2}")

if val1 > 0 and val2 > 0:
    print(f"val1 and val2 are positive. va11 is {val1} and val2 is {val2}")
elif val1 < 0 and val2 < 0:
    print(f"val1 and val2 are negative. va11 is {val1} and val2 is {val2}")
else:
    print(f"val1 and val2 are not both positive or both negative. va11 is {val1} and val2 is {val2}")
# - If both values are positive, print: "val1 and val2 are positive"
#   and print the values.
# - If both values are negative, print: "val1 and val2 are negative"
#   and print the values.
# - Otherwise, print: "The values are not both positive or both negative"
#   and print the values.'''
#
# Use try / except ValueError for user input.
#Enter an integer for val1 3
#Enter an integer for val2 4
#val1 and val2 are positive. va11 is 3 and val2 is 4
#Enter an integer for val1 3
#Enter an integer for val2 -5
#val1 and val2 are not both positive or both negative. va11 is 3 and val2 is -5
#resandfunctions.py"
#Enter an integer for val1 -5
#Enter an integer for val2 -8
#val1 and val2 are negative. va11 is -5 and val2 is -8

#==========================================================
# Exercise 6: Explore the or statement
#
# Ask the user to enter integers val1 and val2.
#
# - If val1 or val2 is positive, print: "At least one value is positive"
#   and print the values.
# - If val1 or val2 is equal to zero, print: "At least one value is zero"
#   and print the values.
# - Otherwise, print: "At least one value is negative"
#
# Use try / except ValueError for user input.

#val1 = int(input("Enter an integer for val1"))
try:
  n = int(val1)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {val1}")

val2 = int(input("Enter an integer for val2"))
try:
  n = int(val2)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {val2}")

if val1 > 0 or val2 > 0:
    print(f"At least one value is positive. Val1 is {val1} and val2 is {val2}")
if val1 == 0 or val2 == 0:
    print(f"At least one value is equal to 0. Val1 is {val1} and val2 is {val2}")
else:
    print(f"Atleast one value is negative. Val1 is {val1} and val2 is {val2}")


# ================================================================
# Exercise 7: Explore not
#
# Set the following variables:
a = True
b = True
c = False
d = not (a and b) # Result: False, because opposite (not) of true (a and b)
print(d)
e = not a or not c # Result: True, because True is opposite of c (false)
print(e)
f = not((a and c) and b)#Result: True, because opposite of false. need everything to be true to be true
print(f)
# Evaluate and print the results of these expressions:
# 1. not (a and b)
# 2. not a or not c
# 3. not ((a and c) and b)
#
# Include a comment explaining each result.



# ================================================================
# Exercise 8: Voting Age and Citizenship
age = int(input("Enter your age"))
try:
  n = int(age)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {age}")
citizenship = input("Are you a citizen? Yes or no").strip().lower()
if age >= 18 and citizenship == 'yes':
    print('You are eligable to vote.')
if age < 18 or citizenship == 'no':
    print('You are not eligable to vote.')

# Ask the user for their age and whether they are a citizen (yes or no).
#
# - If they are 18 or older AND a citizen, print:
#   "You are eligible to vote."
# - If they are under 18 OR not a citizen, print:
#   "You are not eligible to vote."
#
# Hint: use and for the eligibility requirements. Use try / except ValueError
# for the age input.



# ================================================================
# Exercise 9: Number Classification
integer = int(input("Enter an integer."))
try:
  n = int(integer)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {integer}")

if integer%2 == 0 and integer > 0:
    print("Positive even number.")
elif integer%2 == 1 and integer > 0:
    print("Positive odd number.")
elif integer <= 0:
    print ("Not a positive number")
# Ask the user for an integer.
#
# - If it is positive and even, print: "Positive even number."
# - If it is positive and odd, print: "Positive odd number."
# - If it is negative or zero, print: "Not a positive number."
#
# Hint: combine and and or. Use try / except ValueError for user input.



# ================================================================
# Exercise 10: Triangle Check
#
# Ask the user for three side lengths: a, b, and c.
a = int(input("Enter triangle length a."))
try:
  n = int(a)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {a}")
b = int(input("Enter triangle length b."))
try:
  n = int(b)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {b}")
c = int(input("Enter triangle length c."))
try:
  n = int(c)
except ValueError as e:
  print(f"Error. We were expecting a number, but you supplied {c}")

if a > 0 and b > 0 and c> 0 and a + b > c and a + c > b and b + c > a:
    print ("Valid triangle.")
else:
    print ("Not a valid triangle.")
# Print "Valid triangle." only if all sides are greater than 0 AND:
# - a + b > c
# - a + c > b
# - b + c > a
#
# Otherwise, print "Not a valid triangle."
#
# Hint: chain multiple and conditions. Use try / except ValueError for input.



# ================================================================
# Exercise 11: Weekend Plan Decision Tree
#
# Ask the user two questions:
# - gIs it the weekend? (yes or no)
# - Do you have homework? (yes or no)
weekend = input("Is it the weekend?").lower
homework = input("Do you have homework?").lower
if weekend == 'yes' and homework == 'no':
    print("Go have fun!")
elif weekend == 'yes' and homework == 'yes':
    print("Do your homework first, then relax.")
elif weekend == 'no' and homework == 'no':
    print("Focus on schoolwork.")
else:
    print("It's a regular day, keep learning!")
# Build a decision tree that prints:
# - Weekend and no homework: "Go have fun!"
# - Weekend and homework: "Do your homework first, then relax."
# - Not weekend and homework: "Focus on schoolwork."
# - Not weekend and no homework: "It's a regular day, keep learning!"
#
# Consider converting responses to lowercase so Yes, YES, and yes all work.

