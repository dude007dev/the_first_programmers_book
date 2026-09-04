# Chapter 5. Terminal and Console

This chapter contains examples from the book **"The First Programmer's Book"**.  
We get acquainted with the terminal and the interactive Python console.

⚠️ All examples in this chapter are included directly in the `README.md` because they are intended to be run in a terminal or console, not in regular `.py` files.

---

## Folder structure

- [**`README.md`**](./README.md) — contains all snippets from the chapter sections.  
  ⚠️ The examples are meant to be run in a terminal or an interactive console.

---

## Examples contents

- **5.1 The difference between a terminal and a console**
  ```bash
  pip install pandas
  python3 example.py
  ```

- **5.3 Running a Python Program in the Terminal**
  
  Program in `hello.py` file:
  ```python
  name = input("Enter your name: ")
  print(f"Hello, {name}!")
  ```

  Running program:
  ```bash
  python3 hello.py
  python hello.py
  py hello.py
  ```

- **5.4 The Interactive Python Console**

  Open the interactive Python console:
  ```bash
  python3
  python
  py
  ```

- **5.6 Independent Practice**

  Run the following program in your editor:
  ```python
  print("My first program is running!")
  ```

  Run the program, enter your name, and then change the greeting:
  ```python
  name = input("What is your name? ")
  print(f"Hello, {name}!")
  ```

- **5.8 The `python`, `python3`, and `py` Commands**
  
  Check the installed Python version:
  ```bash
  python3 --version
  python --version
  py --version
  ```
---

## How to run the examples

Since this chapter is about the terminal, to test the examples you just need to run a Python program from a terminal:
```bash
python3 4_the_first_program.py
```

## Useful links

- [Official Python Website](https://python.org/)

**Navigation**

⬅️ [Chapter 4](../../04/en) | ➡️ [Chapter 6](../../06/en)
