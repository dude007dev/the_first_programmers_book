# 14.8 Програма: розрахунок депозиту з використанням try..except...

try:
    d = int(input("Enter the deposit amount: "))
except ValueError:
    print("Please enter a valid number")
    d = int(input("Enter the deposit amount: "))

try:
    i = float(input("Enter the interest rate (example: 1.28): "))
except ValueError:
    print("Please enter a valid float number")
    i = float(input("Enter the interest rate (example: 1.28): "))

try:
    n = int(input("Enter the number of years: "))
except ValueError:
    print("Please enter a valid number")
    n = int(input("Enter the number of years: "))

i /= 100
compound_rate = (1 + i) ** n - 1
compound_interest = d * compound_rate

result = round(d + compound_interest, 2)
print(result)
