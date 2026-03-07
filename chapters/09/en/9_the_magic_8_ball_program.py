# 9. The Magic 8 Ball
from random import randint

answers = [
    "Yes",
    "You may rely on it",
    "Ask again later",
    "Concentrate and ask again",
    "My sources say no",
    "Very doubtful",
]

question = input("Enter your question: ")

index = randint(0, 5)  # generates a number from 0 to 5 inclusive
print(answers[index])
