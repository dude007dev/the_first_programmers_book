# 24. Тип даних множина (set)

# створення множини
my_set = {"apple", "banana", "strawberry"}
print(my_set)  # {'apple', 'banana', 'strawberry'}

# створення та додавання елементів до множини
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(5)
print(my_set)  # {1, 2, 5}

# створення словника, а не множини
my_set = {}
print(type(my_set))  # <class 'dict'>

# множина не зберігає порядок елементів і не дозволяє дублікати
my_set = {"apple", "banana", "kiwi", "apple", "banana"}
print(my_set)  # {'banana', 'kiwi', 'apple'}

# елементи множини мають бути хешованими (не змінюваними)
my_set = {"apple", ["banana", "kiwi"], "apple", "banana"}
print(my_set)  # TypeError: unhashable type: 'list'

# приклад множини з різними типами даних
my_set = {"apple", 1, True, False, "apple", True, ("a", "b"), 5.33}
print(my_set)  # {False, 1, 5.33, 'apple', ('a', 'b')}

# перевірка наявності елемента в множині (швидка операція, O(1))
my_set = {"apple", "banana", "kiwi"}
print("kiwi" in my_set)  # True

# 24.1 Comprehension множин (set comprehension)

# створення множини квадратів чисел від 0 до 5
squares = {x**2 for x in range(6)}
print(squares)  # {0, 1, 4, 9, 16, 25}

# парні квадрати від 0 до 10
even_squares = {x**2 for x in range(11) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64, 100}

# 24.2 Методи типу даних множина (set)

# add() - додавання елемента
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

# remove() - видалення елемента (викидає KeyError, якщо елемента немає)
s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}

s.remove(2)  # KeyError: 2 not in {1, 3}

# discard() - видалення елемента (не викидає помилку, якщо елемента немає)
s = {1, 2, 3}
s.discard(2)
print(s)  # {1, 3}

s.discard(2)
print(s)  # {1, 3}

# pop() - видалення і повернення випадкового елемента
s = {1, 2, 3}
elem = s.pop()
print(elem)  # Один з елементів множини, наприклад 1
print(s)  # Залишилися два елементи, наприклад {2, 3}

# clear() - очищення множини
s = {1, 2, 3}
s.clear()
print(s)  # set()

# union() - об'єднання множин
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)

print(s1)  # {1, 2, 3}
print(s2)  # {3, 4, 5}
print(s3)  # {1, 2, 3, 4, 5}

s4 = s1 | s2
print(s4)  # {1, 2, 3, 4, 5}

# update() - додавання елементів з іншої множини
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.update(s2)
print(s1)  # {1, 2, 3, 4, 5}

s3 = {6, 7, 8}
s1 |= s3
print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection() - перетин множин
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 2, 5}
s4 = s1.intersection(s2, s3)
print(s4)  # {2, 3}

s5 = s1 & s2 & s3
print(s5)  # {2, 3}

# intersection_update() - оновлення множини перетином з іншими
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 2, 5}
s1.intersection_update(s2, s3)
print(s1)  # {2, 3}

s4 = {5, 6, 7}
s4 &= s3
print(s4)  # {5}

# difference() - різниця множин
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.difference(s2)
print(s3)  # {1}

s3 = {3, 4, 5}
s4 = {2, 3, 4}
s5 = s3 - s4
print(s5)  # {5}

# difference_update() - оновлення множини різницею з іншою
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.difference_update(s2)
print(s1)  # {1}

s3 = {3, 4, 5}
s4 = {2, 3, 4}
s3 -= s4
print(s3)  # {5}

# symmetric_difference() - симетрична різниця множин
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)  # {'banana', 'microsoft', 'cherry', 'google'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x ^ y
print(z)  # {'banana', 'microsoft', 'cherry', 'google'}

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.symmetric_difference(s2)
print(s3)  # {1, 4}

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 ^ s2
print(s3)  # {1, 4}

# symmetric_difference_update() - оновлення множини симетричною різницею з іншою
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)  # {'banana', 'microsoft', 'cherry', 'google'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x ^= y
print(x)  # {'banana', 'microsoft', 'cherry', 'google'}

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.symmetric_difference_update(s2)
print(s1)  # {1, 4}

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 ^= s2
print(s1)  # {1, 4}

# issubset() - перевірка підмножини
s1 = {1, 2}
s2 = {1, 2, 3}

print(s1.issubset(s2))  # True
print(s1 < s2)  # True
print(s1 <= s2)  # True

# issuperset() - перевірка надмножини
s1 = {1, 2, 3}
s2 = {1, 2}

print(s1.issuperset(s2))  # True
print(s1 > s2)  # True
print(s1 >= s2)  # True

# isdisjoint() - перевірка на відсутність спільних елементів
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))  # True

# 24.3 Практичне використання множин

my_list = [1, 2, 1, 3, 4, 5, 3, 5]
my_set = set(my_list)

print(my_set)  # {1, 2, 3, 4, 5}
print(5 in my_set)  # True, перевірка виконується за O(1)

for item in my_set:
    # do something with item
    pass
