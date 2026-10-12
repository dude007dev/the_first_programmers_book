# 27. Song Words Counter

# variable with song text
text = """
O, when the saints go marching in.
Lord, I want to be in that number
when the saints go marching in.

O when the sun refused to shine,
Lord, I want to be in that number
when the sun refused to shine.
...
"""

# replacing newline characters with spaces
text = text.replace("\n", " ")

# iterating through text elements
for el in text:
    print(el)  # "O"

# splitting text into words
text = text.replace("\n", " ")
words_list = text.split(" ")
for word in words_list:
    print(word)  # O,

# alternative option
text = text.replace("\n", " ")
for word in text.split(" "):
    print(word)  # O,


# printing word and its length
text = text.replace("\n", " ")
for word in text.split(" "):
    print(word, len(word))  # O, 2

# filtering unnecessary characters and empty lines
text = """
O, when the saints go marching in.
Lord, I want to be in that number
when the saints go marching in.

O when the sun refused to shine,
Lord, I want to be in that number
when the sun refused to shine.
"""

text = text.replace("\n", " ")
for word in text.split(" "):
    word = word.replace(",", "")
    word = word.strip()
    if len(word) > 2:
        print(word, len(word))  # when 4

# dictionary for counting words
words_dict = {}

# filling the dictionary
if words_dict.get(word):
    words_dict[word] += 1
else:
    words_dict[word] = 1

# alternative option
if word in words_dict:
    words_dict[word] += 1
else:
    words_dict[word] = 1

# intermediate code of program
text = """
O, when the saints go marching in.
Lord, I want to be in that number
when the saints go marching in.

O when the sun refused to shine,
Lord, I want to be in that number
when the sun refused to shine.
"""

text = text.replace("\n", " ")
words_dict = {}
for word in text.split(" "):
    word = word.replace(",", "")
    word = word.strip()
    if len(word) > 2:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

print(words_dict)

# finding the leading word
target_word = ""
counter = 0
for word, count in words_dict.items():
    if count > counter:
        target_word = word
        counter = count

print(target_word, counter)  # when 4


# 27.2 Independent practice

# filtering of service words
service_words = {"the", "and", "or", "but", "in", "on", "at", "to", "of", "a", "an", "when", "that"}


# 27.3 For the curious: other ways to solve similar tasks

# 1) using defaultdict
from collections import defaultdict

words_dict = defaultdict(int)

print(words_dict["example"])  # 0

words_dict["example"] += 1
print(words_dict["example"])  # 1

# updated code of program using defaultdict
from collections import defaultdict

text = """
O, when the saints go marching in.
Lord, I want to be in that number
when the saints go marching in.

O when the sun refused to shine,
Lord, I want to be in that number
when the sun refused to shine.

O when they gather 'round the throne,
Lord, I want to be in that number
when they gather 'round the throne.

O when they crown Him Lord of all,
Lord, I want to be in that number
when they crown Him Lord of all.

And on that hallelujah day,
Lord, I want to be in that number
on that hallelujah day.
"""
text = text.replace("\n", " ")
words_dict = defaultdict(int)
for word in text.split(" "):
    word = word.replace(",", "")
    word = word.strip()
    if len(word) > 2:
        words_dict[word] += 1

target_word = ""
counter = 0
for word, count in words_dict.items():
    if count > counter:
        target_word = word
        counter = count

print(target_word, counter)  # when 8

# 2) using "Counter" data type

from collections import Counter

text = """
O, when the saints go marching in.
Lord, I want to be in that number
when the saints go marching in.

O when the sun refused to shine,
Lord, I want to be in that number
when the sun refused to shine.

O when they gather 'round the throne,
Lord, I want to be in that number
when they gather 'round the throne.

O when they crown Him Lord of all,
Lord, I want to be in that number
when they crown Him Lord of all.

And on that hallelujah day,
Lord, I want to be in that number
on that hallelujah day.
"""
text = text.replace("\n", " ")
words = []

for word in text.split(" "):
    word = word.replace(",", "")
    word = word.strip()
    if len(word) > 2:
        words.append(word)

counter = Counter(words)
print(counter.most_common(3))  # [('when', 8), ('Lord', 7), ('that', 7)]

# 3) extracting words using regular expressions

import re

text = """O, when the saints go marching in."""
words_list = re.findall(r"\w+", text)
print(words_list)  # ['O', 'when', 'the', 'saints', 'go', 'marching', 'in']
