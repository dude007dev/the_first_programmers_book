# 18. Loops

# 18.1 while loop

# Example of infinite loop
while True:
    print("Hello Python!")

print("We are outside the while loop")

# Example of infinite loop with counter
i = 1
while True:
    print("Hello Python!", i)
    i += 1  # i = i + 1

print("We are outside the while loop")

# Example of loop with condition
input_value = ""
while input_value != "exit":
    input_value = input("Enter your name: ")
    if input_value != "exit":
        print(f"Hello, {input_value}!")

print("We are outside the while loop")

# 18.2 Keywords break and continue

# Example of using break
while True:
    input_value = input("Enter your name: ")
    if input_value == "exit":
        break  # exit the loop

    print(f"Hello, {input_value}!")

print("We are outside the while loop")

# incorrect use of break
name = "John"
if name == "John":
    break  # SyntaxError: 'break' outside loop

print("Hello, John!")

# illogical use of break
while True:
    break
    input_value = input("Enter your name: ")
    if input_value == "exit":
        break

    if input_value == "q":
        break

    print(f"Hello, {input_value}!")

print("We are outside the while loop")

# Example of using continue
while True:
    input_value = input("Enter your favorite programming language: ")
    if input_value.lower() == "exit":
        break

    print(f"Your favorite programming language is: {input_value}.")

    if input_value.lower() != "python":
        continue

    print("Nice choice!")

print("We are outside the while loop")

# 18.3 While loop in the game “Guess the Word”

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

# 18.4 for loop

# Example of for loop
word = "example"
for letter in word:
    print(f"This is a letter: {letter}")

print("Out of the loop!")

# Example of for loop with empty string
word = ""
for letter in word:
    print(f"This is a letter: {letter}")  # nothing will be printed

print("Out of the loop!")

# Example of for loop using break and continue
word = "Poker"
for l in word.lower():
    if l == "p":
        continue

    print(l)

    if l == "k":
        break

# 18.5 For loop in the game “Guess the Word”

# Example of displaying guessed and not guessed letters
word = "apple"
guessed_letters = "rep"

display_word = ""
for letter in word:
    if letter in guessed_letters:
        display_word = f"{display_word}{letter} "
    else:
        display_word = f"{display_word}_ "

print(display_word)  # Output: _ p p _ e

# Example of checking if letters are in guessed letters
word = "apple"
guessed_letters = "rep"

print("The word is:", word)
for letter in word:
    if letter in guessed_letters:
        print(f"The letter '{letter}' is in the guessed letters '{guessed_letters}'.")
    else:
        print(f"The letter '{letter}' is not in the guessed letters '{guessed_letters}'.")

# initial example of checking if all letters are in guessed letters
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

# corrected example of checking if all letters are in guessed letters
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
