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

index = randint(0, 5)  # дає число від 0 до 5 включно
print(answers[index])
