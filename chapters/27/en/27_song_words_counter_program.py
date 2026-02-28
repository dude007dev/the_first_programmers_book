# 27. Song Words Counter

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

print(target_word, counter)  # when 8