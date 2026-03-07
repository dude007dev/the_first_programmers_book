# 11. Numeric Data Types

# Integers (type int)
age = 20
temperature = -5

# Floats (type float)
height = 1.65
pi = 3.14159

# Complex numbers (type complex)
x = 100 + 3j

# 11.3 Arithmetic Operators

# +, addition
print(5 + 3)  # 8
print(2.1 + 7)  # 9.1
print(-1 + 2)  # 1

x = -1.0
y = 1
print(x + y)  # 0.0

# -, subtraction
print(5 - 3)  # 2
print(2.1 - 7)  # -4.9
print(-1 - 2)  # -3

x = -1.0
y = 1
print(x - y)  # -2.0

# *, multiplication
print(5 * 3)  # 15
print(2.1 * 7)  # 14.700000000000001
print(-1 * 2)  # -2

x = -1.0
y = 1
z = x * y
print(z)  # -1.0

# /, division
print(5 / 3)  # 1.6666666666666667
print(2.1 / 7)  # 0.3
print(-1 / 2)  # -0.5

x = -1.0
y = 1
z = x / y
print(z)  # -1.0

# %, modulus (remainder of division)
print(7 % 3)  # 1
print(8 % 3)  # 2
print(4 % 2)  # 0

# **, exponentiation
print(2**3)  # 8
print(7**2)  # 49
print(3.1**2.2)  # 6.820000000000001

# //, floor division
print(3 // 2)  # 1
print(49 // 10)  # 4
print(2.7 // 3)  # 0.0

# 11.4 Floating Point Arithmetic: Problems and Limitations
print(5 / 3)  # 1.6666666666666667
print(2.1 * 7)  # 14.700000000000001

# rounding a float
value = 2.1 * 7
print(round(value, 3))  # 14.7
# or without variable:
print(round(2.1 * 7, 3))  # 14.7

# converting float to integer
print((int(2.1 * 10) * 7) / 10)  # 14.7
# or step by step:
int_value = 2.1 * 10
print(int_value * 7 / 10)  # 14.7

print(7 / 3)  # 2 - result rounded down!
print(7.0 / 3)  # 2.3333333333333335
