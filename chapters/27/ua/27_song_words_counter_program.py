# 27. Song Words Counter

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
words_dict = {}
for word in text.split(" "):
    word = word.replace(",", "")
    word = word.strip()
    if len(word) > 2:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

target_word = ""
counter = 0
for word, count in words_dict.items():
    if count > counter:
        target_word = word
        counter = count

print(target_word, counter)  # під 3
