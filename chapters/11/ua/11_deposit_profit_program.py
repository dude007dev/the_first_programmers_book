# 11.5 Програма для розрахунку прибутку за депозитом

d = 1500
i = 1.35
n = 3

interest_rate = i / 100
compound_interest = d * ((1 + interest_rate) ** n - 1)

total_amount = d + compound_interest
print(total_amount)  # 1561.5738155625004

total_amount = round(total_amount, 2)
print(total_amount)  # 1561.57
