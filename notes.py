# VARIABLES
character_name = "Jill"
character_age = "75"

print("there once was a name named " + character_name + ",")
print("he was " + character_age +" years old. ")

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but he didn't like being " + character_age + ".")

# STRINGS
# \n is a new line
print("Power\nRangers")
# \" for quotation marks
print("Power\"Rangers")

phrase = "Giraffe Academy"
# CONCATENATION appending a sting onto another one
print(phrase + " is cool")

# FUNCTIONS
# makes string lowercase
print(phrase.lower())

# makes string uppercase
print(phrase.upper())

# returns True or False value of if its upper or lower case.
print(phrase.isupper())

# 2 funcs in 1
print(phrase.upper().isupper())

# length function. length of string
print(len(phrase))

# String index starts with 0. Starts counting at 0.
print(phrase[0])

# gives index of thing
print(phrase.index("G"))

# replaces
print(phrase.replace("Giraffe", "Elephant"))

# NUMBERS - can do math lol

# imports math functions
# math module - gives access to more math functions
from math import *

print(-2.0 + 4.568)

# Modules - gives the remainder. % sign
print(10 % 3)

# absolute value of
my_num = 5
print(abs(my_num))

# Exponents
print(pow(3,2))

# min
print(min(4, 6))

# max
print(max(4,6))

# round a number
print(round(3.7))

# floor function - gets the lowest number
print(floor(3.6))

# square root
print(sqrt(36))

