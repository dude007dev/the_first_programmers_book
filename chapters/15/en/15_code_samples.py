# 15. Blocks and Indentation: How Python Reads Your Code

# What is a code block
favorite_language = "Python"
if favorite_language == "Python":
    print("Nice choice!")

try:
    d = int(input("Enter the deposit amount: "))
except ValueError:
    print("Please enter a valid number")

# syntax error: IndentationError: expected an indented block after 'try'
try:
d = int(input("Enter the deposit amount: "))
except ValueError:
    print("Please enter a valid number")

# 15.1 Indentation Rules

# Indentation must consist of at least one space
try:
 d = int(input("Enter the deposit amount: "))
except ValueError:
    print("Please enter a valid number")

# syntax error: IndentationError: unexpected indent
try:
 d = int(input("Enter the deposit amount: "))
     print(f"Deposit amount: {d}")  # IndentationError
except ValueError:
    print("Please enter a valid number")