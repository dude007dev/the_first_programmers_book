# 25. Word Game: Hangman

# початкова версія гри "Відгадай слово" (повередника Hangman)
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

    guessed_letters = f"{guessed_letters}{guess}"  # або guessed_letters += guess

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

# 25.1 Зображення повішеного чоловіка

# зображення повішеного (hangman)
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

# кількість спроб для вгадування
attempts = len(hanged_man) - 1

# 25.2 Вибір слова для гри

import random

words = ("apple", "banana", "strawberry")
random_index = random.randint(0, len(words) - 1)
word = words[random_index]
print(word)

# спрощений варіант вибору слова
import random

words = ("apple", "banana", "strawberry")
word = random.choice(words)
print(word)

# 25.3 Запис введених значень

# попередня версія
guessed_letters = ""
...
guessed_letters = f"{guessed_letters}{guess}"
...

# покращена версія
guessed_values = set()
guess = input("Guess a letter or the whole word: ").lower()
if guess in guessed_values:
    print("You've already guessed that word/letter.")
    # continue -> пропускаємо ітерацію, йдемо до початку циклу

guessed_values.add(guess)
...

# 25.4 Оновлений спосіб перевірки закінчення гри

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

# використання list comprehension
word = "banana"  # Example word for testing
guessed_values = {"a", "b", "c"}  # Example guessed letters
result = [letter in guessed_values for letter in word]
print(result)  # [True, True, False, True, False, True]

# перевірка повного вгадування слова
word = "banana"  # Example word for testing
guessed_values = {"c", "a", "n", "b"}  # Example guessed letters
result = [letter in guessed_values for letter in word]
print(result)  # [True, True, True, True, True, True]

# функція all()
word = "banana"  # Example word for testing
guessed_values = {"c", "a", "n", "b"}  # Example guessed letters
result = [letter in guessed_values for letter in word]
if all(result):
    print("Congratulations! You've guessed the word:", word)

# запис без проміжної змінної
word = "banana"
guessed_values = {"c", "a", "n", "b"}
if all([letter in guessed_values for letter in word]):
    print("Congratulations! You've guessed the word:", word)

# 25.7 Самостійна робота

# подвійний цикл while для збереження кількості перемог
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
