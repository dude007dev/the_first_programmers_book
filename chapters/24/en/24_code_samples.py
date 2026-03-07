# 24. Set Data Type

# Creating a set
my_set = {"apple", "banana", "strawberry"}
print(my_set)  # {'apple', 'banana', 'strawberry'}

# creating and adding elements to a set
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(5)
print(my_set)  # {1, 2, 5}

# creating a dictionary, not a set
my_set = {}
print(type(my_set))  # <class 'dict'>

# set does not preserve order of elements and does not allow duplicates
my_set = {"apple", "banana", "kiwi", "apple", "banana"}
print(my_set)  # {'banana', 'kiwi', 'apple'}

# set elements must be hashable (immutable)
my_set = {"apple", ["banana", "kiwi"], "apple", "banana"}
print(my_set)  # TypeError: unhashable type: 'list'

# example of set with different data types
my_set = {"apple", 1, True, False, "apple", True, ("a", "b"), 5.33}
print(my_set)  # {False, 1, 5.33, 'apple', ('a', 'b')}

# checking if element exists in set (fast operation, O(1))
my_set = {"apple", "banana", "kiwi"}
print("kiwi" in my_set)  # True

# 24.1 Set Comprehension

# creating set of squares of numbers from 0 to 5
squares = {x**2 for x in range(6)}
print(squares)  # {0, 1, 4, 9, 16, 25}

# even squares from 0 to 10
even_squares = {x**2 for x in range(11) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64, 100}

# 24.2 Set Data Type Methods

# add() - adding element
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

# remove() - removing element (raises KeyError if element doesn't exist)
s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}

s.remove(2)  # KeyError: 2 not in {1, 3}

# discard() - removing element (does not raise error if element doesn't exist)
s = {1, 2, 3}
s.discard(2)
print(s)  # {1, 3}

s.discard(2)
print(s)  # {1, 3}

# pop() - removing and returning random element
s = {1, 2, 3}
elem = s.pop()
print(elem)  # One of the set elements, for example 1
print(s)  # Two elements remained, for example {2, 3}

# clear() - clearing the set
s = {1, 2, 3}
s.clear()
print(s)  # set()

# union() - union of sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)

print(s1)  # {1, 2, 3}
print(s2)  # {3, 4, 5}
print(s3)  # {1, 2, 3, 4, 5}

s4 = s1 | s2
print(s4)  # {1, 2, 3, 4, 5}

# update() - adding elements from another set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.update(s2)
print(s1)  # {1, 2, 3, 4, 5}

s3 = {6, 7, 8}
s1 |= s3
print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8}

# intersection() - intersection of sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 2, 5}
s4 = s1.intersection(s2, s3)
print(s4)  # {2, 3}

s5 = s1 & s2 & s3
print(s5)  # {2, 3}

# intersection_update() - updating set with intersection from others
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 2, 5}
s1.intersection_update(s2, s3)
print(s1)  # {2, 3}

s4 = {5, 6, 7}
s4 &= s3
print(s4)  # {5}

# difference() - difference of sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.difference(s2)
print(s3)  # {1}

s3 = {3, 4, 5}
s4 = {2, 3, 4}
s5 = s3 - s4
print(s5)  # {5}

# difference_update() - updating set with difference from another
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.difference_update(s2)
print(s1)  # {1}

s3 = {3, 4, 5}
s4 = {2, 3, 4}
s3 -= s4
print(s3)  # {5}

# symmetric_difference() - symmetric difference of sets
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

# symmetric_difference_update() - updating set with symmetric difference from another
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

# issubset() - checking subset
s1 = {1, 2}
s2 = {1, 2, 3}

print(s1.issubset(s2))  # True
print(s1 < s2)  # True
print(s1 <= s2)  # True

# issuperset() - checking superset
s1 = {1, 2, 3}
s2 = {1, 2}

print(s1.issuperset(s2))  # True
print(s1 > s2)  # True
print(s1 >= s2)  # True

# isdisjoint() - checking for no common elements
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))  # True

# 24.3 Practical use of sets

my_list = [1, 2, 1, 3, 4, 5, 3, 5]
my_set = set(my_list)

print(my_set)  # {1, 2, 3, 4, 5}
print(5 in my_set)  # True, check is performed in O(1)

for item in my_set:
    # do something with item
    pass
