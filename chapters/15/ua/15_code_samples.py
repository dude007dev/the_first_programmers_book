# 15. Блоки та відступи: як Python читає ваш код

# Що таке блок коду
favorite_language = "Python"
if favorite_language == "Python":
    print("Nice choice!")

favorite_language = "Python"
if favorite_language == "Python":
    print("Nice choice!")
else:
    print("You should try Python!")

# помилка синтаксису: IndentationError: expected an indented block after 'if' statement
favorite_language = "Python"
if favorite_language == "Python":
print("Nice choice!")
else:
    print("You should try Python!")

# 15.1 Правила відступів

# Відступ має складатися щонайменше з одного пробілу
favorite_language = "Python"
if favorite_language == "Python":
 print("Nice choice!")
else:
    print("You should try Python!")

# помилка синтаксису: IndentationError: unexpected indent
favorite_language = "Python"
if favorite_language == "Python":
 print("Nice choice!")
    print("Python is a great programming language.")
else:
    print("You should try Python!")

# 15.2 Вкладені блоки

age = 20
has_ticket = True

if age >= 18:
    print("Age is OK")

    if has_ticket:
        print("You can enter")