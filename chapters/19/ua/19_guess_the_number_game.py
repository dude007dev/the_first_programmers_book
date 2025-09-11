# 19. Гра “Вгадай число”

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 5 attempts to guess it.")

secret_number = random.randint(1, 100)

for attempt in "12345":  # Надаємо гравцеві 5 спроб
    guess = None
    while guess is None:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    if guess < secret_number:
        print("Too low. Try a higher number.")
    elif guess > secret_number:
        print("Too high. Try a lower number.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} correctly on attempt {attempt}.")
        exit()

print(f"Sorry, you've used all your attempts. The correct number was {secret_number}.")
