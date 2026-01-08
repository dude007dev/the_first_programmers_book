# 7. Variable

# 7.1 What is a variable

# Creating a variable
age = 20
nickname = "dude007dev"

# Example from the first program
input_value = input("What is your name? ")
name = input_value.title()

# After entering, for example "some name", it will look like this:
input_value = "some name"
name = input_value.title()  # "Some Name"
print(f"Hello {name}!")  # Some Name

# Or a shorter variant
name = "some name".title()  # "Some Name"
# which is the same as
name = "Some Name"

# 7.2 How to choose a variable name

# Good examples
user_name = "Anna"
current_year = 2025

# Bad examples
a = 17  # not descriptive
year2025 = 2025  # looks like a number, can be confusing

# 7.3 Variable types

# Integers
age = 20
temperature = -5

# Floats
height = 1.65
pi = 3.14159

# None (empty value)
x = None
print(type(x))  # <class 'NoneType'>
x = "John"  # Now x is a string

# Boolean
is_student = True
has_access = False

# String (str)
name = "Maria"
message = "Hello, world!"

# Examples of all basic types
name = "Maria"  # str
age = 20  # int
height = 1.65  # float
is_student = True  # bool
salary = None  # NoneType
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>

# 7.4 Reassigning a variable
x = 5
x = "five"

# 7.5 Variable size

# Option 1
import sys

x = 10
print(sys.getsizeof(x))  # e.g., 28

# Option 2
from sys import getsizeof

input_value = input("What is your name? ")  # e.g., john smith
name = input_value.title()  # "John Smith"

variable_size = getsizeof(name)
print(variable_size)  # 51 (bytes)
print(f"Size of name is: {variable_size}")  # Size of name is: 51
