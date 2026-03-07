# 12. Conversion of Basic Data Types

# Examples of conversions
# to see the result on the screen - use print()
int(5.0)  # 5
float(4)  # 4.0
bool(1)  # True
bool(0)  # False
bool(None)  # False
str(5)  # "5"
str(True)  # "True"
float("5.5")  # 5.5
float("5")  # 5.0

x = {1, 1, 2, 3, 4, 5, 5}  # set {1, 2, 3, 4, 5}
y = list(x)  # [1, 2, 3, 4, 5]

# more examples
int(5.95)  # 5

float(4)  # 4.0

bool(1)  # True
bool(0)  # False
bool(None)  # False
bool("")  # False
bool("example")  # True

str(5)  # "5"
str(True)  # "True"

float("5.5")  # 5.5
float("5")  # 5.0
int("5")  # 5

x = {1, 1, 2, 3, 4, 5, 5}  # set {1, 2, 3, 4, 5}
y = list(x)  # [1, 2, 3, 4, 5]

# 12.1 Conversion to Numeric Data Type

d = int(input("Enter the deposit amount: "))
i = float(input("Enter the interest rate (example: 1.28): "))
n = int(input("Enter the number of years: "))

i /= 100
compound_rate = (1 + i) ** n - 1
compound_interest = d * compound_rate

result = round(d + compound_interest, 2)
print(result)

# example of error
int("A1")  # ValueError: invalid literal for int() with base 10: 'A1'
