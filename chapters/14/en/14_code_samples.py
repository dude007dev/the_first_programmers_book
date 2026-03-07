# 14. The try...except Block

# 14.4 Continue the program while handling an error


number_of_students = 0
sum_of_grades = 0
average_value = sum_of_grades / number_of_students
# If an error occurred - average_value = 0
average_value = 0


# 14.5 The try...except block


number_of_students = 0
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except:  # if an error occurred - average_value = 0
    average_value = 0

print(average_value)  # 0
print("This is the end of the program")


# Example without an error
number_of_students = 10
sum_of_grades = 85
try:
    average_value = sum_of_grades / number_of_students
except:  # no error will occur, except block is ignored
    average_value = 0

print(average_value)  # 8.5
print("This is the end of the program")


# Early program termination
number_of_students = 0
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except:
    print("Oops, something went wrong")
    exit()

print(average_value)
print("This is the end of the program")


# 14.6 Error details


number_of_students = 0
sum_of_grades = 0

try:
    average_value = sum_of_grades / number_of_students
except Exception:
    print("Oops, something went wrong")
    exit()

# Error details
number_of_students = 0
sum_of_grades = 0

try:
    average_value = sum_of_grades / number_of_students
except Exception as e:
    print(f"Error details: {e}")  # Error details: division by zero
    print("Oops, something went wrong")
    exit()

    average_value = sum_of_grades / number_of_students
except Exception:
    print("Oops, something went wrong")
    exit()

# Error type
number_of_students = 0
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except ZeroDivisionError:
    average_value = 0


# When the error is not what you expected
number_of_students = "zero"
sum_of_grades = 0
try:
    average_value = sum_of_grades / number_of_students
except ZeroDivisionError:
    average_value = 0

print(average_value)
print("This is the end of the program")
# TypeError: unsupported operand type(s) for /: 'int' and 'str'

# Example of bad style
try:
    number_of_students = 0
    sum_of_grades = 0
    average_value = sum_of_grades / number_of_students
except ZeroDivisionError:
    average_value = 0

# Handling multiple error types
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

# Grouping errors
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

# 14.7 The finally block:

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


# Practical example — working with databases
# Function definitions were not provided in the book
# Functions are discussed at the end of the book
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

# 14.8 Example: deposit calculation using try..except...

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
