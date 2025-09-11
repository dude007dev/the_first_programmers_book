# 8 Типи даних

# 8.1 Типи даних

# Цілі числа (integers)
age = 20
temperature = -5

# Дійсні числа (float)
height = 1.65
pi = 3.14159

# Комплексні числа (complex)
x = 100 + 3j

# Логічний тип (boolean)
is_student = True
has_access = False

# None (порожнє значення)
x = None
print(type(x))  # <class 'NoneType'>
x = "John"

# Текстовий тип (str)
name = "Maria"
message = 'Hello, world!'

# Байти (bytes)
my_text = b"hello user"

# Список (list)
x = [1, 2, 3, 4, 5]
my_friends = ["John", "Andrew", "Anna"]
my_list = [12, "Anna", 2022, True, [1, 2, 3]]

# Кортеж (tuple)
my_list = [1, 2]
my_list.append(3)
print(my_list)  # [1, 2, 3]

my_tuple = (1, 2)
my_tuple.append(3)  # помилка! У кортежа немає методу append

# Діапазон (range)
range(3)  # 0, 1, 2
range(0, 3)  # те саме: 0, 1, 2
print(list(range(3)))  # [0, 1, 2]

# Множина (set)
my_set = {"apple", "banana", "cherry", "apple"}
print(my_set)  # {"banana", "apple", "cherry"}

# Незмінна (заморожена) множина (frozenset)
my_set = frozenset({"apple", "banana", "cherry"})
# {"apple", "banana", "cherry"}
my_set2 = frozenset([1, 2, 5, 2])  # {1, 2, 5}

# Словник (dictionary)
my_eng_dict = {
    "experience": "досвід",
    "knowledge": "знання",
}

print(my_eng_dict["experience"])  # досвід

my_dict = {"UA": "Ukraine", "NL": "Netherlands"}
print(my_dict["UA"])  # Ukraine

# 8.2 Спеціальні типи даних

import datetime

now = datetime.datetime.now()
print(now)

# 8.3 Змінні та незмінні типи даних

# Змінний тип даних
names_list = ["Joachim", "Elon"]
names_list.append("Anna")
print(names_list)  #  ["Joachim", "Elon", "Anna"]

# Незмінний тип даних
text = "My name is "
text.add("John")  # error, exception
text.append("Anna")  # error, exception

# Змінюємо тип даних
text = "My name is"
text = text + " John"
print(text)  # My name is John
# or
text = "My name is"
text = f"{text} John"
print(text)  # My name is John
# or
text = "My name is %s"
text = text % ("John")
print(text)  # My name is John
