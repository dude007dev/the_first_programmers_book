# 16. Text data type

name = 'John Smith'
name = "John Smith"  # те саме

# Multi-line text. Option 1
some_text = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(some_text)

# Multi-line text. Option 2
random_text = "Lorem ipsum dolor sit amet," \
    "consectetur adipiscing elit," \
    "sed do eiusmod tempor incididunt" \
    "ut labore et dolore magna aliqua."

print(random_text)

# Displaying text on multiple lines
random_text = "Lorem ipsum dolor sit amet,\n" \
    "consectetur adipiscing elit,\n" \
    "sed do eiusmod tempor incididunt\n" \
    "ut labore et dolore magna aliqua."

print(random_text)

# Multi-line text. Option 3 (recommended)
random_text = (
    "Lorem ipsum dolor sit amet,\n"
    "consectetur adipiscing elit,\n"
    "sed do eiusmod tempor incididunt\n"
    "ut labore et dolore magna aliqua."
)

print(random_text)

# text in parentheses
random_text = ("Lorem")
print(random_text)  # Lorem

random_text = ("Lorem", "ipsum")
print(random_text)  # ('Lorem', 'ipsum')

# double quotes in text
text = "Hello, \"Python!\""
print(text)  # Hello, "Python!"

# 16.1 Text as a sequence of characters

# character indexing in text
text = "Hello World!"
print(text[0])  # H
print(text[1])  # e
print(text[2])  # l

print(type(text))  # <class 'str'>

# character membership in text
text = "Hello World!"
print("l" in text)  # True
print("L" in text)  # False
print("q" not in text)  # True

# 16.2 String slicing

# text slicing
text = "Hello Python!"
print(text[6:12])  # Python

# various text slicing options
text = "Hello Python!"

print(text[0:13])  # Hello Python!
print(text[0:len(text)])  # Hello Python!
print(text[0:])  # Hello Python!
print(text[:len(text)])  # Hello Python!
print(text[:])  # Hello Python!

# slicing with negative indices
text = "Hello Python!"
print(text[-7:-1])  # Python

# slicing step
text = "Hello Python!"
print(text[6:12:2])  # Pto

# 16.3 Functions and methods for text

# example with + operator
"Hello " + "Python!"  # concatenation via + operator
" ".join(["Hello", "Python!"])  # concatenation via join method

# text length
text = "Hello World!"
print(len(text))  # 12

# example of function usage
print("Hello, World!")
print("Hello,", "World!")

# example of method usage
text = "hello world!"
print(text.title())  # Hello World!

# example of returning result from method
text = "HELLO PYTHON!"

print(text.lower())  # hello python!
print(text)  # HELLO PYTHON!

new_text = text.lower()
print(new_text)  # hello python!

text = text.lower()
print(text)  # hello python!

# String data type methods
# Methods for changing case

# capitalize() - first letter uppercase
text = "hello python!"
print(text.capitalize())  # Hello python!

# casefold() - all letters lowercase
text = "HELLO PYTHON!"
print(text.casefold())  # hello python!

# lower() - all letters lowercase
text = "Hello Python!"
print(text.lower())  # hello python!
print(text)  # Hello Python!

lower_next = text.lower()
print(lower_next)  # hello python!

# upper() - all letters uppercase
txt = "Hello, Python!"
new_txt = txt.upper()
print(new_txt)  # HELLO, PYTHON!

# title() - each word capitalized
txt = "hello, python!"
new_txt = txt.title()
print(new_txt)  # Hello, Python!

# Methods for checking string content

# isalnum() - all characters are alphanumeric
text = "TeslaModel3"
print(text.isalnum())  # True

text = "Tesla Model 3"
print(text.isalnum())  # False

text = "221"
print(text.isalnum())  # True

# isalpha() - all characters are letters
name = "John"
print(name.isalpha())  # True

name = "John12"
print(name.isalpha())  # False

text = "John T."
print(text.isalpha())  # False

# isdecimal() - all characters are decimal digits
value = "12345"
print(value.isdigit())  # True

value = "12.345"
print(value.isdigit())  # False

value = "\u0031"  # Unicode for 1
print(value.isdigit())  # True

# isdigit() - all characters are digits
text = "1234"
print(text.isdigit())  # True

text = "12.34"
print(text.isdigit())  # False

text = "12,34"
print(text.isdigit())  # False

text = "abcd123"
print(text.isdigit())  # False

# isidentifier() - string is a valid Python identifier
text = "1234"
print(text.isidentifier())  # False

text = "my_directory"
print(text.isidentifier())  # True

text = "Demo1234"
print(text.isidentifier())  # True

text = "1234demo"
print(text.isidentifier())  # False

text = "привіт"
print(text.isidentifier())  # True

# isnumeric() - all characters are numeric
text = "hello python"
print(text.isnumeric())  # False

text = "12.45"
print(text.isnumeric())  # False

text = "1245"
print(text.isnumeric())  # True

# islower() - all letters in string are lowercase
text = "hello python"
print(text.islower())  # True

text = "Hello Python"
print(text.islower())  # False

# isupper() - all letters in string are uppercase
text = "HELLO PYTHON!"
print(text.isupper())  # True

text = "Hello Python!"
print(text.isupper())  # False

# endswith() - string ends with specified suffix
text = "Hello Python!"
print(text.endswith("Python!"))  # True

# startswith() - string starts with specified prefix
txt = "Hello, Python!"
starts_with_hello = txt.startswith("Hello")
print(starts_with_hello)  # True

txt = "Hello, Python!"
starts_with_hello = txt.startswith("hello")
print(starts_with_hello)  # False

# Methods for formatting and joining strings

# format() - string formatting
txt = "You can buy it for only {price:.2f} dollars!"
print(txt.format(price=49))  # You can buy it for only 49.00 dollars!

price = 49.12345
txt = f"You can buy it for only {price:.2f} dollars!"
print(txt)  # You can buy it for only 49.12 dollars!

text1 = "My name is {name}, and I'm {age}".format(name="Anna", age=33)
print(text1)  # My name is Anna, and I'm 33

text2 = "My name is {0}, and I'm {1}".format("Anna", 23)
print(text2)  # My name is Anna, and I'm 23

text3 = "My name is {}, and I'm {}".format("Derik", 18)
print(text3)  # My name is Derik, and I'm 18

# %-formatting
text = "My name is %s, and I'm %s" % ("Anna", 23)
print(text)  # My name is Anna, and I'm 23

# join() - joining elements of an iterable into a string
my_list = ["123", "456", "789"]
result = "-".join(my_list)
print(result)  # 123-456-789

result = "-".join(["123", "456", "789"])
print(result)  # 123-456-789

text = "abcd"
print(".".join(text))  # a.b.c.d

# replace() - replacing substring in string
txt = "My favorite programming language is C++!"
new_text = txt.replace("C++", "Python")
print(new_text)  # My favorite programming language is Python!

# split() - splitting string into list of substrings
text = "John, Anna, Joachim"
names = text.split(", ")
print(names)  # ['John', 'Anna', 'Joachim']

# splitlines() - splitting string into list of lines
txt = "Thanks for choosing programming!\nWelcome to the jungle!"
lines = txt.splitlines()
print(lines)  # ['Thanks for choosing programming!', 'Welcome to the jungle!']

# Methods for working with whitespace

# lstrip() - removing spaces from the left
txt = "     Python     "
new_text = txt.lstrip()

print(f"My favorite language is: {txt}!")
print(f"My favorite language is: {new_text}!")

# rstrip() - removing spaces from the right
txt = "     Python     "
new_text = txt.rstrip()

print(f"My favorite language is: {txt}!")
print(f"My favorite language is: {new_text}!")

# strip() - removing spaces from left and right
txt = "     Python     "
new_text = txt.strip()

print(f"My favorite language is: {txt}!")
print(f"My favorite language is: {new_text}!")

# count() - counting occurrences of substring in string
text = "Hello Python!. Python is my favorite programming language."

print(text.count("Python"))  # 2
print(text.count("python"))   # 0
print(text.count("Python", 10))  # 1

# find() - searching for substring in string, returns index of first occurrence or -1
text = "Hello Python!"

print(text.find("Python!"))  # 6
print(text.find("python"))  # -1
print(text.find("THE"))  # -1

# 16.4 Encoding and decoding text

# encoding string to bytes
text = "Hello Python!"
bytes_encoded = text.encode(encoding="utf-8")
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'Hello Python!'

# decoding bytes to string
text = "Hello Python!"
bytes_encoded = text.encode()
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'Hello Python!'

decoded_text = bytes_encoded.decode()
print(type(decoded_text))  # <class 'str'>
print(decoded_text)  # Hello Python!

# encoding and decoding with ASCII
text = "Hello Python!"
bytes_encoded = text.encode(encoding="ASCII")
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'Hello Python!'

decoded_text = bytes_encoded.decode(encoding="ASCII")
print(type(decoded_text))  # <class 'str'>
print(decoded_text)  # Hello Python!

# example of decoding error
text = "Привіт Python!"
bytes_encoded = text.encode(encoding="ISO 8859-5")  # Cyrillic alphabet
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'\xbf\xe0\xd8\xd2\xf6\xe2 Python!'

decoded_text = bytes_encoded.decode(
    encoding="UTF-8"
)

# example of decoding without error
text = "Привіт Python!"
bytes_encoded = text.encode(encoding="ISO 8859-5")  # Cyrillic alphabet
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'\xbf\xe0\xd8\xd2\xf6\xe2 Python!'

decoded_text = bytes_encoded.decode(encoding="ISO 8859-5")
print(decoded_text)  # Привіт Python!

# 16.6 Preparing for the 'Guess the Word' game

# Basic variables and initial messages
word = "apple"
attempts = 6
guessed_letters = ""

print("Welcome to the Word Guessing Game!")
print(f"You have {attempts} attempts to guess the word.")
print("Try to guess the word.")
print("_ " * len(word))

# Input and validation of entered value
guess = input("Guess a letter: ").lower()
if not guess.isalpha() or len(guess) > 1:
    print("Please try again. Enter a correct letter.")
    exit()

if guess not in word:
    attempts -= 1
    print(
        f"Oops! The letter '{guess}' is not in the word. "
        f"You have {attempts} attempts left."
    )
else:
    print(f"Good guess! '{guess}' is in the word.")

guessed_letters = f"{guessed_letters}{guess}"  # or guessed_letters += guess
