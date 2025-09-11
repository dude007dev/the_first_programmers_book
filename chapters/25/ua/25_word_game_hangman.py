# 25. Word Game: Hangman

import random

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
  |   |
  |   |
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
/ |   |
  |   |
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
/     |
|     |
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


words = ("apple", "banana", "strawberry")
word = random.choice(words)

attempts = len(hanged_man) - 1
guessed_values = set()

print("Welcome to the Word Game: Hangman!")
print(f"You have {attempts} attempts to guess the word.")
print("Try to guess the word.")
print(hanged_man[0])
print("_ " * len(word))

while attempts > 0:
    guess = input("Guess a letter or the whole word: ").lower()
    # check if the input is a letter/word
    if not guess.isalpha():
        print("Please enter a correct letter or a word.")
        continue

    # check if the letter/word has already been guessed
    if guess in guessed_values:
        print("You've already guessed that word/letter.")
        continue

    guessed_values.add(guess)

    # Check if the entered value is the word
    if guess == word:
        print("Congratulations! You've guessed the word:", word)
        break
    elif len(guess) > 1:
        print(hanged_man[-attempts])
        attempts -= 1
        print(f"Oops! '{guess}' is not the correct word. You have {attempts} attempts left.")
        continue

    # Check if the entered (guessed) letter is in the word
    if guess not in word:
        print(hanged_man[-attempts])
        attempts -= 1
        print(f"Oops! The letter '{guess}' is not in the word. You have {attempts} attempts left.")
    else:
        print(f"Good guess! '{guess}' is in the word.")

    # Display the current state of the word
    display_word = ""
    for letter in word:
        if letter in guessed_values:
            display_word = f"{display_word}{letter} "
        else:
            display_word = f"{display_word}_ "
    print(display_word)

    # Check if all letters have been guessed
    if all([letter in guessed_values for letter in word]):
        print("Congratulations! You've guessed the word:", word)
        break

if attempts == 0:
    print("Sorry, you ran out of attempts. The word was:", word)
