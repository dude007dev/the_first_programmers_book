# 7. Змінна

# 7.1 Що таке змінна

# Створення змінної
age = 20
nickname = "dude007dev"

# Приклад з першої програми
input_value = input("What is your name? ")
name = input_value.title()

# Після введення, наприклад "some name", це виглядатиме так:
input_value = "some name"
name = input_value.title()  # "Some Name"

# Або коротший варіант
name = "some name".title()  # "Some Name"
# те самше що й
name = "Some Name"

# 7.2 Як обрати ім’я змінної

# Добрі приклади
user_name = "Anna"
current_year = 2025

# Погані приклади
a = 17  # нічого не зрозуміло
year2025 = 2025  # виглядає як число, плутає

# 7.3 Типи змінної

# Цілі числа (integers)
age = 20
temperature = -5

# Дійсні числа (float)
height = 1.65
pi = 3.14159

# None (порожнє значення)
x = None
print(type(x))  # <class 'NoneType'>
x = "John"  # Тепер x це рядок

# Логічний тип (boolean)
is_student = True
has_access = False

# Текстовий тип (str)
name = "Maria"
message = "Hello, world!"

# Приклади всіх базових типів
name = "Maria"  # str
age = 20  # int
height = 1.65  # float
is_student = True  # bool
salary = None  # NoneType
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>

# 7.4 Перевизначення змінної
x = 5
x = "п'ять"

# 7.5 Обʼєм змінної

# Варіант 1
import sys

x = 10
print(sys.getsizeof(x))  # наприклад, 28

# Варіант 2
from sys import getsizeof

input_value = input("What is your name? ")  # анна батьківна
name = input_value.title()  # Анна Батьківна

variable_size = getsizeof(name)
print(variable_size)  # 86 (bytes)
print(f"Size of name is: {variable_size}")  # Size of name is: 86
