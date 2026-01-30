# 25. Word Game: Hangman

# Initial version of "Guess the Word" game (predecessor to Hangman)
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

    guessed_letters = f"{guessed_letters}{guess}"  # or guessed_letters += guess

    if guess not in word:
        attempts -= 1
        print(f"Oops! '{guess}' is not in the word. You have {attempts} attempts left.")
    else:
        print(f"Good guess! '{guess}' is in the word.")

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word = f"{display_word}{letter} "
        else:
            display_word = f"{display_word}_ "
    print(display_word)

    all_letters_guessed = False
    for letter in word:
        if letter in guessed_letters:
            all_letters_guessed = True
        else:
            all_letters_guessed = False
            break

    if all_letters_guessed:
        print("Congratulations! You've guessed the word:", word)
        break

if attempts == 0:
    print("Sorry, you ran out of attempts. The word was:", word)

# 25.1 Displaying the Hanged Man

# display of hanged man (hangman)
hanged_man = (
    """
 -----
 |   |
     |
     |
     |
     |
     |
     |
     |
     |
-------
""",
    """
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
)

# number of attempts for guessing
attempts = len(hanged_man) - 1

# 25.2 Selecting a Word for the Game

import random

words = ("apple", "banana", "strawberry")
random_index = random.randint(0, len(words) - 1)
word = words[random_index]
print(word)

# simplified version of selecting a word
import random

words = ("apple", "banana", "strawberry")
word = random.choice(words)
print(word)

# 25.3 Recording Entered Values

# previous version
guessed_letters = ""
...
guessed_letters = f"{guessed_letters}{guess}"
...

# improved version
guessed_values = set()
guess = input("Guess a letter or the whole word: ").lower()
if guess in guessed_values:
    print("You've already guessed that word/letter.")
    # continue -> skip iteration, go to beginning of loop

guessed_values.add(guess)
...

# 25.4 Updated Way to Check End of Game

# попередня версія
while attempts > 0:
    ...
    all_letters_guessed = False
    for letter in word:
        if letter in guessed_letters:
            all_letters_guessed = True
        else:
            all_letters_guessed = False
            break

    if all_letters_guessed:
        print("Congratulations! You've guessed the word:", word)
        break

# using list comprehension
word = "banana"  # Example word for testing
guessed_values = {"a", "b", "c"}  # Example guessed letters
result = [letter in guessed_values for letter in word]
print(result)  # [True, True, False, True, False, True]

# checking complete word guessing
word = "banana"  # Example word for testing
guessed_values = {"c", "a", "n", "b"}  # Example guessed letters
result = [letter in guessed_values for letter in word]
print(result)  # [True, True, True, True, True, True]

# all() function
word = "banana"  # Example word for testing
guessed_values = {"c", "a", "n", "b"}  # Example guessed letters
result = [letter in guessed_values for letter in word]
if all(result):
    print("Congratulations! You've guessed the word:", word)

# writing without intermediate variable
word = "banana"
guessed_values = {"c", "a", "n", "b"}
if all([letter in guessed_values for letter in word]):
    print("Congratulations! You've guessed the word:", word)

# 25.7 Independent Work

# double while loop to keep track of wins
while True:
    word = random.choice(words)
    attempts = len(hanged_man) - 1
    guessed_values = set()
    while attempts > 0:
        guess = input("Guess a letter or the whole word: ").lower()
        ...

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
