# 20. Гра “Вгадай слово”

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
        print(f"Oops! The letter '{guess}' is not in the word. You have {attempts} attempts left.")
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
