# 10. Що таке баг

# 10.1 Як виникають баги

# Приклад багу, який виникає завжди
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
print(answers[6])  # Помилка! IndexError: list index out of range

# Приклад багу, який виникає інколи
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

index = randint(0, 6)  # дає число від 0 до 6 включно
print(answers[index])
