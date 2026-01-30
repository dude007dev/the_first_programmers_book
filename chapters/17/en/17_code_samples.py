# 17. if...else... block

# 17.1 How the if...else... block works in Python

# Example 1
forecast = ["rain", "sun"]

if "storm" in forecast:
    print("Stay at home!")
elif "rain" in forecast and "sun" in forecast:
    print("Take an umbrella and sunglasses.")
elif "rain" in forecast:
    print("Take a jacket and an umbrella.")
elif "sun" in forecast:
    print("Take sunglasses.")

# 17.2 if...else... block in a program for grading on an A–F scale

value = input("Enter the percentage of correct answers of the test: ")
value = int(value)
if value >= 90:
    grade = "A"
elif value >= 80 and value < 90:
    grade = "B"
elif value >= 70 and value < 80:
    grade = "C"
elif value >= 60 and value < 70:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# 17.3 if...else... block in the 'Guess the Word' game

word = "apple"
attempts = 6
guessed_letters = ""

print("Welcome to the Word Guessing Game!")
print(f"You have {attempts} attempts to guess the word.")
print("Try to guess the word.")
print("_ " * len(word))

guess = input("Guess a letter: ").lower()
# first if...else... block
if not guess.isalpha() or len(guess) > 1:
    print("Please try again. Enter a correct letter.")
    exit()

# second if...else... block
if guess not in word:
    attempts -= 1
    print(f"Oops! '{guess}' is not in the word. You have {attempts} attempts left.")
else:
    print(f"Good guess! '{guess}' is in the word.")

guessed_letters = f"{guessed_letters}{guess}"  # guessed_letters += guess
