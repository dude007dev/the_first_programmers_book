# 26. Тип даних словник (dictionary)

# приклад створення порожнього словника
my_dict = {}

# приклад створення словника з одним елементом
my_dict = {"some key": "some value"}

# приклад створення словника з кількома елементами
my_en_ua_dict = {"experience": "досвід", "knowledge": "знання"}

# приклад створення словника з кількома елементами з комою в кінці
my_en_ua_dict = {
    "experience": "досвід",
    "knowledge": "знання",
}

# приклад доступу до елемента словника за ключем
my_en_ua_dict = {
    "experience": "досвід",
    "knowledge": "знання",
}

print(my_en_ua_dict["experience"])  # досвід

# приклад додавання нового елемента до словника
my_en_ua_dict = {
    "experience": "досвід",
    "knowledge": "знання",
}

my_en_ua_dict["skill"] = "навичка"
print(my_en_ua_dict)  # {'experience': 'досвід', 'knowledge': 'знання', 'skill': 'навичка'}

# приклад оновлення значення елемента словника за ключем
my_en_ua_dict = {
    "experience": "досвід",
}
my_en_ua_dict["experience"] = "нове значення"
print(my_en_ua_dict["experience"])  # нове значення

# прикоад звернення до неіснуючого ключа
my_en_ua_dict = {
    "knowledge": "досвід",
    "knowledge": "знання",
    True: "правда",
    "true": "правда",
}

print(my_en_ua_dict["experience"])  # KeyError: 'experience'

# приклад дублювання ключів у словнику
my_en_ua_dict = {
    "knowledge": "досвід",
    "knowledge": "знання",
    "knowledge": "повторення!!!",
    True: "правда",
    "true": "правда",
}

print(my_en_ua_dict["knowledge"])  # повторення!!!

# приклад використання різних типів даних як ключів словника
my_dict = {
    "experience": "досвід",
    True: ["п", "р", "а", "в", "д", "а"],
    "true": "правда",
    (1, 2): "кортеж",
}
print(my_dict[True])  # ['п', 'р', 'а', 'в', 'д', 'а']

# TypeError: unhashable type: 'list'
my_error_dict = {
    [1, 2]: "список",
}

# порядок елементів у словнику
my_dict = {
    "experience": "досвід",
    True: "правда",
    (1, 2): "кортеж",
}

print(my_dict)  # {'experience': 'досвід', True: 'правда', (1, 2): 'кортеж'}

# перебір елементів словника
my_dict = {
    "experience": "досвід",
    True: "правда",
    (1, 2): "кортеж",
}

for key in my_dict:
    print(f"The key is '{key}'. The value is: '{my_dict[key]}'")

# отримання ключа та значення елемента словника
my_dict = {
    "experience": "досвід",
    True: "правда",
    (1, 2): "кортеж",
}

for key, value in my_dict.items():
    print(f"The key is '{key}'. The value is: '{value}'")

# використання різних назв для змінних ключа та значення
my_dict = {
    "experience": "досвід",
    True: "правда",
    (1, 2): "кортеж",
}

for element, value in my_dict.items():
    print(f"The key is '{element}'. The value is: '{value}'")

# словник як база даних
phone_book = {
    "example1.com": {"name": "John", "phone": "123456789"},
    "example2.com": {"name": "Alice", "phone": "987654321"},
}
print(phone_book["example1.com"])
print(phone_book["example1.com"]["name"])

# 26.1 Методи типу даних словник

# clear() - очищає словник
my_dict = {
    "experience": "досвід",
    True: "правда",
    "true": "правда",
    (1, 2): "кортеж",
}
my_dict.clear()
print(my_dict)  # {}

# copy() - повертає поверхневу копію словника
my_list = ["P", "y", "t", "h", "o", "n"]
my_dict = {
    "список": my_list,
    (1, 2): "кортеж",
}
new_dict = my_dict.copy()

# 1) Модифікуємо ВМІСТ спільного списку → видно в обох
my_list.append("!")
print(my_dict["список"])  # ['P', 'y', 't', 'h', 'o', 'n', '!']
print(new_dict["список"])  # ['P', 'y', 't', 'h', 'o', 'n', '!']

# 2) Видаляємо ключ тільки з оригіналу → копія НЕ змінюється
my_dict.pop((1, 2))
print((1, 2) in my_dict)  # False
print((1, 2) in new_dict)  # True

# 3) Переприсвоюємо ключу НОВИЙ список лише в оригіналі
my_dict["список"] = ["N", "e", "w"]
print(my_dict["список"])  # ['N', 'e', 'w']
print(new_dict["список"])  # ['P', 'y', 't', 'h', 'o', 'n', '!']

# fromkeys() - створює новий словник із заданими ключами та значенням за замовчуванням
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
friends_init_score = dict.fromkeys(friends, 0)
print(friends_init_score)  # {'Alice': 0, 'Bob': 0, 'Charlie': 0, 'David': 0, 'Eve': 0}

# get() - повертає значення за ключем, якщо ключа немає - None або значення за замовчуванням
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
}

print(my_en_ua_dict.get("some key"))  # None
print(my_en_ua_dict.get("some key", "some value"))  # some value
print(my_en_ua_dict.get("knowledge", "some value"))  # знання

# items() - повертає об'єкт представлення елементів словника (ключ, значення)
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
}

print(list(my_en_ua_dict.items()))  # [('knowledge', 'знання'), ('truth', 'правда')]

for key, value in my_en_ua_dict.items():
    print(f"Key: {key}, Value: {value}")
# Key: knowledge, Value: знання
# Key: truth, Value: правда

# keys() - повертає об'єкт представлення ключів словника
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
}

print(my_en_ua_dict.keys())  # dict_keys(['knowledge', 'truth'])
print(list(my_en_ua_dict.keys()))  # ['knowledge', 'truth']

for element in my_en_ua_dict.keys():
    print(f"The key is: {element}")
# The key is: knowledge
# The key is: truth

# values() - повертає об'єкт представлення значень словника
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
}

print(my_en_ua_dict.values())  # dict_values(['знання', 'правда'])
list_of_values = list(my_en_ua_dict.values())
print(list_of_values)  # ['знання', 'правда']
print(list_of_values[0])  # знання

for element in my_en_ua_dict.values():
    print(f"The value is: {element}")

# pop() - видаляє елемент за ключем і повертає його значення
my_en_ua_dict = {
    "knowledge": "знання",
    "truth": "правда",
    "example": "приклад",
}

print(my_en_ua_dict.pop("knowledge"))  # знання
print(my_en_ua_dict)  # {'truth': 'правда', 'example': 'приклад'}
print(my_en_ua_dict.pop("knowledge", "N/A"))  # N/A (not available)
print(my_en_ua_dict.pop("knowledge"))  # KeyError: 'knowledge'

# popitem() - видаляє і повертає останній доданий елемент словника (ключ, значення)
my_en_ua_dict = {"knowledge": "знання", "truth": "правда"}

print(my_en_ua_dict.popitem())  # ('truth', 'правда')
print(my_en_ua_dict.popitem())  # ('knowledge', 'знання')
print(my_en_ua_dict.popitem())  # KeyError: 'popitem(): dictionary is empty'

# setdefault() - повертає значення за ключем, якщо ключа немає - додає ключ зі значенням за замовчуванням
my_en_ua_dict = {"knowledge": "знання", "truth": "правда"}

print(my_en_ua_dict.setdefault("knowledge", "немає перекладу"))  # знання
print(my_en_ua_dict.setdefault("wisdom", "мудрість"))  # мудрість
print(my_en_ua_dict)  # {'knowledge': 'знання', 'truth': 'правда', 'wisdom': 'мудрість'}

# update() - оновлює словник елементами з іншого словника або ітерабельного об'єкта (список кортежів)
my_en_ua_dict = {"knowledge": "знання", "truth": "правда"}

my_en_ua_dict.update({"wisdom": "мудрість", "experience": "досвід"})
print(my_en_ua_dict)  # {'knowledge': 'знання', 'truth': 'правда', 'wisdom': 'мудрість', 'experience': 'досвід'}

my_en_ua_dict.update([("intelligence", "інтелект")])
print(
    my_en_ua_dict
)  # {'knowledge': 'знання', 'truth': 'правда', 'wisdom': 'мудрість', 'experience': 'досвід', 'intelligence': 'інтелект'}

# альтернатива update() через розпаковку **
dict_a = {"knowledge": "знання", "truth": "правда"}
dict_b = {"wisdom": "мудрість", "experience": "досвід"}

merged_dict = {**dict_a, **dict_b}
print(merged_dict)  # {'knowledge': 'знання', 'truth': 'правда', 'wisdom': 'мудрість', 'experience': 'досвід'}

# якщо є однакові ключі - залишається значення з останнього словника
dict_a = {"knowledge": "знання", "truth": "правда"}
dict_b = {"truth": "істина"}

merged_dict = {**dict_a, **dict_b}
print(merged_dict)  # {'knowledge': 'знання', 'truth': 'істина'}

# 26.2 Dict comprehension

# приклад створення словника за допомогою dict comprehension
my_dict = {x: x**2 for x in range(1, 11)}
print(my_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# приклад створення словника з умовою за допомогою dict comprehension
my_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(my_dict)

# еквівалентний приклад без dict comprehension
my_dict = {}
for x in range(1, 11):
    if x % 2 == 0:
        my_dict[x] = x**2

print(my_dict)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# 26.4 Самостійна робота

# 2 cловники
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# список імен
names = ["Alice", "Bob", "Alice", "Eve", "Bob", "Alice"]
