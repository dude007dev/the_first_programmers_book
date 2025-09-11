# 16. Текстовий тип даних

name = 'John Smith'
name = "John Smith"  # те саме

# Багаторядковий текст. Варіант 1
some_text = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(some_text)

# Багаторядковий текст. Варіант 2
random_text = "Lorem ipsum dolor sit amet," \
    "consectetur adipiscing elit," \
    "sed do eiusmod tempor incididunt" \
    "ut labore et dolore magna aliqua."

print(random_text)

# Відображення тексту у кілька рядків
random_text = "Lorem ipsum dolor sit amet,\n" \
    "consectetur adipiscing elit,\n" \
    "sed do eiusmod tempor incididunt\n" \
    "ut labore et dolore magna aliqua."

print(random_text)

# Багаторядковий текст. Варіант 3 (рекомендований)
random_text = (
    "Lorem ipsum dolor sit amet,\n"
    "consectetur adipiscing elit,\n"
    "sed do eiusmod tempor incididunt\n"
    "ut labore et dolore magna aliqua."
)

print(random_text)

# текст в дужках
random_text = ("Lorem")
print(random_text)  # Lorem

random_text = ("Lorem", "ipsum")
print(random_text)  # ('Lorem', 'ipsum')

# подвійні лапки в тексті
text = "Hello, \"Python!\""
print(text)  # Hello, "Python!"

# 16.1 Текст як послідовність символів

# індексація символів в тексті
text = "Hello World!"
print(text[0])  # H
print(text[1])  # e
print(text[2])  # l

print(type(text))  # <class 'str'>

# належність символу до тексту
text = "Hello World!"
print("l" in text)  # True
print("L" in text)  # False
print("q" not in text)  # True

# 16.2 Нарізка рядків (slicing)

# нарізка тексту
text = "Hello Python!"
print(text[6:12])  # Python

# різні варіанти нарізки тексту
text = "Hello Python!"

print(text[0:13])  # Hello Python!
print(text[0:len(text)])  # Hello Python!
print(text[0:])  # Hello Python!
print(text[:len(text)])  # Hello Python!
print(text[:])  # Hello Python!

# нарізка з негативними індексами
text = "Hello Python!"
print(text[-7:-1])  # Python

# крок нарізки
text = "Hello Python!"
print(text[6:12:2])  # Pto

# 16.3 Функції й методи для тексту

# приклад з оператором +
"Hello " + "Python!"  # об'єднання через оператор +
" ".join(["Hello", "Python!"])  # об'єднання через метод join

# довжина тексту
text = "Hello World!"
print(len(text))  # 12

# приклад використання функції
print("Hello, World!")
print("Hello,", "World!")

# приклад використання методу
text = "hello world!"
print(text.title())  # Hello World!

# приклад повернення результату від методу
text = "HELLO PYTHON!"

print(text.lower())  # hello python!
print(text)  # HELLO PYTHON!

new_text = text.lower()
print(new_text)  # hello python!

text = text.lower()
print(text)  # hello python!

# Методи типу даних string (рядків тексту)
# Методи для зміни регістру

# capitalize() - перша літера велика
text = "hello python!"
print(text.capitalize())  # Hello python!

# casefold() - всі літери малі
text = "HELLO PYTHON!"
print(text.casefold())  # hello python!

# lower() - всі літери малі
text = "Hello Python!"
print(text.lower())  # hello python!
print(text)  # Hello Python!

lower_next = text.lower()
print(lower_next)  # hello python!

# upper() - всі літери великі
txt = "Hello, Python!"
new_txt = txt.upper()
print(new_txt)  # HELLO, PYTHON!

# title() - кожне слово з великої літери
txt = "hello, python!"
new_txt = txt.title()
print(new_txt)  # Hello, Python!

# Методи для перевірки вмісту рядка

# isalnum() - всі символи є буквено-цифровими
text = "TeslaModel3"
print(text.isalnum())  # True

text = "Tesla Model 3"
print(text.isalnum())  # False

text = "221"
print(text.isalnum())  # True

# isalpha() - всі символи є літерами
name = "John"
print(name.isalpha())  # True

name = "John12"
print(name.isalpha())  # False

text = "John T."
print(text.isalpha())  # False

# isdecimal() - всі символи є десятковими цифрами
value = "12345"
print(value.isdigit())  # True

value = "12.345"
print(value.isdigit())  # False

value = "\u0031"  # Unicode for 1
print(value.isdigit())  # True

# isdigit() - всі символи є цифрами
text = "1234"
print(text.isdigit())  # True

text = "12.34"
print(text.isdigit())  # False

text = "12,34"
print(text.isdigit())  # False

text = "abcd123"
print(text.isdigit())  # False

# isidentifier() - рядок є дійсним ідентифікатором Python

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

# isnumeric() - всі символи є числовими
text = "hello python"
print(text.isnumeric())  # False

text = "12.45"
print(text.isnumeric())  # False

text = "1245"
print(text.isnumeric())  # True

# islower() - всі літери в рядку є малими
text = "hello python"
print(text.islower())  # True

text = "Hello Python"
print(text.islower())  # False

# isupper() - всі літери в рядку є великими
text = "HELLO PYTHON!"
print(text.isupper())  # True

text = "Hello Python!"
print(text.isupper())  # False

# endswith() - рядок закінчується вказаним суфіксом
text = "Hello Python!"
print(text.endswith("Python!"))  # True

# startswith() - рядок починається з вказаного префікса
txt = "Hello, Python!"
starts_with_hello = txt.startswith("Hello")
print(starts_with_hello)  # True

txt = "Hello, Python!"
starts_with_hello = txt.startswith("hello")
print(starts_with_hello)  # False

# Методи для форматування та з'єднання рядків

# format() - форматування рядка
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

# %-форматування
text = "My name is %s, and I'm %s" % ("Anna", 23)
print(text)  # My name is Anna, and I'm 23

# join() - об'єднання елементів ітерованого об'єкта в рядок
my_list = ["123", "456", "789"]
result = "-".join(my_list)
print(result)  # 123-456-789

result = "-".join(["123", "456", "789"])
print(result)  # 123-456-789

text = "abcd"
print(".".join(text))  # a.b.c.d

# replace() - заміна підрядка в рядку
txt = "My favorite programming language is C++!"
new_text = txt.replace("C++", "Python")
print(new_text)  # My favorite programming language is Python!

# split() - розбиття рядка на список підрядків
text = "John, Anna, Joachim"
names = text.split(", ")
print(names)  # ['John', 'Anna', 'Joachim']

# splitlines() - розбиття рядка на список рядків
txt = "Thanks for choosing programming!\nWelcome to the jungle!"
lines = txt.splitlines()
print(lines)  # ['Thanks for choosing programming!', 'Welcome to the jungle!']

# Методи для роботи з пробілами

# lstrip() - видалення пробілів зліва
txt = "     Python     "
new_text = txt.lstrip()

print(f"My favorite language is: {txt}!")
print(f"My favorite language is: {new_text}!")

# rstrip() - видалення пробілів справа
txt = "     Python     "
new_text = txt.rstrip()

print(f"My favorite language is: {txt}!")
print(f"My favorite language is: {new_text}!")

# strip() - видалення пробілів зліва і справа
txt = "     Python     "
new_text = txt.strip()

print(f"My favorite language is: {txt}!")
print(f"My favorite language is: {new_text}!")

# count() - підрахунок входжень підрядка в рядок
text = "Hello Python!. Python is my favorite programming language."

print(text.count("Python"))  # 2
print(text.count("python"))   # 0
print(text.count("Python", 10))  # 1

# find() - пошук підрядка в рядку, повертає індекс першого входження або -1
text = "Hello Python!"

print(text.find("Python!"))  # 6
print(text.find("python"))  # -1
print(text.find("THE"))  # -1

# 16.4 Кодування і декодування тексту

# кодування рядка в байти
text = "Hello Python!"
bytes_encoded = text.encode(encoding="utf-8")
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'Hello Python!'

# декодування байтів в рядок
text = "Hello Python!"
bytes_encoded = text.encode()
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'Hello Python!'

decoded_text = bytes_encoded.decode()
print(type(decoded_text))  # <class 'str'>
print(decoded_text)  # Hello Python!

# кодування і декодування з ASCII
text = "Hello Python!"
bytes_encoded = text.encode(encoding="ASCII")
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'Hello Python!'

decoded_text = bytes_encoded.decode(encoding="ASCII")
print(type(decoded_text))  # <class 'str'>
print(decoded_text)  # Hello Python!

# приклад помилки декодування
text = "Привіт Python!"
bytes_encoded = text.encode(encoding="ISO 8859-5")  # Cyrillic alphabet
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'\xbf\xe0\xd8\xd2\xf6\xe2 Python!'

decoded_text = bytes_encoded.decode(
    encoding="UTF-8"
)

# приклад декодування без помилки
text = "Привіт Python!"
bytes_encoded = text.encode(encoding="ISO 8859-5")  # Cyrillic alphabet
print(type(bytes_encoded))  # <class 'bytes'>
print(bytes_encoded)  # b'\xbf\xe0\xd8\xd2\xf6\xe2 Python!'

decoded_text = bytes_encoded.decode(encoding="ISO 8859-5")
print(decoded_text)  # Привіт Python!

# 16.6 Підготовка до гри “вгадай слово”

# Базові змінні та початкові повідомлення
word = "apple"
attempts = 6
guessed_letters = ""

print("Welcome to the Word Guessing Game!")
print(f"You have {attempts} attempts to guess the word.")
print("Try to guess the word.")
print("_ " * len(word))

# Введення та перевірка введеного значення
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

guessed_letters = f"{guessed_letters}{guess}"  # або guessed_letters += guess
