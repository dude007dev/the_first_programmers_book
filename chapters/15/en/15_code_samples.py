# 15. Блоки та відступи: як Python читає ваш код

# Що таке блок коду
favorite_language = "Python"
if favorite_language == "Python":
    print("Nice choice!")

try:
    d = int(input("Enter the deposit amount: "))
except ValueError:
    print("Please enter a valid number")

# помилка синтаксису: IndentationError: expected an indented block after 'try'
try:
d = int(input("Enter the deposit amount: "))
except ValueError:
    print("Please enter a valid number")

# 15.1 Правила відступів

# Відступ має складатися щонайменше з одного пробілу
try:
 d = int(input("Enter the deposit amount: "))
except ValueError:
    print("Please enter a valid number")

# помилка синтаксису: IndentationError: unexpected indent
try:
 d = int(input("Enter the deposit amount: "))
     print(f"Deposit amount: {d}")  # IndentationError
except ValueError:
    print("Please enter a valid number")