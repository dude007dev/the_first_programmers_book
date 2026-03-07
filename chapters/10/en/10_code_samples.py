# 10. What is a Bug

# 10.1 How Bugs Arise

# Example of a bug that occurs always
answers = [
    "Yes",
    "You may rely on it",
    "Ask again later",
    "Concentrate and ask again",
    "My sources say no",
    "Very doubtful",
]

question = input("Enter your question: ")

print(question)
print(answers[1])  # 'You may rely on it'
print(answers[6])  # Error! IndexError: list index out of range

# Example of a bug that occurs sometimes
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

index = randint(0, 6)  # generates a number from 0 to 6 inclusive
print(answers[index])
