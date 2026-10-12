# 14. Блок if...else...

# 14.1 Як працює блок if...else... у Python

# Приклад 1
forecast = ["rain", "sun"]

if "storm" in forecast:
    print("Stay at home!")
elif "rain" in forecast and "sun" in forecast:
    print("Take an umbrella and sunglasses.")
elif "rain" in forecast:
    print("Take a jacket and an umbrella.")
elif "sun" in forecast:
    print("Take sunglasses.")
elif "clouds" in forecast:
    print("Take a jacket.")
else:
    print("No special recommendations.")

# 14.2 Блок if...else... в програмі для оцінювання за шкалою A–F

value = input("Enter the percentage of correct answers of the test: ")
value = int(value)
if value >= 90:
    grade = "A"
elif value >= 80 and value < 90:
    grade = "B"
elif value >= 70 and value < 80:
    grade = "C"
elif value >= 60 and value < 70:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

