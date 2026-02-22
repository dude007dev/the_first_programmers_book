# 26. Dictionary Data Type

# example of creating an empty dictionary
my_dict = {}

# example of creating a dictionary with one element
my_dict = {"some key": "some value"}

# example of creating a dictionary with several elements
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject"
}

# example of creating a dictionary with several elements with comma at the end
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
}

# example of accessing dictionary element by key
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
}

print(my_dict["experience"])  # practical knowledge gained over time

# example of adding new element to dictionary
my_dict = {"UA": "Ukraine", "NL": "Netherlands"}

my_dict["USA"] = "United States of America"
print(my_dict)  # {'UA': 'Ukraine', 'NL': 'Netherlands', 'USA': 'United States of America'}

# example of updating dictionary element value by key
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
}
my_dict["experience"] = "new value"
print(my_dict["experience"])  # new value

# example of accessing non-existent key
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
}
print(my_dict["some_key"])  # KeyError: 'some_key'

# example of duplicate keys in dictionary
my_dict = {
    "experience": "practical knowledge gained over time",
    "experience": "repeated key!!!",
    "knowledge": "information and understanding of a subject",
}

print(my_dict["experience"])  # repeated key!!!

# example of using different data types as dictionary keys
my_dict = {
    "experience": "practical knowledge gained over time",
    True: "truth",
    "true": ["t", "r", "u", "t", "h"],
    (1, 2): "tuple",
}

print(my_dict["true"])  # ['t', 'r', 'u', 't', 'h']

# TypeError: unhashable type: 'list'
my_dict = {
    [1, 2]: "list",
}

# order of elements in dictionary
my_dict = {
    "experience": "practical knowledge gained over time",
    True: "truth",
    (1, 2): "tuple",
}

print(my_dict)  # {'experience': 'practical knowledge gained over time', True: 'truth', (1, 2): 'tuple'}

# iterating through dictionary elements
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
    "skills": "the ability to do something well",
}

for key in my_dict:
    print(f"The key is '{key}'. The value is: '{my_dict[key]}'")

# getting key and value of dictionary element
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
    "skills": "the ability to do something well",
}

for key, value in my_dict.items():
    print(f"The key is '{key}'. The value is: '{value}'")

# using different names for key and value variables
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
    "skills": "the ability to do something well",
}

for element, value in my_dict.items():
    print(f"The key is '{element}'. The value is: '{value}'")

# dictionary as database
phone_book = {
    "example1.com": {"name": "John", "phone": "123456789"},
    "example2.com": {"name": "Alice", "phone": "987654321"},
}
print(phone_book["example1.com"])  # {'name': 'John', 'phone': '123456789'}
print(phone_book["example1.com"]["name"])  # John

# 26.1 Dictionary Data Type Methods

# clear() - clearing the dictionary
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
    "skills": "the ability to do something well",
}
my_dict.clear()
print(my_dict)  # {}

# copy() - returns shallow copy of dictionary
my_list = ["P", "y", "t", "h", "o", "n"]
my_dict = {
    "list": my_list,
    (1, 2): "tuple",
}
new_dict = my_dict.copy()

# 1) Modify the CONTENT of the shared list → visible in both dictionaries
my_list.append("!")
print(my_dict["list"])  # ['P', 'y', 't', 'h', 'o', 'n', '!']
print(new_dict["list"])  # ['P', 'y', 't', 'h', 'o', 'n', '!']

# 2) Remove a key only from the original → the copy does NOT change
my_dict.pop((1, 2))
print((1, 2) in my_dict)  # False
print((1, 2) in new_dict)  # True

# 3) Reassign a NEW list to the key only in the original
my_dict["list"] = ["N", "e", "w"]
print(my_dict["list"])  # ['N', 'e', 'w']
print(new_dict["list"])  # ['P', 'y', 't', 'h', 'o', 'n', '!']

# fromkeys() - creates new dictionary with given keys and default value
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
friends_init_score = dict.fromkeys(friends, 0)
print(friends_init_score)  # {'Alice': 0, 'Bob': 0, 'Charlie': 0, 'David': 0, 'Eve': 0}

# get() - returns value by key, if key doesn't exist - None or default value
my_dict = {"UA": "Ukraine", "NL": "Netherlands"}

print(my_dict.get("some key"))  # None
print(my_dict.get("some key", "default value"))  # default value
print(my_dict.get("UA", "default value"))  # Ukraine

# items() - returns object representation of dictionary items (key, value)
my_dict = {"UA": "Ukraine", "NL": "Netherlands"}

print(list(my_dict.items()))  # [('UA', 'Ukraine'), ('NL', 'Netherlands')]

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
# Key: UA, Value: Ukraine
# Key: NL, Value: Netherlands

# keys() - returns object representation of dictionary keys
my_dict = {"UA": "Ukraine", "NL": "Netherlands"}

print(my_dict.keys())  # dict_keys(['UA', 'NL'])
print(list(my_dict.keys()))  # ['UA', 'NL']

for element in my_dict.keys():
    print(f"The key is: {element}")
# The key is: UA
# The key is: NL

# values() - returns object representation of dictionary values
my_dict = {"UA": "Ukraine", "NL": "Netherlands"}

print(my_dict.values())  # dict_values(['Ukraine', 'Netherlands'])

list_of_values = list(my_dict.values())
print(list_of_values)  # ['Ukraine', 'Netherlands']
print(list_of_values[0])  # Ukraine

for element in my_dict.values():
    print(f"The value is: {element}")

# pop() - removes element by key and returns its value
my_dict = {
    "experience": "practical knowledge gained over time",
    "knowledge": "information and understanding of a subject",
    "skills": "the ability to do something well",
}

print(my_dict.pop("knowledge"))  # information and understanding of a subject
print(my_dict)  # {'experience': 'practical knowledge gained over time', 'skills': 'the ability to do something well'}
print(my_dict.pop("knowledge", "N/A"))  # N/A (not available)
print(my_dict.pop("knowledge"))  # KeyError: 'knowledge'

# popitem() - removes and returns last added element of dictionary (key, value)
my_dict = {"UA": "Ukraine", "NL": "Netherlands"}

print(my_dict.popitem())  # ('NL', 'Netherlands')
print(my_dict.popitem())  # ('UA', 'Ukraine')
print(my_dict.popitem())  # KeyError: 'popitem(): dictionary is empty'

# setdefault() - returns value by key, if key doesn't exist - adds key with default value
my_dict = {"UA": "Ukraine", "NL": "Netherlands"}

print(my_dict.setdefault("UA", "N/A"))  # Ukraine (already exists, so returns existing value)
print(my_dict.setdefault("USA", "United States of America"))  # United States of America
print(my_dict)  # {'UA': 'Ukraine', 'NL': 'Netherlands', 'USA': 'United States of America'}

# update() - updates dictionary with elements from another dictionary or iterable object (list of tuples)
my_dict = {"UA": "Ukraine", "NL": "Netherlands"}

my_dict.update({"ES": "Spain"})
print(my_dict)  # {'UA': 'Ukraine', 'NL': 'Netherlands', 'ES': 'Spain'}

my_dict.update([("FR", "France")])
print(my_dict)  # {'UA': 'Ukraine', 'NL': 'Netherlands', 'ES': 'Spain', 'FR': 'France'}

# alternative to update() using ** unpacking
dict_a = {"UA": "Ukraine", "NL": "Netherlands"}
dict_b = {"ES": "Spain", "FR": "France"}

merged_dict = {**dict_a, **dict_b}
print(merged_dict)  # {'UA': 'Ukraine', 'NL': 'Netherlands', 'ES': 'Spain', 'FR': 'France'}

# if there are identical keys - value from last dictionary remains
dict_a = {"UA": "Ukraine", "NL": "Netherlands"}
dict_b = {"NL": "Holland"}

merged_dict = {**dict_a, **dict_b}
print(merged_dict)  # {'UA': 'Ukraine', 'NL': 'Holland'}

# 26.2 Dict Comprehension

# example of creating dictionary using dict comprehension
my_dict = {x: x**2 for x in range(1, 11)}
print(my_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# example of creating dictionary with condition using dict comprehension
my_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(my_dict)

# equivalent example without dict comprehension
my_dict = {}
for x in range(1, 11):
    if x % 2 == 0:
        my_dict[x] = x**2

print(my_dict)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 26.4 Independent practice

# 2 dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# list of names
names = ["Alice", "Bob", "Alice", "Eve", "Bob", "Alice"]
