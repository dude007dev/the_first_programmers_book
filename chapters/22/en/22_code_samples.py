# 22. Range Data Type

# Example of creating a range
r = range(0, 5, 1)  # 0, 1, 2, 3, 4

# creating a range and iterating through it using for loop
for i in range(0, 3, 1):
    print(i)  # 0, 1, 2

# same, but by default
for i in range(3):
    print(i)  # 0, 1, 2


# examples with number filtering
# method 1: using list comprehension
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [item for item in init_list if item % 2 == 0]

print(new_list)  # [2, 4, 6, 8, 10]

# method 2: using range() and for loop
new_list = []
for item in range(1, 11):
    if item % 2 == 0:
        new_list.append(item)

print(new_list)  # [2, 4, 6, 8, 10]

# method 3: using range() and list comprehension
new_list = [item for item in range(1, 11) if item % 2 == 0]
print(new_list)  # [2, 4, 6, 8, 10]

# filtering numbers: optional way using range() and for loop
init_range = range(1, 11)
new_list = []
for item in init_range:
    if item % 2 == 0:
        new_list.append(item)

print(new_list)  # [2, 4, 6, 8, 10]

# filtering numbers: Pythonic way
new_list = [item for item in range(2, 11, 2)]
print(new_list)  # [2, 4, 6, 8, 10]

# filtering numbers: Pythonic way, alternative
new_list = list(range(2, 11, 2))
print(new_list)  # [2, 4, 6, 8, 10]
