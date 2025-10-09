# 21. Тип даних список (list)

# приклади створення списків
shopping_list = ["milk", "eggs", "meat"]

my_list = ["milk", 21, True, ["eggs"]]

empty_list = []

#  Доступ до елементів списку за індексом
shopping_list = ["milk", "eggs", "meat"]
print(shopping_list[0])  # milk
print(["milk", "eggs", "meat"][0])  # milk

# 21.1 Проходження по списку

# базова інформація про список
shopping_list = ["milk", "eggs", "meat"]
print(len(shopping_list))  # 3
print(shopping_list[1])  # eggs

# помилка: індекс 3 виходить за межі списку
print(shopping_list[3])
print(shopping_list[len(shopping_list)])

# проходження по списку за допомогою циклу while
shopping_list = ["milk", "eggs", "meat"]

i = 0
while i < len(shopping_list):
    print(shopping_list[i])
    i += 1

# проходження по списку за допомогою циклу for
shopping_list = ["milk", "eggs", "meat"]

for element in shopping_list:
    print(element)

# 21.2 Функція enumerate() для відстеження поточного індексу

# приклад проблеми індексу
my_list = ["milk", "eggs", "milk", "eggs", "meat"]

for el in my_list:
    print(el)

# приклад рішення з використанням enumerate()
my_list = ["milk", "eggs", "milk", "eggs", "meat"]

for i, el in enumerate(my_list):
    print(f"Element value: {el}")  # значення елемента
    print(f"Element index: {i}")  # його індекс

# приклад розпакування списку
i, el = [0, "milk"]
print(i)  # 0
print(el)  # milk

# приклад розпакування рядка
text = "The"
x, y, z = text
print(x)  # T
print(y)  # h
print(z)  # e

# 21.3 Операції над списками. Методи типу даних list

# приклад функції len()
shopping_list = ["milk", "eggs", "meat"]
print(len(shopping_list))  # 3

# Методи типу даних list

# append() — додавання елемента в кінець списку
shopping_list = ["milk", "eggs", "meat"]
print(len(shopping_list))  # 3

shopping_list.append("bread")
print(shopping_list)  # ['milk', 'eggs', 'meat', 'bread']
print(len(shopping_list))  # 4

# clear() — очищення списку
shopping_list = ["milk", "eggs", "meat"]
shopping_list.clear()
print(shopping_list)  # []

# copy() — створення копії списку
shopping_list = ["milk", "eggs", "meat"]
shopping_list_copy = shopping_list.copy()
shopping_list.append("bread")

print(shopping_list_copy)  # ["milk", "eggs", "meat"]
print(shopping_list)  # ['milk', 'eggs', 'meat', 'bread']

# приклад неглибокого копіювання (shallow copy)
sub_list = ["bread"]
shopping_list = ["milk", "eggs", "meat", sub_list]
shopping_list_copy = shopping_list.copy()
print(shopping_list_copy)  # ["milk", "eggs", "meat", ["bread"]]

sub_list.append("butter")
print(shopping_list_copy)  # ["milk", "eggs", "meat", ["bread", "butter"]]
print(shopping_list)  # ["milk", "eggs", "meat", ["bread", "butter"]]

# глибоке копіювання (deep copy)
from copy import deepcopy

sub_list = ["bread"]
shopping_list = ["milk", "eggs", "meat", sub_list]
shopping_list_copy = deepcopy(shopping_list)
print(shopping_list_copy)  # ["milk", "eggs", "meat", ["bread"]]

sub_list.append("butter")
print(shopping_list_copy)  # ["milk", "eggs", "meat", ["bread"]]
print(shopping_list)  # ["milk", "eggs", "meat", ["bread", "butter"]]

# count() — підрахунок кількості входжень елемента в список
shopping_list = ["milk", "eggs", "meat", "milk"]
print(shopping_list.count("milk"))  # 2

# extend() — розширення списку елементами з іншого списку
shopping_list = ["milk", "eggs", "meat"]
additional_shopping_list = ["bread", "butter", "cheese", "milk"]
shopping_list.extend(additional_shopping_list)
print(shopping_list)

# приклад розширення списку елементами рядка тексту
shopping_list = ["milk", "eggs", "meat"]
shopping_list.extend("bread")
print(shopping_list)

# index() — пошук індексу першого входження елемента в список
shopping_list = ["milk", "eggs", "meat"]
print(shopping_list.index("eggs"))  # 1
print(shopping_list.index("bread"))  # ValueError: 'bread' is not in list

# insert() — вставка елемента за певним індексом
shopping_list = ["milk", "eggs", "meat"]
shopping_list.insert(1, "bread")
print(shopping_list)  # ['milk', 'bread', 'eggs', 'meat']

# pop() — вилучення елемента за індексом (за замовчуванням — останнього)
shopping_list = ["milk", "eggs", "meat"]
shopping_list.pop(1)
print(shopping_list)  # ['milk', 'meat']

shopping_list.pop(3)  # This will raise an IndexError

# remove() — вилучення першого входження елемента за значенням
shopping_list = ["milk", "eggs", "meat"]
shopping_list.remove("eggs")
print(shopping_list)  # ['milk', 'meat']

shopping_list.remove("bread")  # ValueError: list.remove(x): x not in list

# reverse() — реверс (зворотній порядок) елементів списку
shopping_list = ["milk", "eggs", "meat"]
shopping_list.reverse()
print(shopping_list)  # ['meat', 'eggs', 'milk']

# sort() — сортування елементів списку
shopping_list = ["milk", "eggs", "meat"]
shopping_list.sort()
print(shopping_list)  # ['eggs', 'meat', 'milk']

shopping_list.sort(reverse=True)
print(shopping_list)  # ['milk', 'meat', 'eggs']

# 21.4 Приклади застосування

# Приклад 1: Гра “The Magic 8 Ball”
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

index = randint(0, 5)  # генерує ціле число від 0 до 5 включно
print(answers[index])

# Приклад 2: Список друзів + сортування
friends = []

while True:
    name = input("Enter a name of your friend or type 'exit' to quit: ")
    name = name.title()
    if name.lower() == "exit":
        break

    friends.append(name)

friends.sort()
print(f"Your friends are: {friends}")

# Приклад 3: Перетворення слова у зворотному порядку
word = "python"
list_word = list(word)  # ['p', 'y', 't', 'h', 'o', 'n']
list_word.reverse()  # ['n', 'o', 'h', 't', 'y', 'p']
reversed_word = "".join(list_word)
print(reversed_word)  # nohtyp

# альтернативний спосіб
word = "python"
reversed_word = word[::-1]
print(reversed_word)  # nohtyp

# Практичне застосування insert() та pop()
my_schedule = ["eat", "sleep", "code"]

value = my_schedule.pop(0)
my_schedule.append(value)
print(my_schedule)  # ['sleep', 'code', 'eat']

# або

my_schedule = ["eat", "sleep", "code"]
my_schedule.append(my_schedule.pop(0))
print(my_schedule)  # ['sleep', 'code', 'eat']

# 21.5 List comprehension (спискове включення)

# приклад створення списку парних чисел
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

for item in init_list:
    if item % 2 == 0:
        new_list.append(item)

print(new_list)  # [2, 4, 6, 8, 10]

# альтернативний спосіб з використанням list comprehension
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [item for item in init_list if item % 2 == 0]

print(new_list)  # [2, 4, 6, 8, 10]
