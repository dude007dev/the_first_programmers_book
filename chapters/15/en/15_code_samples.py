# 15. Blocks and Indentation: How Python Reads Your Code

# What is a code block
favorite_language = "Python"
if favorite_language == "Python":
    print("Nice choice!")

favorite_language = "Python"
if favorite_language == "Python":
    print("Nice choice!")
else:
    print("You should try Python!")

# syntax error: IndentationError: expected an indented block after 'if' statement
favorite_language = "Python"
if favorite_language == "Python":
print("Nice choice!")
else:
    print("You should try Python!")

# 15.1 Indentation Rules

# Indentation must consist of at least one space
favorite_language = "Python"
if favorite_language == "Python":
 print("Nice choice!")
else:
    print("You should try Python!")

# syntax error: IndentationError: unexpected indent
favorite_language = "Python"
if favorite_language == "Python":
 print("Nice choice!")
    print("Python is a great programming language.")
else:
    print("You should try Python!")

# 15.2 Nested blocks

age = 20
has_ticket = True

if age >= 18:
    print("Age is OK")

    if has_ticket:
        print("You can enter")