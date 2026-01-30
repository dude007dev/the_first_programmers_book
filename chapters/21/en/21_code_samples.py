# 21. List Data Type

# Examples of creating lists
shopping_list = ["milk", "eggs", "meat"]

my_list = ["milk", 21, True, ["eggs"]]

empty_list = []

#  Accessing list elements by index
shopping_list = ["milk", "eggs", "meat"]
print(shopping_list[0])  # milk
print(["milk", "eggs", "meat"][0])  # milk

# 21.1 Iterating Through Lists

# Basic information about a list
shopping_list = ["milk", "eggs", "meat"]
print(len(shopping_list))  # 3
print(shopping_list[1])  # eggs

# error: index 3 is out of bounds
print(shopping_list[3])
print(shopping_list[len(shopping_list)])

# iterating through list using while loop
shopping_list = ["milk", "eggs", "meat"]

i = 0
while i < len(shopping_list):
    print(shopping_list[i])
    i += 1

# iterating through list using for loop
shopping_list = ["milk", "eggs", "meat"]

for element in shopping_list:
    print(element)

# 21.2 enumerate() function for tracking current index

# example of problem with index
my_list = ["milk", "eggs", "milk", "eggs", "meat"]

for el in my_list:
    print(el)

# example of solution using enumerate()
my_list = ["milk", "eggs", "milk", "eggs", "meat"]

for i, el in enumerate(my_list):
    print(f"Element value: {el}")  # element value
    print(f"Element index: {i}")  # its index

# example of unpacking a list
i, el = [0, "milk"]
print(i)  # 0
print(el)  # milk

# example of unpacking a string
text = "The"
x, y, z = text
print(x)  # T
print(y)  # h
print(z)  # e

# 21.3 Operations on Lists. List Data Type Methods

# Example of len() function
shopping_list = ["milk", "eggs", "meat"]
print(len(shopping_list))  # 3

# List data type methods

# append() — adding element to end of list
shopping_list = ["milk", "eggs", "meat"]
print(len(shopping_list))  # 3

shopping_list.append("bread")
print(shopping_list)  # ['milk', 'eggs', 'meat', 'bread']
print(len(shopping_list))  # 4

# clear() — clearing the list
shopping_list = ["milk", "eggs", "meat"]
shopping_list.clear()
print(shopping_list)  # []

# copy() — creating a copy of list
shopping_list = ["milk", "eggs", "meat"]
shopping_list_copy = shopping_list.copy()
shopping_list.append("bread")

print(shopping_list_copy)  # ["milk", "eggs", "meat"]
print(shopping_list)  # ['milk', 'eggs', 'meat', 'bread']

# example of shallow copy
sub_list = ["bread"]
shopping_list = ["milk", "eggs", "meat", sub_list]
shopping_list_copy = shopping_list.copy()
print(shopping_list_copy)  # ["milk", "eggs", "meat", ["bread"]]

sub_list.append("butter")
print(shopping_list_copy)  # ["milk", "eggs", "meat", ["bread", "butter"]]
print(shopping_list)  # ["milk", "eggs", "meat", ["bread", "butter"]]

# deep copy
from copy import deepcopy

sub_list = ["bread"]
shopping_list = ["milk", "eggs", "meat", sub_list]
shopping_list_copy = deepcopy(shopping_list)
print(shopping_list_copy)  # ["milk", "eggs", "meat", ["bread"]]

sub_list.append("butter")
print(shopping_list_copy)  # ["milk", "eggs", "meat", ["bread"]]
print(shopping_list)  # ["milk", "eggs", "meat", ["bread", "butter"]]

# count() — counting occurrences of element in list
shopping_list = ["milk", "eggs", "meat", "milk"]
print(shopping_list.count("milk"))  # 2

# extend() — extending list with elements from another list
shopping_list = ["milk", "eggs", "meat"]
additional_shopping_list = ["bread", "butter", "cheese", "milk"]
shopping_list.extend(additional_shopping_list)
print(shopping_list)

# example of extending list with characters from string
shopping_list = ["milk", "eggs", "meat"]
shopping_list.extend("bread")
print(shopping_list)

# index() — finding index of first occurrence of element in list
shopping_list = ["milk", "eggs", "meat"]
print(shopping_list.index("eggs"))  # 1
print(shopping_list.index("bread"))  # ValueError: 'bread' is not in list

# insert() — inserting element at specific index
shopping_list = ["milk", "eggs", "meat"]
shopping_list.insert(1, "bread")
print(shopping_list)  # ['milk', 'bread', 'eggs', 'meat']

# pop() — removing element by index (last element by default)
shopping_list = ["milk", "eggs", "meat"]
shopping_list.pop(1)
print(shopping_list)  # ['milk', 'meat']

shopping_list.pop(3)  # This will raise an IndexError

# remove() — removing first occurrence of element by value
shopping_list = ["milk", "eggs", "meat"]
shopping_list.remove("eggs")
print(shopping_list)  # ['milk', 'meat']

shopping_list.remove("bread")  # ValueError: list.remove(x): x not in list

# reverse() — reversing elements in list
shopping_list = ["milk", "eggs", "meat"]
shopping_list.reverse()
print(shopping_list)  # ['meat', 'eggs', 'milk']

# sort() — sorting elements in list
shopping_list = ["milk", "eggs", "meat"]
shopping_list.sort()
print(shopping_list)  # ['eggs', 'meat', 'milk']

shopping_list.sort(reverse=True)
print(shopping_list)  # ['milk', 'meat', 'eggs']

# 21.4 Examples of applications

# Example 1: The Magic 8 Ball game
from random import randint

answers = [
    "Yes",
    "You may rely on it",
    "Ask again later",
    "Concentrate and ask again",
    "My sources say no",
    "Very doubtful",
]

question = input("Enter your question: ")

index = randint(0, 5)  # generates integer from 0 to 5 inclusive
print(answers[index])

# Example 2: List of friends + sorting
friends = []

while True:
    name = input("Enter a name of your friend or type 'exit' to quit: ")
    name = name.title()
    if name.lower() == "exit":
        break

    friends.append(name)

friends.sort()
print(f"Your friends are: {friends}")

# Example 3: Transforming word in reverse order
word = "python"
list_word = list(word)  # ['p', 'y', 't', 'h', 'o', 'n']
list_word.reverse()  # ['n', 'o', 'h', 't', 'y', 'p']
reversed_word = "".join(list_word)
print(reversed_word)  # nohtyp

# alternative way
word = "python"
reversed_word = word[::-1]
print(reversed_word)  # nohtyp

# Practical application of insert() and pop()
my_schedule = ["eat", "sleep", "code"]

value = my_schedule.pop(0)
my_schedule.append(value)
print(my_schedule)  # ['sleep', 'code', 'eat']

# or

my_schedule = ["eat", "sleep", "code"]
my_schedule.append(my_schedule.pop(0))
print(my_schedule)  # ['sleep', 'code', 'eat']

# 21.5 List comprehension

# example of creating list of even numbers
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

for item in init_list:
    if item % 2 == 0:
        new_list.append(item)

print(new_list)  # [2, 4, 6, 8, 10]

# alternative way using list comprehension
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [item for item in init_list if item % 2 == 0]

print(new_list)  # [2, 4, 6, 8, 10]
