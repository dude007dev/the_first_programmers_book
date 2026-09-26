# 23. Tuple Data Type

# example of tuple
my_friends = ("John", "Luna", "Stef")

# example of tuple with a trailing comma
my_tuple = (1, 2, 3,)
print(my_tuple)  # (1, 2, 3)

# Accessing tuple elements
coordinates = (10, 25, 7)

print(coordinates[0])  # 10
print(coordinates[1])  # 25
print(coordinates[-1])  # 7

# Operations on tuples
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])  # (20, 30, 40)
print(len(numbers))  # 5
print(30 in numbers)  # True

# Tuple immutability
numbers = (10, 20, 30)
numbers[1] = 50  # TypeError: 'tuple' object does not support item assignment

# example of tuple with a mutable object
my_list = [3, "4"]
my_tuple = (1, "2", my_list)
print(my_tuple)  # (1, '2', [3, '4'])

my_list.append(5)
print(my_tuple)  # (1, '2', [3, '4', 5])

# 23.1 Tuple Data Type Methods

# count() - counting number of elements in tuple
tuple_example = (1, "2", [3, 4], True, 3, "2")

print(tuple_example.count(3))  # 1
print(tuple_example.count([3, 4]))  # 1
print(tuple_example.count("2"))  # 2
print(tuple_example.count("test"))  # 0

# index() - finding index of element in tuple
tuple_example = (1, "2", [3, 4], True, 3, "2")

print(tuple_example.index(3))  # 4
print(tuple_example.index("2"))  # 1

print(tuple_example.index("test"))  # ValueError: tuple.index(x): x not in tuple

# When to use tuples
shopping_list = ["milk", "bread", "apples"]
coordinates = (52.09, 5.12)

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

# 23.4 Independent practice

value1 = (7,)
value2 = (7)

data = (3, 5, 3, 8, 3, 2, 5, 3)

example = (1, "hello", [10, 20])

colors = ["red", "green", "blue", "yellow"]

# 23.5 For the curious: memory usage of tuples

from sys import getsizeof

list_example = list(range(1000))
tuple_example = tuple(list_example)

print(getsizeof(list_example))
print(getsizeof(tuple_example))
