# 29. Word Game: Hangman with Functions

# template for main game function
import random


def game_hangman():
    pass


game_hangman()

# 29.1 Function for Getting Hangman Drawing


def get_hangman_drawing(stage_number):
    """Return the hangman drawing for the given stage number.

    Args:
        stage_number (int): The stage number (index in the list) of the hangman drawing.

    Returns:
        str: The hangman drawing.
    """
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
        # ... (other hangman drawings) ...
        """1""",
        """2""",
        """3""",
        """4""",
        """5""",
        """6""",
    )
    return hanged_man[stage_number]


print(get_hangman_drawing(0))

# example of running function `get_hangman_drawing` with indices
attempts = 6
hanged_man = (0, 1, 2, 3, 4, 5, 6)

print(hanged_man[-attempts])

print(get_hangman_drawing(-attempts))

print(get_hangman_drawing(stage_number=-attempts))

# 29.2 Updated Variant of Game Initialization


def game_hangman():
    """Play the hangman game."""
    words = ("apple", "banana", "strawberry")
    word = random.choice(words)

    attempts = 6  # len(hanged_man) - 1
    current_attempt = 0
    guessed_values = set()

    print("Welcome to the Word Game: Hangman!")
    print(f"You have {attempts} attempts to guess the word.")
    print("Try to guess the word.")
    print(get_hangman_drawing(0))
    print("_ " * len(word))

    while current_attempt < attempts:
        pass


# 29.3 Function for Initial Greetings

# previous greeting code
print("Welcome to the Word Game: Hangman!")
print(f"You have {attempts} attempts to guess the word.")
print("Try to guess the word.")
print(get_hangman_drawing(0))
print("_ " * len(word))


# new greeting function
def print_welcome_message(num_attempts, word):
    """Print welcome message for the Hangman game.

    Args:
        num_attempts (int): Number of attempts the player has to guess the word.
        word (str): The secret word to be guessed.

    Returns:
        None
    """
    print("Welcome to the Word Game: Hangman!")
    print(f"You have {num_attempts} attempts to guess the word.")
    print("Try to guess the word.")
    print(get_hangman_drawing(0))
    print("_ " * len(word))


# 29.4 Function for Validating Input

# previous code for checking input value
# check if the input is a letter/word
if not guess.isalpha():
    print("Please enter a correct letter or a word.")
    continue

# check if the letter/word has already been guessed
if guess in guessed_values:
    print("You've already guessed that word/letter.")
    continue


# new function for validating input value
def is_guess_valid(input_value, guessed_values):
    """Validate the player's guess.

    Args:
        input_value (str): The letter or word entered by the player.
        guessed_values (set): Letters or words that the player has already guessed.

    Returns:
        bool: True if the guess is valid, False otherwise.
    """
    if not input_value.isalpha():
        print("Please enter a correct letter or a word.")
        return False

    if input_value in guessed_values:
        print("You've already guessed that word/letter.")
        return False

    return True


# future usage of function `is_guess_valid`
if not is_guess_valid(input_value=guess, guessed_values=guessed_values):
    continue

# code structure after making changes
import random


def get_hangman_drawing(stage_number):
    pass


def print_welcome_message(num_attempts, word):
    pass


def is_guess_valid(input_value, guessed_values):
    pass
    return True


def game_hangman():
    """Play the hangman game."""
    words = ("apple", "banana", "strawberry")
    word = random.choice(words)

    attempts = 6
    current_attempt = 0
    guessed_values = set()

    print_welcome_message(num_attempts=attempts, word=word)

    while current_attempt < attempts:
        guess = input("Guess a letter or the whole word: ").lower()
        if not is_guess_valid(input_value=guess, guessed_values=guessed_values):
            continue
        pass


game_hangman()

# 29.5 Function for Displaying Word Progress

# previous code for displaying current word state
# Display the current state of the word
display_word = ""
for letter in word:
    if letter in guessed_values:
        display_word = f"{display_word}{letter} "
    else:
        display_word = f"{display_word}_ "
print(display_word)


# new function for displaying current word state
def display_word_progress(word, guessed_values):
    """Show the word with guessed letters revealed and underscores for the rest.

    Args:
        word (str): The secret word to be guessed.
        guessed_values (set): Letters or words that the player has already guessed.

    Returns:
        None
    """
    display_word = ""
    for letter in word:
        if letter in guessed_values:
            display_word = f"{display_word}{letter} "
        else:
            display_word = f"{display_word}_ "
    print(display_word)


# 29.6 Final Appearance of Main Function


def game_hangman():
    """Play the hangman game."""
    words = ("apple", "banana", "strawberry")
    word = random.choice(words)

    attempts = 6
    current_attempt = 0
    guessed_values = set()

    print_welcome_message(num_attempts=attempts, word=word)

    while current_attempt < attempts:
        guess = input("Guess a letter or the whole word: ").lower()
        if not is_guess_valid(input_value=guess, guessed_values=guessed_values):
            continue

        guessed_values.add(guess)

        # Check if the entered value is the word
        if guess == word:
            print("Congratulations! You've guessed the word:", word)
            break
        elif len(guess) > 1:
            current_attempt += 1
            print(get_hangman_drawing(stage_number=current_attempt))
            print(f"Oops! '{guess}' is not the correct word. You have {attempts - current_attempt} attempts left.")
            continue

        # Check if the entered (guessed) letter is in the word
        if guess not in word:
            current_attempt += 1
            print(get_hangman_drawing(stage_number=current_attempt))
            print(
                f"Oops! The letter '{guess}' is not in the word. "
                f"You have {attempts - current_attempt} attempts left."
            )
        else:
            print(f"Good guess! '{guess}' is in the word.")

        display_word_progress(word=word, guessed_values=guessed_values)

        # Check if all letters have been guessed
        if all([letter in guessed_values for letter in word]):
            print("Congratulations! You've guessed the word:", word)
            break

    if current_attempt == attempts:
        print("Sorry, you ran out of attempts. The word was:", word)


# 29.8 Independent practice

from random import randint


def the_magic_8_ball():
    """Docstring example."""
    pass


the_magic_8_ball()
