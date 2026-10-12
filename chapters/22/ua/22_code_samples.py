# 22. Тип даних діапазон (range)

# приклад створення діапазону
r = range(0, 5, 1)  # 0, 1, 2, 3, 4

# створення діапазону та проходження по ньому за допомогою циклу for
for i in range(0, 3, 1):
    print(i)  # 0, 1, 2

# проходження по діапазону у зворотному порядку з кроком -1
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1

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

# фільтрація чисел: необов'язковий спосіб використання range() та циклу for
init_range = range(1, 11)
new_list = []
for item in init_range:
    if item % 2 == 0:
        new_list.append(item)

print(new_list)  # [2, 4, 6, 8, 10]

# фільтрація чисел: Pythonic way
new_list = [item for item in range(2, 11, 2)]
print(new_list)  # [2, 4, 6, 8, 10]

# фільтрація чисел: Pythonic way, альтернативний
new_list = list(range(2, 11, 2))
print(new_list)  # [2, 4, 6, 8, 10]
