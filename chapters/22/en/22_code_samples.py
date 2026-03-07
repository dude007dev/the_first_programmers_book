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

# filtering numbers: optional and inefficient way using range() and for loop
init_range = range(1, 11)
new_list = []
for item in init_range:
    if item % 2 == 0:
        new_list.append(item)

print(new_list)  # [2, 4, 6, 8, 10]

# filtering numbers: efficient way, Pythonic way
new_list = [item for item in range(2, 11, 2)]
print(new_list)  # [2, 4, 6, 8, 10]

# filtering numbers: efficient way, Pythonic way, alternative
new_list = list(range(2, 11, 2))
print(new_list)  # [2, 4, 6, 8, 10]

# example using named arguments (Python 3.8+)
new_list = list(range(start=2, stop=11, step=2))
print(new_list)  # [2, 4, 6, 8, 10]

# 22.1 Example of Using range for Performing N Steps

# repeatedly performing actions (for example, trying to connect to server)
from random import randint
from time import sleep


def try_action():
    """Attempting to perform an action that may fail."""
    if randint(0, 1):
        raise Exception("Simulated error")
    return "Success!"


print("Program started")
for i in range(3):
    try:
        result = try_action()
    except Exception as e:
        print(f"Attempt {i + 1} failed. Error: {e}")
        sleep(1)
        continue

    print(result)
    break

print("Program finished")
