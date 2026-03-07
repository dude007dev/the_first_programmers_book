# 9. The Magic 8 Ball

# 9.1 Creating a list of answers
answers = [
    "Yes",
    "You may rely on it",
    "Ask again later",
    "Concentrate and ask again",
    "My sources say no",
    "Very doubtful",
]

# 9.2 Creating a question
question = input("Enter your question: ")
print(question)  # temporary line for checking, debugging

print(1, 2, "c")  # output: 1 2 c

# 9.3 Selecting an element from the list of answers
answers = [
    "Yes",
    "You may rely on it",
    "Ask again later",
    "Concentrate and ask again",
    "My sources say no",
    "Very doubtful",
]
print(answers[0])  # first element of the list - "Yes"
print(answers[5])  # "Very doubtful"

print([1, 2, "c", "d"][2])  # 'c', because it's the element with index 2

print(answers[5])  # equivalent to ["Yes", ..., "Very doubtful"][5]

# 9.4 Intermediate result
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

# 9.5 Random number selection
from random import randint

index = randint(0, 5)  # generates a number from 0 to 5 inclusive
print(index)
