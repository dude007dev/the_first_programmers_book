# 27. Song Words Counter

# змінна з текстом пісні
text = """
Ніч яка місячна,
Зоряна, ясная,
Видно, хоч голки збирай

Вийди, коханая
Працею зморена
Хоч на хвилиноньку в гай
...
"""

# заміна символів нового рядка на пробіли
text = text.replace("\n", " ")

# проходимо по елементах тексту
for el in text:
    print(el)  # "Н"

# розбиваємо текст на слова
text = text.replace("\n", " ")
words_list = text.split(" ")
for word in words_list:
    print(word)  # Ніч

# альтернативний варіант
text = text.replace("\n", " ")
for word in text.split(" "):
    print(word)  # Ніч


# виводимо слово та його довжину
text = text.replace("\n", " ")
for word in text.split(" "):
    print(word, len(word))  # Ніч 3

# фільтруємо зайві символи та порожні рядки
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

# словник для підрахунку слів
words_dict = {}

# заповнюємо словник
if words_dict.get(word):
    words_dict[word] += 1
else:
    words_dict[word] = 1

# альтернативний варіант
if word in words_dict:
    words_dict[word] += 1
else:
    words_dict[word] = 1

# проміжний код програми
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

# знаходимо слово-лідер
target_word = ""
counter = 0
for word, count in words_dict.items():
    if count > counter:
        target_word = word
        counter = count

print(target_word, counter)  # Ніч 1

# 27.1 Інші способи вирішення задачі

# 1) використовуючи defaultdict
from collections import defaultdict

words_dict = defaultdict(int)

print(words_dict["example"])  # 0

words_dict["example"] += 1
print(words_dict["example"])  # 1

# оновлений код програми з використанням defaultdict
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

# 2) за допомогою типу даних "лічильник"

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

# 3) за допомогою сортування словника

# приклад функції сортування з типом даних кортеж
my_tuple = (5, 2, 1)
print(sorted(my_tuple))  # [1, 2, 5]

# приклад функції сортування з використанням параметру `key`
my_tuple = (("a", 33), ("b", 1), ("c", 2))
print(sorted(my_tuple, key=lambda item: item[1]))  # [('b', 1), ('c', 2), ('a', 33)]

# приклад сортування словника за значенням
sorted_words = sorted(words_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_words[0])

# повний код програми з використанням сортування словника
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

# 4) виділення слів за допомогою регулярних виразів

import re

text = """Ніч яка місячна, Зоряна, ясная,"""
words_list = re.findall(r"\w+", text)
print(words_list)  # ['Ніч', 'яка', 'місячна', 'Зоряна', 'ясная']

# 27.3 Самостійна робота

# фільтрація службових слів
service_words = {"і", "та", "але", "в", "на", "до", "що", "як"}
