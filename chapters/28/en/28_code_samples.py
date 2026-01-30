# 28. Функції

# 28.1 Створення і виклик функції

# приклад визначення та виклику функції
def my_function():
    print("Hello, this is my first function!")


my_function()  # Hello, this is my first function!

# 28.2 Створення і виклик функції з параметрами

# приклад визначення та виклику функції з одним параметром
def my_second_function(first_name):
    print(f"Hello, {first_name}!")
    print("This is my second function!")


my_second_function("John")

# повторний виклик функції з різними параметрами
my_second_function("Jane")  # Hello, Jane! ...
my_second_function("Jack")  # Hello, Jack! ...

# 28.3 Назва функції

# приклад правильного стилю
def my_function(first_name):
    print(f"Hello, {first_name}!")


my_function("Olha")  # Hello, Olha!

# робочий приклад, який не відповідає PEP-8
def mySecondFunction(first_name):
    print(f"Hello, {first_name}!")


mySecondFunction("Alex")  # Hello, Alex!

## Використання цифр у назві функції

# коректна назва
def my_2_function(first_name):  # Коректно
    print(f"Hello, {first_name}!")


my_2_function("Ivan")  # Hello, Ivan!


# Помилка: SyntaxError
def 2_function(first_name):
    print(f"Hello, {first_name}!")


# коректна і практична назва
def calc_1208():
    print("Do some calculations.")


calc_1208()  # Do some calculations.

# 28.4 Функції з кількома параметрами

# приклад функції з двома параметрами
def my_function(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


my_function("Alice", "Smith")  # Hello, Alice Smith!

# 28.5 Кількість аргументів

# приклад визначення і виклику функції з двома параметрами
def my_function(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


my_function("Alice", "Smith")  # Hello, Alice Smith!
my_function("Alice")  # TypeError: my_function() missing 1 required positional argument: 'last_name'

# 28.6 Позиційні аргументи

# визначення функції
def my_function(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


# виклик функції з позиційними аргументами
my_function("Alice", "Smith")  # Hello, Alice Smith!

# 28.7 Іменовані аргументи

# визначення функції, в якій перший параметр це `last_name`
def my_function(last_name, first_name):
    print(f"Hello, {first_name} {last_name}!")


# виклик функції з позиційними аргументами
my_function("Adams", "John")  # Hello, John Adams!

# виклик функції за допомогою іменованих аргументів
my_function(first_name="Adams", last_name="John")  # Hello, Adams John!

# порядок передавання іменованих аргументів не має значення
def my_function(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


my_function(first_name="Adams", last_name="John")  # Hello, Adams John!
my_function(last_name="Smith", first_name="Alice")  # Hello, Alice Smith!

# приклад, коли іменовані аргументи особливо корисні
def my_contact(first_name, last_name, middle_name, phone, mobile, work_phone):
    print(f"Person: {first_name} {middle_name} {last_name} ...")


my_contact("John", "Adams", "Quincy", "123-456-7777", "123-456-9999", "123-456-8888")
my_contact(
    first_name="John",
    last_name="Adams",
    middle_name="Quincy",
    phone="123-456-7777",
    mobile="123-456-9999",
    work_phone="123-456-8888",
)

## Змішування позиційних та іменованих аргументів

def my_contact(first_name, last_name, middle_name, phone, mobile, work_phone):
    print(f"Person: {first_name} {middle_name} {last_name} ...")


# OK - всі аргументи іменовані
my_contact(
    first_name="John",
    last_name="Adams",
    middle_name="Quincy",
    phone="123-456-7777",
    mobile="123-456-9999",
    work_phone="123-456-8888",
)

# Помилка: SyntaxError - positional argument follows keyword argument
my_contact(
    first_name="John",
    last_name="Adams",
    "Quincy",
    "123-456-7777",
    "123-456-9999",
    work_phone="123-456-8888",
)

# коректний приклад змішування позиційних та іменованих аргументів
def my_contact(first_name, last_name, middle_name, phone, mobile, work_phone):
    print(f"Person: {first_name} {middle_name} {last_name} ...")


my_contact(
    "Alice",
    middle_name="Example",
    phone="123-456-1111",
    mobile="123-456-2222",
    work_phone="123-456-3333",
    last_name="Smith",
)

# 28.8 Лише позиційні аргументи (/)

def my_function(first_name, last_name, /):
    print(f"Hello, {first_name} {last_name}!")


my_function("Alice", "Smith")  # Hello, Alice Smith!

# TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'first_name, last_name'
my_function(first_name="Alice", last_name="Smith")

# 28.9 Лише іменовані аргументи (*)

def my_function(*, first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


my_function(first_name="Alice", last_name="Smith")  # Hello, Alice Smith!

# TypeError: my_function() takes 0 positional arguments but 2 were given
my_function("Alice", "Smith")

# практичне використання лише іменованих аргументів
def my_function(*, first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


input_data = {"first_name": "Alice", "last_name": "Smith"}
my_function(**input_data)  # Hello, Alice Smith!

# 28.10 Комбіновані параметри: лише позиційні (/) та лише іменовані (*) аргументи

def my_function(first_name, last_name, /, *, phone_number):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


my_function("Alice", "Smith", phone_number="123-456-789")  # Hello, Alice Smith 123-456-789!

# 28.11 Передача змінної у якості параметра функції

# передача змінної `input_name` у якості параметра функції
def my_function(first_name):
    print(f"Hello, {first_name}!")


input_name = input("What is your first name? ")  # Alice
my_function(input_name)  # Hello, Alice!


# передача змінної `first_name` у якості параметра функції
def my_function(first_name):
    print(f"Hello, {first_name}!")


first_name = input("What is your first name? ")  # John
my_function(first_name)  # Hello, John!


# приклад, який доказує, що параметр та змінна `first_name` це не одна й та сама змінна
def my_function(first_name):
    print(f"Hello, {first_name}!")
    first_name = "Alyona"
    print(f"I have changed the first name to {first_name}")


first_name = input("What is your first name? ")  # John
my_function(first_name)
# Hello, John!
# I have changed the first name to Alyona

print(first_name)  # John

## міні-програма "The most frequent letter"

def the_most_frequent_letter(first_name):
    letters = {}
    for letter in first_name:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    output = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    print(f"The most frequent letter is {output[0]}")


input_name = input("What is your first name? ")  # "Dude007dev"
input_name = input_name.lower()  # "dude007dev"
the_most_frequent_letter(input_name)  # The most frequent letter is ('d', 3)

# 28.12 Значення параметра за замовчуванням

# коректний, робочий приклад
def my_function(first_name, last_name, phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


my_function("Alice", last_name="Smith")  # Hello, Alice Smith 123-456-789!

my_function("John", last_name="Adams", phone_number="123-456-000")  # Hello, John Adams 123-456-000!

## приклад з помилкою: неправильний порядок аргументів

# SyntaxError: non-default argument follows default argument
def my_function(first_name, last_name="Example", phone_number):
   print(f"Hello, {first_name} {last_name} {phone_number}!")

# не буде викликано
my_function(...)

## правильний варіант

def my_function(first_name, last_name="Example", phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


my_function("John", phone_number="123-456-000")  # Hello, John Example 123-456-000!

# 28.13 Повернення результату функції

# приклад вбудованої функції, яка повертає результат
print(len("456"))  # 3

## ключове слово return

def my_sum(a, b):
    return a + b


print(my_sum(1, 2))  # 3

## збереження результату у змінну

def my_sum(a, b):
    return a + b


result = my_sum(1, 2)
print(result)  # 3

## return без значення

def my_sum(a, b):
    return


result = my_sum(1, 2)
print(result)  # None

# функція завжди щось повертає
def my_function(first_name, last_name, phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


result = my_function("John", last_name="Adams")  # Hello, John Adams 123-456-789!
print(result)  # None

## return не обов’язковий

def my_function(first_name, last_name, phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


# те саме
def my_function(first_name, last_name, phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")
    return


# порожній return завжди повертає None
def my_sum(a, b):
    return None


result = my_sum(1, 2)
print(result)  # None

## Кілька return у функції

# приклад 1
def my_custom_sum(a, b):
    if a == 1:
        return a

    if b == 2:
        return 9

    return a + b


print(my_custom_sum(1, 2))  # 1

# приклад 2
def my_function(first_name, last_name, phone_number="123-456-789"):
    if last_name == "Adams":
        print(f"Can't process {last_name}!")
        return

    if phone_number == "123":
        print("The number is incorrect!")
        return

    print(f"Hello, {first_name} {last_name} {phone_number}!")


my_function("Alice", last_name="Smith", phone_number="123")  # The number is incorrect!

# 28.14 Змінний тип даних в параметрі функції

# приклад функції з типом даних `list` у якості аргументу
def my_function(friends):
    for friend in friends:
        print(friend)


list_of_friends = ["Alice", "Bob", "Charlie"]
my_function(list_of_friends)

# змінюємо список у тілі функції
def my_function(friends):
    friends.append("David")

    for friend in friends:
        print(friend)

    friends.append("Eve")


list_of_friends = ["Alice", "Bob", "Charlie"]
my_function(list_of_friends)
# Alice
# Bob
# Charlie
# David

print(list_of_friends)  # ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

## Незмінні типи даних

def another_function(name):
    print(f"Value inside the function: {name}")
    name = "David"
    print(f"Updated value inside the function: {name}")


some_name = "Alice"
another_function(name=some_name)
# Value inside the function: Alice
# Updated value inside the function: David

print(f"Value after the function call: {some_name}")  # Value after the function call: Alice

## Схожа поведінка зі змінними типами

def my_function(friends):
    friends.append("David")

    print("My friends:")
    for friend in friends:
        print(friend)

    friends = {"friend": "Eve"}
    print(f"New object inside the function: {friends}")


list_of_friends = ["Alice", "Bob", "Charlie"]
my_function(list_of_friends)
# My friends:
# Alice
# Bob
# Charlie
# David
# New object inside the function: {'friend': 'Eve'}

print(list_of_friends)  # ['Alice', 'Bob', 'Charlie', 'David']

# змінюємо змінну і повертаємо її в результаті
def my_function(friends):
    friends.append("David")

    print("Friends inside the function:")
    for friend in friends:
        print(friend)

    friends.append("Eve")
    return friends


list_of_friends = ["Alice", "Bob", "Charlie"]
list_of_friends = my_function(friends=list_of_friends)
# Friends inside the function:
# Alice
# Bob
# Charlie
# David

print(list_of_friends)  # ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# те саме, але змінна і параметр мають однакове ім'я
def my_function(list_of_friends):
    list_of_friends.append("David")

    print("Friends inside the function:")
    for friend in list_of_friends:
        print(friend)

    list_of_friends.append("Eve")
    return list_of_friends


list_of_friends = ["Alice", "Bob", "Charlie"]
list_of_friends = my_function(list_of_friends)
# Friends inside the function:
# Alice
# Bob
# Charlie
# David

print(list_of_friends)  # ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

## Значення за замовчуванням для параметрів зі змінним типом даних

def buggy_function(friends=[]):
    friends.append("David")

    for friend in friends:
        print(friend)

    friends.append("Eve")


# На перший погляд — нічого підозрілого. Функція виконується, і все працює
def buggy_function(friends=[]):
    friends.append("David")

    for friend in friends:
        print(friend)

    friends.append("Eve")


list_of_friends = ["Alice"]
buggy_function(friends=list_of_friends)
# Alice
# David

print(list_of_friends)  # ['Alice', 'David', 'Eve']


# та сама функція, але параметри не передаємо
def buggy_function(friends=[]):
    friends.append("David")

    for friend in friends:
        print(friend)

    friends.append("Eve")


buggy_function()
buggy_function()
print("----")
buggy_function()
# після третього виклику
# ----
# David
# Eve
# David
# Eve
# David


# правильний варіант
def good_function(friends=None):
    if friends is None:
        friends = []

    friends.append("David")

    for friend in friends:
        print(friend)

    friends.append("Eve")


good_function()
good_function()
print("----")
good_function()
# після третього виклику
# ---
# David

# 28.15 Використання pass

def my_function(first_name, last_name, phone_number):
    pass


my_function("Alice", last_name="Smith", phone_number="123")

# технічно те саме
def my_function(first_name, last_name, phone_number):
    return


my_function("Alice", last_name="Smith", phone_number="123")

## `pass` у будь-якому місці

def my_function(first_name, last_name, phone_number):
    pass
    print("The function is not yet implemented")
    pass


my_function("Alice", last_name="Smith", phone_number="123")  # The function is not yet implemented

# 28.16 Вкладені функції

def the_most_frequent_letter(name):
    letters = {}
    for letter in name:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    output = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    print(f"The most frequent letter is {output[0]}")


def main():
    value = "strawberry"
    the_most_frequent_letter(value)


main()  # The most frequent letter is ('r', 3)

## Визначення функцій усередині інших функцій

def main():
    value = "strawberry"

    def the_most_frequent_letter():
        letters = {}
        for letter in value:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        output = sorted(letters.items(), key=lambda item: item[1], reverse=True)
        print(f"The most frequent letter is {output[0]}")

    the_most_frequent_letter()


main()  # The most frequent letter is ('r', 3)

# 28.17 Документація функцій

def my_function(first_name, last_name, phone_number):
    """Prints the full name and phone number.

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
        phone_number (str): The phone number of the person.

    Returns:
        None: The function does not return anything.
    """
    print(f"Hello, {first_name} {last_name} {phone_number}!")


my_function("Alice", last_name="Smith", phone_number="123")  # Hello, Alice Smith 123!

# 28.18 *args, **kwargs

## Довільна кількість позиційних аргументів: *args

def custom_args(*args):
    print(args[0], args[1])


custom_args("Alice", "Smith", "123-456-1111")  # Alice Smith

# розпаковка кортежу
args = ("Alice", "Smith", "123-456-1111")
print(*args)  # Alice Smith 123-456-1111

## Довільна кількість іменованих аргументів: **kwargs

def custom_kwargs(**kwargs):
    print(kwargs["first_name"], kwargs["last_name"])


custom_kwargs(first_name="Alice", last_name="Smith", phone="123-456-1111")  # Alice Smith

## Використання разом

def my_custom_func(*args, **kwargs):
    print(args[0], kwargs["phone"])


my_custom_func("Alice", "Smith", middle_name="John", phone="123-456-789")  # Alice 123-456-789

## Практичне застосування

data_example = {"first_name": "Alice", "last_name": "Smith", "phone": "123-456-789"}
new_data = {"first_name": "John", "last_name": "Adams", "phone": "123-456-000", "date_of_birth": "01-01-2000"}


def my_function(first_name, last_name, phone, **kwargs):
    print(f"{first_name} {last_name} {phone}")
    if kwargs.get("date_of_birth"):
        print(f"Date of birth: {kwargs['date_of_birth']}")


my_function(**data_example)  # Alice Smith 123-456-789

my_function(**new_data)
# John Adams 123-456-000
# Date of birth: 01-01-2000

# *args, **kwargs у вбудованій функції `print()``
print("Hello", "world", sep=" - ", end="!\n")  # Hello - world!
