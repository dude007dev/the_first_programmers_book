# 23. Тип даних кортеж (tuple)

# приклад кортежу
my_friends = ("John", "Luna", "Stef")

# приклад кортежу з один елементом
my_tuple = (1,)
print(type(my_tuple))  # <class 'tuple'>

# приклад не кортежу, а цілого числа
my_tuple = (1)
print(type(my_tuple))  # <class 'int'>

# приклади використання круглих дужок
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

# приклад кортежу з цілими числами
my_tuple = (1, 2, 3,)
print(my_tuple)  # (1, 2, 3)

# приклад кортежу з різними типами даних
my_list = [3, "4"]
my_tuple = (1, "2", my_list)
print(my_tuple)  # (1, '2', [3, '4'])

my_list.append(5)
print(my_tuple)  # (1, '2', [3, '4', 5])

# 23.1 Методи типу даних кортеж

# count() - підрахунок кількості елементів у кортежі
tuple_example = (1, "2", [3, 4], True, 3, "2")

print(tuple_example.count(3))  # 1
print(tuple_example.count("2"))  # 2
print(tuple_example.count("test"))  # 0

# index() - пошук індексу елемента в кортежі
tuple_example = (1, "2", [3, 4], True, 3, "2")

print(tuple_example.index(3))  # 4
print(tuple_example.index("2"))  # 1

print(tuple_example.index("test"))  # ValueError: tuple.index(x): x not in tuple

# кортеж займає менше пам'яті ніж список
from sys import getsizeof

list_example = [i for i in range(1000)]
print(getsizeof(list_example))  # Можливий результат: 8856 байт

tuple_example = tuple(list_example)
print(getsizeof(tuple_example))  # Можливий результат: 8040 байт

# 23.2 Приклад використання кортежу

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

# 23.4 Самостійна робота

data = (3, 5, 3, 8, 3, 2, 5, 3)

example = (1, "hello", [10, 20])

colors = ["red", "green", "blue", "yellow"]
