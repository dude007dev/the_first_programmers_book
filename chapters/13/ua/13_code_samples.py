# 13. Оператори

# 13.2 Оператори присвоєння

# для відображення результати на екрані - використовуйте print()

# = — звичайне присвоєння (assign)
x = 5  # x присвоїли значення 5

# += — додавання та присвоєння
x = 1  # 1
x += 3  # 4

x = 2  # 2
y = 3  # 3
y += x  # y тепер дорівнює 5

# -= — віднімання та присвоєння
x = 5
x -= 2  # 3, x = x - 2

# *= — множення та присвоєння
x = 5
x *= 5  # 25, x = x * 5

# /= — ділення та присвоєння
x = 30
x /= 6  # 5, x = x / 6

# %= — остача від ділення та присвоєння
x = 5
x %= 3  # 2, x = x % 2

# //= — ділення націло та присвоєння
x = 24
x //= 5  # 4, x = x // 5

# **= — піднесення до степеня та присвоєння
x = 2
x **= 4  # 16, x = x ** 4

# 13.3 Оператори порівняння (Comparison Operators)

# == — дорівнює (equals)
x = 5
y = 10
print(x == y)  # False

x = 3
y = 3
print(x == y)  # True

# != — не дорівнює (not equals)
x = 5
y = 10
print(x != y)  # True

x = 3
y = 3
print(x != y)  # False

# > — більше (greater)
x = 5
y = 10
print(x > y)  # False

x = 3
y = 3
print(x > y)  # False

# < — менше (less)
x = 5
y = 10
print(x < y)  # True

x = 3
y = 3
print(x < y)  # False

# >= — більше або дорівнює (greater or equal)
x = 5
y = 10
print(x >= y)  # False

x = 3
y = 3
print(x >= y)  # True

# <= — менше або дорівнює (less or equal)
x = 5
y = 10
print(x <= y)  # True

x = 3
y = 3
print(x <= y)  # True

# 13.4 Програма з використанням оператора порівняння
programming_language = input("Enter the name of your favorite programming language: ")
if programming_language.lower() != "python":
    print("Oops, unexpected answer!")
else:
    print("I knew it! Good choice!")

# 13.5 Логічні оператори (Logical Operators)

# and — і (та)
x = 5
y = 10
print(x >= 5 and y != 10)  # True and False => False

x = 3
y = 3
print(x >= y and x < 5)  # True and True => True

# or — або (чи)
x = 5
y = 10
print(x >= 5 or y != 10)  # True or False => True

x = 3
y = 3
print(x != y or x > 5)  # False or False => False

# not — заперечення (не)
x = 5
y = 10
print(not (x >= 5 or y != 10))  # not(True) => False

x = 3
y = 3
print(not (x != y))  # not(False) => True

empty_data = True
print(not empty_data)  # False

empty_data = True
if not empty_data:  # False
    # will not be called as check returned False
    # process_data()
    pass
else:  # True
    # will be called
    exit()

# Комбінування логічних операторів
city = "Amsterdam"
minimum_population = 1_000_000
big_city = True
print((big_city and city == "Amsterdam") or minimum_population > 10_000)  # True

# Читабельність коду
x = 3
y = 5

print(all([x, x > 1, y != 3]))  # True
print(all([x > 5, y != 3]))  # False

print(any([x > 10, y < 1]))  # False
print(any([x > 5, y != 3]))  # True

# 13.6 Програма для оцінювання за шкалою A–F
value = input("Enter the percentage of correct answers of the test: ")
value = int(value)
if value >= 90:
    grade = "A"
elif value >= 80 and value < 90:
    grade = "B"
elif value >= 70 and value < 80:
    grade = "C"
elif value >= 60 and value < 70:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# 13.7 Оператори особистості (Identity Operators)
some_variable = "some text"
print(some_variable is None)  # False


# опис функції не було наведено в книжці
# функції розглядаються в кінці книжки
def some_function():
    return None


result = some_function()  # returns None
print(result is not None)  # False


# ще один приклад перевірки на None
# опис функції не було наведено в книжці
# функції розглядаються в кінці книжки
def get_points():
    return 99


grade = None
points = get_points()
if points == 100:
    grade = "A"

if grade is None:
    print("Error")

# Приклад із простими типами
x = "John"
y = "John"
print(x is y)  # True

y = "Anna"
print(x is y)  # False

y = "John"
print(x is y)  # True


# Приклад із користувацьким типом
class Person:
    def __init__(self, name):
        self.name = name


a = Person(name="John")
b = Person(name="John")
print(a is b)  # False

# 13.8 Оператори приналежності (Membership Operators)

# in
name = "John"
print("oh" in name)  # True

# not in
grades = ["A", "B", "C", "D", "F"]
print("Q" not in grades)  # True

# 13.10 Оператори пріоритету
print(5 * (3 + 6) - 10 / 2)  # 40.0
print(2**3)  # 8

x = 10
print(x > 5 and x < 15 or str(x) == "10")  # True


# коротке замикання
def my_func(a):
    print("I am here")
    print(a)


x = 10
print(x > 5 and x < 15 or my_func(x))  # True

# 13.12 Самостійна робота

# Виконайте перевірку та поясніть результат:
a = 5
b = 8
print(a > 3 and b < 10)
print(a > 10 or b == 8)
print(not (a < b))

# Що виведе наступний код?
a = None
print(a is None)
print(a is not None)

# список
languages = ["Python", "JavaScript", "C++"]

# Передбачте результат виразу
result = 5 + 3 * 2**2
print(result)
