# 8 Data Types

# 8.1 Data Types

# Integers
age = 20
temperature = -5

# Floats
height = 1.65
pi = 3.14159

# Complex numbers
x = 100 + 3j

# Boolean
is_student = True
has_access = False

# None (empty value)
x = None
print(type(x))  # <class 'NoneType'>
x = "John"

# String
name = "Maria"
message = 'Hello, world!'

# Bytes
my_text = b"hello user"

# List
x = [1, 2, 3, 4, 5]
my_friends = ["John", "Andrew", "Anna"]
my_list = [12, "Anna", 2022, True, [1, 2, 3]]

# Tuple
x = (1, 2, 3, 4, 5)
my_friends = ("John", "Andrew", "Anna")
my_tuple = (12, "Anna", 2022, True, [1, 2, 3])

my_list = [1, 2]
my_list.append(3)
print(my_list)  # [1, 2, 3]

my_tuple = (1, 2)
my_tuple.append(3)  # error! Tuple has no append method

# Range
range(3)  # 0, 1, 2
range(0, 3)  # same: 0, 1, 2
print(list(range(3)))  # [0, 1, 2]

# Set
x = {1, 2, 3, 4, 5}
my_friends = {"John", "Andrew", "Anna"}

my_set = {"apple", "banana", "cherry", "apple"}
print(my_set)  # {"banana", "apple", "cherry"}

# Frozen set (immutable set)
my_set = frozenset({"apple", "banana", "cherry"})
# {"apple", "banana", "cherry"}
my_set2 = frozenset([1, 2, 5, 2])  # {1, 2, 5}

# Dictionary
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
}

print(my_dict["experience"])  # practical knowledge gained over time

my_dict = {"UA": "Ukraine", "NL": "Netherlands"}
print(my_dict["UA"])  # Ukraine

# 8.2 Special Data Types

import datetime

now = datetime.datetime.now()
print(now)

# 8.3 Mutable and Immutable Data Types

# Mutable data type
names_list = ["Joachim", "Elon"]
names_list.append("Anna")
print(names_list)  #  ["Joachim", "Elon", "Anna"]

# Immutable data type
text = "My name is "
text.add("John")  # error, exception
text.append("Anna")  # error, exception

# Changing the data
text = "My name is"
text = text + " John"
print(text)  # My name is John
# or
text = "My name is"
text = f"{text} John"
print(text)  # My name is John
# or
text = "My name is %s"
text = text % ("John")
print(text)  # My name is John
