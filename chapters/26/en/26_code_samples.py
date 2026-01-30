# 26. Dictionary Data Type

# example of creating an empty dictionary
my_dict = {}

# example of creating a dictionary with one element
my_dict = {"some key": "some value"}

# example of creating a dictionary with several elements
my_en_ua_dict = {"experience": "досвід", "knowledge": "знання"}

# example of creating a dictionary with several elements with comma at the end
my_en_ua_dict = {
    "experience": "досвід",
    "knowledge": "знання",
}

# example of accessing dictionary element by key
my_en_ua_dict = {
    "experience": "досвід",
    "knowledge": "знання",
}

print(my_en_ua_dict["experience"])  # досвід

# example of adding new element to dictionary
my_en_ua_dict = {
    "experience": "досвід",
    "knowledge": "знання",
}

my_en_ua_dict["skill"] = "навичка"
print(my_en_ua_dict)  # {'experience': 'досвід', 'knowledge': 'знання', 'skill': 'навичка'}

# example of updating dictionary element value by key
my_en_ua_dict = {
    "experience": "досвід",
}
my_en_ua_dict["experience"] = "нове значення"
print(my_en_ua_dict["experience"])  # нове значення

# example of accessing non-existent key
my_en_ua_dict = {
    "knowledge": "досвід",
    "knowledge": "знання",
    True: "правда",
    "true": "правда",
}

print(my_en_ua_dict["experience"])  # KeyError: 'experience'

# example of duplicate keys in dictionary
my_en_ua_dict = {
    "knowledge": "досвід",
    "knowledge": "знання",
    "knowledge": "повторення!!!",
    True: "правда",
    "true": "правда",
}

print(my_en_ua_dict["knowledge"])  # повторення!!!

# example of using different data types as dictionary keys
my_dict = {
    "experience": "досвід",
    True: ["п", "р", "а", "в", "д", "а"],
    "true": "правда",
    (1, 2): "кортеж",
}
print(my_dict[True])  # ['п', 'р', 'а', 'в', 'д', 'а']

# TypeError: unhashable type: 'list'
my_error_dict = {
    [1, 2]: "список",
}

# order of elements in dictionary
my_dict = {
    "experience": "досвід",
    True: "правда",
    (1, 2): "кортеж",
}

print(my_dict)  # {'experience': 'досвід', True: 'правда', (1, 2): 'кортеж'}

# iterating through dictionary elements
my_dict = {
    "experience": "досвід",
    True: "правда",
    (1, 2): "кортеж",
}

for key in my_dict:
    print(f"The key is '{key}'. The value is: '{my_dict[key]}'")

# getting key and value of dictionary element
my_dict = {
    "experience": "досвід",
    True: "правда",
    (1, 2): "кортеж",
}

for key, value in my_dict.items():
    print(f"The key is '{key}'. The value is: '{value}'")

# using different names for key and value variables
my_dict = {
    "experience": "досвід",
    True: "правда",
    (1, 2): "кортеж",
}

for element, value in my_dict.items():
    print(f"The key is '{element}'. The value is: '{value}'")

# dictionary as database
phone_book = {
    "example1.com": {"name": "John", "phone": "123456789"},
    "example2.com": {"name": "Alice", "phone": "987654321"},
}
print(phone_book["example1.com"])
print(phone_book["example1.com"]["name"])

# 26.1 Dictionary Data Type Methods

# clear() - clearing the dictionary
my_dict = {
    "experience": "досвід",
    True: "правда",
    "true": "правда",
    (1, 2): "кортеж",
}
my_dict.clear()
print(my_dict)  # {}

# copy() - returns shallow copy of dictionary
my_list = ["P", "y", "t", "h", "o", "n"]
my_dict = {
    "список": my_list,
    (1, 2): "кортеж",
}
new_dict = my_dict.copy()

# 1) Modifying CONTENTS of shared list → visible in both
my_list.append("!")
print(my_dict["список"])  # ['P', 'y', 't', 'h', 'o', 'n', '!']
print(new_dict["список"])  # ['P', 'y', 't', 'h', 'o', 'n', '!']

# 2) Deleting key only from original → copy does NOT change
my_dict.pop((1, 2))
print((1, 2) in my_dict)  # False
print((1, 2) in new_dict)  # True

# 3) Reassigning key with NEW list only in original
my_dict["список"] = ["N", "e", "w"]
print(my_dict["список"])  # ['N', 'e', 'w']
print(new_dict["список"])  # ['P', 'y', 't', 'h', 'o', 'n', '!']

# fromkeys() - creates new dictionary with given keys and default value
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
friends_init_score = dict.fromkeys(friends, 0)
print(friends_init_score)  # {'Alice': 0, 'Bob': 0, 'Charlie': 0, 'David': 0, 'Eve': 0}

# get() - returns value by key, if key doesn't exist - None or default value
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
}

print(my_en_ua_dict.get("some key"))  # None
print(my_en_ua_dict.get("some key", "some value"))  # some value
print(my_en_ua_dict.get("knowledge", "some value"))  # знання

# items() - returns object representation of dictionary items (key, value)
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
}

print(list(my_en_ua_dict.items()))  # [('knowledge', 'знання'), ('truth', 'правда')]

for key, value in my_en_ua_dict.items():
    print(f"Key: {key}, Value: {value}")
# Key: knowledge, Value: знання
# Key: truth, Value: правда

# keys() - returns object representation of dictionary keys
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
}

print(my_en_ua_dict.keys())  # dict_keys(['knowledge', 'truth'])
print(list(my_en_ua_dict.keys()))  # ['knowledge', 'truth']

for element in my_en_ua_dict.keys():
    print(f"The key is: {element}")
# The key is: knowledge
# The key is: truth

# values() - returns object representation of dictionary values
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
}

print(my_en_ua_dict.values())  # dict_values(['знання', 'правда'])
list_of_values = list(my_en_ua_dict.values())
print(list_of_values)  # ['знання', 'правда']
print(list_of_values[0])  # знання

for element in my_en_ua_dict.values():
    print(f"The value is: {element}")

# pop() - removes element by key and returns its value
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
    "example": "приклад",
}

print(my_en_ua_dict.pop("knowledge"))  # знання
print(my_en_ua_dict)  # {'truth': 'правда', 'example': 'приклад'}
print(my_en_ua_dict.pop("knowledge", "N/A"))  # N/A (not available)
print(my_en_ua_dict.pop("knowledge"))  # KeyError: 'knowledge'

# popitem() - removes and returns last added element of dictionary (key, value)
my_en_ua_dict = {"knowledge": "знання", "truth": "правда"}

print(my_en_ua_dict.popitem())  # ('truth', 'правда')
print(my_en_ua_dict.popitem())  # ('knowledge', 'знання')
print(my_en_ua_dict.popitem())  # KeyError: 'popitem(): dictionary is empty'

# setdefault() - returns value by key, if key doesn't exist - adds key with default value
my_en_ua_dict = {"knowledge": "знання", "truth": "правда"}

print(my_en_ua_dict.setdefault("knowledge", "немає перекладу"))  # знання
print(my_en_ua_dict.setdefault("wisdom", "мудрість"))  # мудрість
print(my_en_ua_dict)  # {'knowledge': 'знання', 'truth': 'правда', 'wisdom': 'мудрість'}

# update() - updates dictionary with elements from another dictionary or iterable object (list of tuples)
my_en_ua_dict = {"knowledge": "знання", "truth": "правда"}

my_en_ua_dict.update({"wisdom": "мудрість", "experience": "досвід"})
print(my_en_ua_dict)  # {'knowledge': 'знання', 'truth': 'правда', 'wisdom': 'мудрість', 'experience': 'досвід'}

my_en_ua_dict.update([("intelligence", "інтелект")])
print(
    my_en_ua_dict
)  # {'knowledge': 'знання', 'truth': 'правда', 'wisdom': 'мудрість', 'experience': 'досвід', 'intelligence': 'інтелект'}

# alternative to update() using ** unpacking
dict_a = {"knowledge": "знання", "truth": "правда"}
dict_b = {"wisdom": "мудрість", "experience": "досвід"}

merged_dict = {**dict_a, **dict_b}
print(merged_dict)  # {'knowledge': 'знання', 'truth': 'правда', 'wisdom': 'мудрість', 'experience': 'досвід'}

# if there are identical keys - value from last dictionary remains
dict_a = {"knowledge": "знання", "truth": "правда"}
dict_b = {"truth": "істина"}

merged_dict = {**dict_a, **dict_b}
print(merged_dict)  # {'knowledge': 'знання', 'truth': 'істина'}

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

# 26.4 Independent Work

# 2 dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# list of names
names = ["Alice", "Bob", "Alice", "Eve", "Bob", "Alice"]
