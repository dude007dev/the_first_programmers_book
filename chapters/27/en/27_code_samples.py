# 27. Song Words Counter

# variable with song text
text = """
Ніч яка місячна,
Зоряна, ясная,
Видно, хоч голки збирай

Вийди, коханая
Працею зморена
Хоч на хвилиноньку в гай
...
"""

# replacing newline characters with spaces
text = text.replace("\n", " ")

# iterating through text elements
for el in text:
    print(el)  # "Н"

# splitting text into words
text = text.replace("\n", " ")
words_list = text.split(" ")
for word in words_list:
    print(word)  # Ніч

# alternative option
text = text.replace("\n", " ")
for word in text.split(" "):
    print(word)  # Ніч


# printing word and its length
text = text.replace("\n", " ")
for word in text.split(" "):
    print(word, len(word))  # Ніч 3

# filtering unnecessary characters and empty lines
text = """
Ніч яка місячна,
Зоряна, ясная,
Видно, хоч голки збирай

Вийди, коханая
Працею зморена
Хоч на хвилиноньку в гай
"""

text = text.replace("\n", " ")
for word in text.split(" "):
    word = word.replace(",", "")
    word = word.strip()
    if len(word) > 2:
        print(word, len(word))  # Ніч 3

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
Ніч яка місячна,
Зоряна, ясная,
Видно, хоч голки збирай

Вийди, коханая
Працею зморена
Хоч на хвилиноньку в гай
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

print(target_word, counter)  # Ніч 1

# 27.1 Other Ways to Solve the Problem

# 1) using defaultdict
from collections import defaultdict

words_dict = defaultdict(int)

print(words_dict["example"])  # 0

words_dict["example"] += 1
print(words_dict["example"])  # 1

# updated code of program using defaultdict
from collections import defaultdict

text = """
Ніч яка місячна,
Зоряна, ясная,
Видно, хоч голки збирай

Вийди, коханая
Працею зморена
Хоч на хвилиноньку в гай

Сядемо вкупочці ми під калиною
І над панами я пан
Глянь, моя рибонько, срібною хвилею
Стелиться в полі туман

Ти не лякайся, що ніженьки босії
Вмочиш в холодну росу
Я ж тебе, вірную, аж до хатиноньки
Сам на руках однесу

Небо незміряне всипано зорями
Перлами теж під тополями
Що то за Божа краса?
Грає перлиста роса

Ти не лякайся, що ніженьки
Вмочиш в холодную росу ти
Ти не лякайся, що змерзнеш ти
Лебедонько

Сядемо вкупочці
Ми під калиною
І над панами ти
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

print(target_word, counter)  # під 3

# 2) using "Counter" data type

from collections import Counter, defaultdict

text = """
Ніч яка місячна,
Зоряна, ясная,
Видно, хоч голки збирай

Вийди, коханая
Працею зморена
Хоч на хвилиноньку в гай

Сядемо вкупочці ми під калиною
І над панами я пан
Глянь, моя рибонько, срібною хвилею
Стелиться в полі туман

Ти не лякайся, що ніженьки босії
Вмочиш в холодну росу
Я ж тебе, вірную, аж до хатиноньки
Сам на руках однесу

Небо незміряне всипано зорями
Перлами теж під тополями
Що то за Божа краса?
Грає перлиста роса

Ти не лякайся, що ніженьки
Вмочиш в холодную росу ти
Ти не лякайся, що змерзнеш ти
Лебедонько

Сядемо вкупочці
Ми під калиною
І над панами ти
"""
text = text.replace("\n", " ")
words_dict = defaultdict(int)
for word in text.split(" "):
    word = word.replace(",", "")
    word = word.strip()
    if len(word) > 2:
        words_dict[word] += 1

counter = Counter(words_dict)
print(counter.most_common(3))  # [('під', 3), ('лякайся', 3), ('Сядемо', 2)]

# 3) using dictionary sorting

# example of sorting function with tuple data type
my_tuple = (5, 2, 1)
print(sorted(my_tuple))  # [1, 2, 5]

# example of sorting function using `key` parameter
my_tuple = (("a", 33), ("b", 1), ("c", 2))
print(sorted(my_tuple, key=lambda item: item[1]))  # [('b', 1), ('c', 2), ('a', 33)]

# example of sorting dictionary by value
sorted_words = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_words[0])

# full code of program using dictionary sorting
from collections import defaultdict

text = """
Ніч яка місячна,
Зоряна, ясная,
Видно, хоч голки збирай

Вийди, коханая
Працею зморена
Хоч на хвилиноньку в гай

Сядемо вкупочці ми під калиною
І над панами я пан
Глянь, моя рибонько, срібною хвилею
Стелиться в полі туман

Ти не лякайся, що ніженьки босії
Вмочиш в холодну росу
Я ж тебе, вірную, аж до хатиноньки
Сам на руках однесу

Небо незміряне всипано зорями
Перлами теж під тополями
Що то за Божа краса?
Грає перлиста роса

Ти не лякайся, що ніженьки
Вмочиш в холодную росу ти
Ти не лякайся, що змерзнеш ти
Лебедонько

Сядемо вкупочці
Ми під калиною
І над панами ти
"""
text = text.replace("\n", " ")
words_dict = defaultdict(int)
for word in text.split(" "):
    word = word.replace(",", "")
    word = word.strip()
    if len(word) > 2:
        words_dict[word] += 1

sorted_words = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_words[0])  # ('під', 3)

# 4) extracting words using regular expressions

import re

text = """Ніч яка місячна, Зоряна, ясная,"""
words_list = re.findall(r"\w+", text)
print(words_list)  # ['Ніч', 'яка', 'місячна', 'Зоряна', 'ясная']

# 27.3 Independent Work

# filtering of service words
service_words = {"і", "та", "але", "в", "на", "до", "що", "як"}
