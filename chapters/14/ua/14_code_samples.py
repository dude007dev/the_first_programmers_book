# 14. Блок try...except

# 14.4 Продовжити програму з урахуванням помилки

number_of_students = 0
sum_of_grades = 0
average_value = sum_of_grades / number_of_students
# Якщо виникла помилка - average_value = 0
average_value = 0

# 14.5 Блок try... except...

number_of_students = 0
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except:  # якщо сталася помилка - average_value = 0
    average_value = 0

print(average_value)  # 0
print("This is the end of the program")

# приклад без помилки
number_of_students = 10
sum_of_grades = 85
try:
    average_value = sum_of_grades / number_of_students
except:  # помилки не буде, блок except ігнорується
    average_value = 0

print(average_value)  # 8.5
print("This is the end of the program")

# Дострокове завершення програми
number_of_students = 0
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except:
    print("Oops, something went wrong")
    exit()

print(average_value)
print("This is the end of the program")


# 14.6 Деталі помилки

number_of_students = 0
sum_of_grades = 0

try:
    average_value = sum_of_grades / number_of_students
except Exception:
    print("Oops, something went wrong")
    exit()

# подробиці помилки
number_of_students = 0
sum_of_grades = 0

try:
    average_value = sum_of_grades / number_of_students
except Exception as e:
    print(f"Error details: {e}")  # Error details: division by zero
    print("Oops, something went wrong")
    exit()

# тип помилки
number_of_students = 0
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except ZeroDivisionError:
    average_value = 0

# Коли помилка — не та, що ви очікували
number_of_students = "zero"
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except ZeroDivisionError:
    average_value = 0

print(average_value)
print("This is the end of the program")
# TypeError: unsupported operand type(s) for /: 'int' and 'str'

# приклад поганого стилю
try:
    number_of_students = 0
    sum_of_grades = 0
    average_value = sum_of_grades / number_of_students
except ZeroDivisionError:
    average_value = 0

# Обробка кількох типів помилок
number_of_students = "zero"
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except ZeroDivisionError:
    average_value = 0
except TypeError:
    average_value = 0
except Exception:
    print("Ooops, something went wrong.")
    exit()

print(average_value)
print("This is the end of the program")

# Групування помилок
number_of_students = "zero"
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except (TypeError, ZeroDivisionError):
    average_value = 0
except Exception as e:
    print("Ooops, something went wrong.")
    print(f"Error details: {e}")
    exit()

print(average_value)
print("This is the end of the program")

# 14.7 Блок finally:

number_of_students = "zero"
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except (TypeError, ZeroDivisionError):
    average_value = 0
except Exception:
    print("Ooops, something went wrong.")
finally:
    print("This is the end of the program")


# практичний приклад — робота з базами даних
# опис функцій не було наведено в книжці
# функції розглядаються в кінці книжки
def connect_to_db():
    print("Connected to the database.")


def do_something():
    print("Doing something...")
    raise Exception("Some error occurred")


def rollback():
    print("Transaction rolled back.")


def close_connection():
    print("Connection closed.")


connect_to_db()
try:
    do_something()
except Exception:
    rollback()
finally:
    close_connection()

print("This is the end of the program")

# 14.8 Приклад: розрахунок депозиту з використанням try..except...

try:
    d = int(input("Enter the deposit amount: "))
except ValueError:
    print("Please enter a valid number")
    d = int(input("Enter the deposit amount: "))

try:
    i = float(input("Enter the interest rate (example: 1.28): "))
except ValueError:
    print("Please enter a valid float number")
    i = float(input("Enter the interest rate (example: 1.28): "))

try:
    n = int(input("Enter the number of years: "))
except ValueError:
    print("Please enter a valid number")
    n = int(input("Enter the number of years: "))

i /= 100
compound_rate = (1 + i) ** n - 1
compound_interest = d * compound_rate

result = round(d + compound_interest, 2)
print(result)
