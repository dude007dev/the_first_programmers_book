# 28. Functions

# 28.1 Creating and Calling a Function

# example of defining and calling a function
def my_function():
    print("Hello, this is my first function!")


my_function()  # Hello, this is my first function!

# 28.2 Creating and Calling a Function with Parameters

# example of defining and calling a function with one parameter
def my_second_function(first_name):
    print(f"Hello, {first_name}!")
    print("This is my second function!")


my_second_function("John")

# repeated function calls with different parameters
my_second_function("Jane")  # Hello, Jane! ...
my_second_function("Jack")  # Hello, Jack! ...

# 28.3 Function Name

# example of correct style
def my_function(first_name):
    print(f"Hello, {first_name}!")


my_function("Olha")  # Hello, Olha!

# working example that does not comply with PEP-8
def mySecondFunction(first_name):
    print(f"Hello, {first_name}!")


mySecondFunction("Alex")  # Hello, Alex!

## Using digits in function name

# correct name
def my_2_function(first_name):  # Correct
    print(f"Hello, {first_name}!")


my_2_function("Ivan")  # Hello, Ivan!


# Error: SyntaxError
def 2_function(first_name):
    print(f"Hello, {first_name}!")


# correct and practical name
def calc_1208():
    print("Do some calculations.")


calc_1208()  # Do some calculations.

# 28.4 Functions with Multiple Parameters

# example of function with two parameters
def my_function(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


my_function("Alice", "Smith")  # Hello, Alice Smith!

# 28.5 Number of Arguments

# example of defining and calling function with two parameters
def my_function(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


my_function("Alice", "Smith")  # Hello, Alice Smith!
my_function("Alice")  # TypeError: my_function() missing 1 required positional argument: 'last_name'

# 28.6 Positional Arguments

# function definition
def my_function(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


# calling function with positional arguments
my_function("Alice", "Smith")  # Hello, Alice Smith!

# 28.7 Named Arguments

# defining function where first parameter is `last_name`
def my_function(last_name, first_name):
    print(f"Hello, {first_name} {last_name}!")


# calling function with positional arguments
my_function("Adams", "John")  # Hello, John Adams!

# calling function using named arguments
my_function(first_name="Adams", last_name="John")  # Hello, Adams John!

# порядок передавання іменованих аргументів не має значення
def my_function(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


my_function(first_name="Adams", last_name="John")  # Hello, Adams John!
my_function(last_name="Smith", first_name="Alice")  # Hello, Alice Smith!

# example when named arguments especially useful
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

## Mixing positional and named arguments

def my_contact(first_name, last_name, middle_name, phone, mobile, work_phone):
    print(f"Person: {first_name} {middle_name} {last_name} ...")


# OK - all arguments named
my_contact(
    first_name="John",
    last_name="Adams",
    middle_name="Quincy",
    phone="123-456-7777",
    mobile="123-456-9999",
    work_phone="123-456-8888",
)

# Error: SyntaxError - positional argument follows keyword argument
my_contact(
    first_name="John",
    last_name="Adams",
    "Quincy",
    "123-456-7777",
    "123-456-9999",
    work_phone="123-456-8888",
)

# correct example of mixing positional and named arguments
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

# 28.8 Positional-Only Arguments (/)

def my_function(first_name, last_name, /):
    print(f"Hello, {first_name} {last_name}!")


my_function("Alice", "Smith")  # Hello, Alice Smith!

# TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'first_name, last_name'
my_function(first_name="Alice", last_name="Smith")

# 28.9 Keyword-Only Arguments (*)

def my_function(*, first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


my_function(first_name="Alice", last_name="Smith")  # Hello, Alice Smith!

# TypeError: my_function() takes 0 positional arguments but 2 were given
my_function("Alice", "Smith")

# practical use of keyword-only arguments
def my_function(*, first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


input_data = {"first_name": "Alice", "last_name": "Smith"}
my_function(**input_data)  # Hello, Alice Smith!

# 28.10 Combined Parameters: Positional-Only (/) and Keyword-Only (*) Arguments

def my_function(first_name, last_name, /, *, phone_number):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


my_function("Alice", "Smith", phone_number="123-456-789")  # Hello, Alice Smith 123-456-789!

# 28.11 Passing Variable as Function Parameter

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


# example proving that parameter and variable `first_name` are not the same variable
def my_function(first_name):
    print(f"Hello, {first_name}!")
    first_name = "Alyona"
    print(f"I have changed the first name to {first_name}")


first_name = input("What is your first name? ")  # John
my_function(first_name)
# Hello, John!
# I have changed the first name to Alyona

print(first_name)  # John

## Mini-program "The most frequent letter"

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

# 28.12 Parameter Default Value

# correct working example
def my_function(first_name, last_name, phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


my_function("Alice", last_name="Smith")  # Hello, Alice Smith 123-456-789!

my_function("John", last_name="Adams", phone_number="123-456-000")  # Hello, John Adams 123-456-000!

## example with error: wrong order of arguments

# SyntaxError: non-default argument follows default argument
def my_function(first_name, last_name="Example", phone_number):
   print(f"Hello, {first_name} {last_name} {phone_number}!")

# will not be called
my_function(...)

## correct version

def my_function(first_name, last_name="Example", phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


my_function("John", phone_number="123-456-000")  # Hello, John Example 123-456-000!

# 28.13 Returning Result of Function

# example of built-in function that returns result
print(len("456"))  # 3

## return keyword

def my_sum(a, b):
    return a + b


print(my_sum(1, 2))  # 3

## saving result in variable

def my_sum(a, b):
    return a + b


result = my_sum(1, 2)
print(result)  # 3

## return without value

def my_sum(a, b):
    return


result = my_sum(1, 2)
print(result)  # None

# function always returns something
def my_function(first_name, last_name, phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


result = my_function("John", last_name="Adams")  # Hello, John Adams 123-456-789!
print(result)  # None

## return is not required

def my_function(first_name, last_name, phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")


# the same
def my_function(first_name, last_name, phone_number="123-456-789"):
    print(f"Hello, {first_name} {last_name} {phone_number}!")
    return


# empty return always returns None
def my_sum(a, b):
    return None


result = my_sum(1, 2)
print(result)  # None

## Multiple return in function

# example 1
def my_custom_sum(a, b):
    if a == 1:
        return a

    if b == 2:
        return 9

    return a + b


print(my_custom_sum(1, 2))  # 1

# example 2
def my_function(first_name, last_name, phone_number="123-456-789"):
    if last_name == "Adams":
        print(f"Can't process {last_name}!")
        return

    if phone_number == "123":
        print("The number is incorrect!")
        return

    print(f"Hello, {first_name} {last_name} {phone_number}!")


my_function("Alice", last_name="Smith", phone_number="123")  # The number is incorrect!

# 28.14 Mutable Data Type in Function Parameter

# example of function with list data type as argument
def my_function(friends):
    for friend in friends:
        print(friend)


list_of_friends = ["Alice", "Bob", "Charlie"]
my_function(list_of_friends)

# modifying list in function body
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

## Immutable data types

def another_function(name):
    print(f"Value inside the function: {name}")
    name = "David"
    print(f"Updated value inside the function: {name}")


some_name = "Alice"
another_function(name=some_name)
# Value inside the function: Alice
# Updated value inside the function: David

print(f"Value after the function call: {some_name}")  # Value after the function call: Alice

## Similar behavior with mutable variable types

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

# modifying variable and returning it in result
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

# the same, but variable and parameter have same name
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

## Default values for parameters with mutable data types

def buggy_function(friends=[]):
    friends.append("David")

    for friend in friends:
        print(friend)

    friends.append("Eve")


# At first glance — nothing suspicious. Function executes and everything works
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


# the same function, but parameters not passed
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


# correct version
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

# 28.15 Using pass

def my_function(first_name, last_name, phone_number):
    pass


my_function("Alice", last_name="Smith", phone_number="123")

# technically the same
def my_function(first_name, last_name, phone_number):
    return


my_function("Alice", last_name="Smith", phone_number="123")

## `pass` in any location

def my_function(first_name, last_name, phone_number):
    pass
    print("The function is not yet implemented")
    pass


my_function("Alice", last_name="Smith", phone_number="123")  # The function is not yet implemented

# 28.16 Nested Functions

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

## Defining functions inside other functions

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

# 28.17 Function Documentation

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

## Arbitrary number of positional arguments: *args

def custom_args(*args):
    print(args[0], args[1])


custom_args("Alice", "Smith", "123-456-1111")  # Alice Smith

# unpacking tuple
args = ("Alice", "Smith", "123-456-1111")
print(*args)  # Alice Smith 123-456-1111

## Arbitrary number of keyword arguments: **kwargs

def custom_kwargs(**kwargs):
    print(kwargs["first_name"], kwargs["last_name"])


custom_kwargs(first_name="Alice", last_name="Smith", phone="123-456-1111")  # Alice Smith

## Using together

def my_custom_func(*args, **kwargs):
    print(args[0], kwargs["phone"])


my_custom_func("Alice", "Smith", middle_name="John", phone="123-456-789")  # Alice 123-456-789

## Practical application

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

# *args, **kwargs in built-in function `print()``
print("Hello", "world", sep=" - ", end="!\n")  # Hello - world!
