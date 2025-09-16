# 9. The Magic 8 Ball

# 9.1 Створюємо список відповідей
answers = [
    "Yes",
    "You may rely on it",
    "Ask again later",
    "Concentrate and ask again",
    "My sources say no",
    "Very doubtful",
]

# 9.2 Створюємо запитання
question = input("Enter your question: ")
print(question)  # тимчасовий рядок для перевірки, debugging

print(1, 2, "c")  # результат: 1 2 c

# 9.3 Вибираємо елемент зі списку відповідей
answers = [
    "Yes",
    "You may rely on it",
    "Ask again later",
    "Concentrate and ask again",
    "My sources say no",
    "Very doubtful",
]
print(answers[0])  # перший елемент списку - "Yes"
print(answers[5])  # "Very doubtful"

print([1, 2, "c", "d"][2])  # 'c', бо це елемент з індексом 2

print(answers[5])  # еквівалентно до [ "Yes", ..., "Very doubtful" ][5]

# 9.4 Проміжний результат
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

# 9.5 Випадковий вибір числа
from random import randint

index = randint(0, 5)  # дає число від 0 до 5 включно
print(index)
