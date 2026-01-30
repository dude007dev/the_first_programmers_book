# Chapter 25. Word Game: Hangman

This chapter contains examples from the book **"The First Programmer's Book"**.  
We create the final version of the **"Hangman"** game — an expanded "Guess the Word" game that combines all topics covered so far: loops, conditional statements, sets, tuples, random number generation, and user input handling.

---

## Folder Structure

- [**`25_code_samples.py`**](./25_code_samples.py) — all code examples from the book sections collected in one file.
  ⚠️ Some examples are fragments with context and are used only to demonstrate individual parts of the game.
- [**`25_word_game_hangman.py`**](./25_word_game_hangman.py) — final, working code of the "Hangman" game.

---

## Contents of Examples

- **25. Word Game: Hangman** → overview and comparison with the previous "Guess the Word" game.
- **25.1 Hangman Drawing** → creating a graphical representation of the game as a tuple (tuple) with 7 stages.
- **25.2 Choosing a Word for the Game** → using the `random` module and `choice()` method to randomly select a word.
- **25.3 Recording Entered Values** → using the `set` data type to store unique entered values (letters or words).
- **25.4 Updated Way of Checking Game End** → applying **list comprehension** and the **`all()`** function to check if a word has been fully guessed.
- **25.7 Self-Check Work** → exercises for expanding game functionality: changing word set, number of stages, using generator expressions, etc.

---

## How to Run Examples

This chapter contains both short examples and complete programs.  
Use Python in the terminal (or in an online interpreter) to run them.  

Running a program:
```bash
python3 25_word_game_hangman.py
```

## Useful Links

- [`random` — Generate pseudo-random numbers (Python docs)](https://docs.python.org/3/library/random.html)
- [`all()` — Built-in Functions (Python docs)](https://docs.python.org/3/library/functions.html#all)
- [`f-string` — Formatted string literals (Python docs)](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

**Navigation**

⬅️ [Chapter 24](../../24/en) | ➡️ [Chapter 26](../../26/en)
