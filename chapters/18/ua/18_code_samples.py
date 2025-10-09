# 18. Цикли (loops)

# 18.1 Цикл while

# Приклад нескінченного циклу
while True:
    print("Hello Python!")

print("We are outside the while loop")

# Приклад нескінченного циклу з лічильником
i = 1
while True:
    print("Hello Python!", i)
    i += 1  # i = i + 1

print("We are outside the while loop")

# Приклад циклу з умовою
input_value = ""
while input_value != "exit":
    input_value = input("Enter your name: ")
    if input_value != "exit":
        print(f"Hello, {input_value}!")

print("We are outside the while loop")

# 18.2 Ключові слова break та continue

# Приклад використання break
while True:
    input_value = input("Enter your name: ")
    if input_value == "exit":
        break  # вихід із циклу

    print(f"Hello, {input_value}!")

print("We are outside the while loop")

# неправильне використання break
name = "John"
if name == "John":
    break  # SyntaxError: 'break' outside loop

print("Hello, John!")

# нелогічне використання break
while True:
    break
    input_value = input("Enter your name: ")
    if input_value == "exit":
        break

    if input_value == "q":
        break

    print(f"Hello, {input_value}!")

print("We are outside the while loop")

# Приклад використання continue
while True:
    input_value = input("Enter your favorite programming language: ")
    if input_value.lower() == "exit":
        break

    print(f"Your favorite programming language is: {input_value}.")

    if input_value.lower() != "python":
        continue

    print("Nice choice!")

print("We are outside the while loop")

# 18.3 Цикл while у грі “Вгадай слово”

word = "apple"
attempts = 6
guessed_letters = ""

print("Welcome to the Word Guessing Game!")
print(f"You have {attempts} attempts to guess the word.")
print("Try to guess the word.")
print("_ " * len(word))

while attempts > 0:
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) > 1:
        print("Please try again. Enter a correct letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    if guess not in word:
        attempts -= 1
        print(f"Oops! '{guess}' is not in the word. You have {attempts} attempts left.")
    else:
        print(f"Good guess! '{guess}' is in the word.")

    guessed_letters = f"{guessed_letters}{guess}"

if attempts == 0:
    print("Sorry, you ran out of attempts. The word was:", word)

# 18.4 Цикл for

# Приклад циклу for
word = "example"
for letter in word:
    print(f"This is a letter: {letter}")

print("Out of the loop!")

# Приклад циклу for з порожнім рядком
word = ""
for letter in word:
    print(f"This is a letter: {letter}")  # нічого не буде виведено

print("Out of the loop!")

# Приклад циклу for з використанням break та continue
word = "Poker"
for l in word.lower():
    if l == "p":
        continue

    print(l)

    if l == "k":
        break

# 18.5 Цикл for у грі “Вгадай слово”

# Приклад відображення вгаданих та невгаданих букв
word = "apple"
guessed_letters = "rep"

display_word = ""
for letter in word:
    if letter in guessed_letters:
        display_word = f"{display_word}{letter} "
    else:
        display_word = f"{display_word}_ "

print(display_word)  # Output: _ p p _ e

# Приклад перевірки наявності букв у вгаданих буквах
word = "apple"
guessed_letters = "rep"

print("The word is:", word)
for letter in word:
    if letter in guessed_letters:
        print(f"The letter '{letter}' is in the guessed letters '{guessed_letters}'.")
    else:
        print(f"The letter '{letter}' is not in the guessed letters '{guessed_letters}'.")

# початковий приклад перевірки наявності всіх букв у вгаданих буквах
word = "apple"
guessed_letters = "rep"

print("The word is:", word)
all_letters_guessed = True
for letter in word:
    if letter in guessed_letters:
        print(f"The letter '{letter}' is in the guessed letters '{guessed_letters}'.")
    else:
        print(f"The letter '{letter}' is not in the guessed letters '{guessed_letters}'.")
        all_letters_guessed = False
        break

print("All letters guessed:", all_letters_guessed)

# виправоений приклад перевірки наявності всіх букв у вгаданих буквах
word = "apple"
guessed_letters = "rep"

print("The word is:", word)
all_letters_guessed = False
for letter in word:
    if letter in guessed_letters:
        print(f"The letter '{letter}' is in the guessed letters '{guessed_letters}'.")
        all_letters_guessed = True
    else:
        print(f"The letter '{letter}' is not in the guessed letters '{guessed_letters}'.")
        all_letters_guessed = False
        break

print("All letters guessed:", all_letters_guessed)
