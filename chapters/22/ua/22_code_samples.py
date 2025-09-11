# 22. Тип даних діапазон (range)

# приклад створення діапазону
r = range(0, 5, 1)  # 0, 1, 2, 3, 4

# створення діапазону та проходження по ньому за допомогою циклу for
for i in range(0, 3, 1):
    print(i)  # 0, 1, 2

# те саме, але за замовчуванням
for i in range(3):
    print(i)  # 0, 1, 2


# приклади із фільтрацією чисел
# спосіб 1: використання генератора списку
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [item for item in init_list if item % 2 == 0]

print(new_list)  # [2, 4, 6, 8, 10]

# спосіб 2: використання range() та циклу for
new_list = []
for item in range(1, 11):
    if item % 2 == 0:
        new_list.append(item)

print(new_list)  # [2, 4, 6, 8, 10]

# спосіб 3: використання range() та list comprehension
new_list = [item for item in range(1, 11) if item % 2 == 0]
print(new_list)  # [2, 4, 6, 8, 10]

# фільтрація чисел: необов'язковий і неефективний спосіб використання range() та циклу for
init_range = range(1, 11)
new_list = []
for item in init_range:
    if item % 2 == 0:
        new_list.append(item)

print(new_list)  # [2, 4, 6, 8, 10]

# фільтрація чисел: ефективний спосіб, Pythonic way
new_list = [item for item in range(2, 11, 2)]
print(new_list)  # [2, 4, 6, 8, 10]

# фільтрація чисел: ефективний спосіб, Pythonic way, альтернативний
new_list = list(range(2, 11, 2))
print(new_list)  # [2, 4, 6, 8, 10]

# приклад з використанням іменованих аргументів (Python 3.8+)
new_list = list(range(start=2, stop=11, step=2))
print(new_list)  # [2, 4, 6, 8, 10]

# 22.1 Приклад використання range для виконання N кроків

# багаторазове повторення дій (наприклад, спроба підключення до сервера)
from random import randint
from time import sleep


def try_action():
    """Спроба виконати дію, яка може завершитися помилкою."""
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
