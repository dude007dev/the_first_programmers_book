# Chapter 27. Song Words Counter

This chapter contains examples from the book **"The First Programmer's Book"**.  
We create the **"Song Words Counter"** program — an application that analyzes song text and determines the most frequently used word.  
This chapter demonstrates practical usage of dictionaries, loops, conditional statements, the `collections` and `re` modules.

---

## Folder Structure

- [**`27_code_samples.py`**](./27_code_samples.py) — all code examples from the book sections collected in one file.
  ⚠️ Some examples are fragments with context and are used only to demonstrate individual parts of the program.
- [**`27_song_words_counter_program.py`**](./27_song_words_counter_program.py) — final, working code of the program.

---

## Contents of Examples

- **27. Song Words Counter** → step-by-step creation of a program for counting words in song text "Nich yaka misyachna".
- **27.1 Other Ways to Solve the Problem** → alternative solution options using:
  - **`defaultdict`** — automatic creation of initial values in a dictionary;
  - **`Counter`** — "counter" data type for simplifying counts;
  - **`sorted()`** — sorting a dictionary by values;
  - **`re.findall()`** — using regular expressions to extract words from text.
- **27.3 Self-Check Work** → exercises for improving the program.

---

## How to Run Examples

This chapter contains both short examples and complete programs.  
Use Python in the terminal (or in an online interpreter) to run them.  

Running a program:
```bash
python3 27_song_words_counter_program.py
```

## Useful Links

- [`collections.defaultdict` — Python Docs](https://docs.python.org/3/library/collections.html#collections.defaultdict)
- [`collections.Counter` — Python Docs](https://docs.python.org/3/library/collections.html#collections.Counter)
- [`sorted()` — Built-in Functions (Python Docs)](https://docs.python.org/3/library/functions.html#sorted)
- [`re.findall()` — Regular Expressions (Python Docs)](https://docs.python.org/3/library/re.html#re.findall)
- [`string` methods — Python Docs](https://docs.python.org/3/library/stdtypes.html#string-methods)

**Navigation**

⬅️ [Chapter 26](../../26/en) | ➡️ [Chapter 28](../../28/en)
