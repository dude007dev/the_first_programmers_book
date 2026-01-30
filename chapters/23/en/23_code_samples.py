# 23. Tuple Data Type

# example of tuple
my_friends = ("John", "Luna", "Stef")

# example of tuple with one element
my_tuple = (1,)
print(type(my_tuple))  # <class 'tuple'>

# example not of tuple but of integer
my_tuple = (1)
print(type(my_tuple))  # <class 'int'>

# examples of using parentheses
result = (1 + 5) * (6 + 3)  # 54

text = (
    "This is a sample text "
    "that is written in multiple rows."
)
print(text)  # This is a sample text that is written in multiple rows.

some_checks = (
    1 > 2 and
    3 < 4 and
    5 > 6
)
print(some_checks)  # False

# example of tuple with integers
my_tuple = (1, 2, 3,)
print(my_tuple)  # (1, 2, 3)

# example of tuple with different data types
my_list = [3, "4"]
my_tuple = (1, "2", my_list)
print(my_tuple)  # (1, '2', [3, '4'])

my_list.append(5)
print(my_tuple)  # (1, '2', [3, '4', 5])

# 23.1 Tuple Data Type Methods

# count() - counting number of elements in tuple
tuple_example = (1, "2", [3, 4], True, 3, "2")

print(tuple_example.count(3))  # 1
print(tuple_example.count("2"))  # 2
print(tuple_example.count("test"))  # 0

# index() - finding index of element in tuple
tuple_example = (1, "2", [3, 4], True, 3, "2")

print(tuple_example.index(3))  # 4
print(tuple_example.index("2"))  # 1

print(tuple_example.index("test"))  # ValueError: tuple.index(x): x not in tuple

# tuple takes less memory than list
from sys import getsizeof

list_example = [i for i in range(1000)]
print(getsizeof(list_example))  # Possible result: 8856 bytes

tuple_example = tuple(list_example)
print(getsizeof(tuple_example))  # Possible result: 8040 bytes

# 23.2 Example of using tuple

from random import randint

answers = (
    "Yes",
    "You may rely on it",
    "Ask again later",
    "Concentrate and ask again",
    "My sources say no",
    "Very doubtful",
)

question = input("Enter your question: ")

index = randint(0, 5)
print(answers[index])

# 23.4 Independent work

data = (3, 5, 3, 8, 3, 2, 5, 3)

example = (1, "hello", [10, 20])

colors = ["red", "green", "blue", "yellow"]
