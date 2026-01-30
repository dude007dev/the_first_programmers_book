# Chapter 29. Word Game: Hangman Using Functions

This chapter contains examples from the book **"The First Programmer's Book"**.  
We rewrite the **"Hangman"** game using functions — breaking the code into logical parts to make it clearer, more flexible, and closer to real software projects.

---

## Folder Structure

- [**`29_code_samples.py`**](./29_code_samples.py) — all code examples from the book sections collected in one file.
  ⚠️ Some examples are fragments with context and are used only to demonstrate individual parts of the program.
- [**`29_hangman_game.py`**](./29_hangman_game.py) — final, working code of the **Hangman** game.

---

## Contents of Examples

- **29. Word Game: Hangman Using Functions** → main function template `game_hangman()`.
- **29.1 Function for Getting Hangman Drawing** → the `get_hangman_drawing(stage_number)` function that returns the drawing for the current game stage. The drawing is stored as a **tuple of strings**.
- **29.2 Updated Game Initialization** → updating the `game_hangman()` function after separating the drawing into its own function; using the `current_attempt` variable instead of negative indices.
- **29.3 Welcome Message Function** → the `print_welcome_message(num_attempts, word)` function for displaying greeting text.  
- **29.4 Input Validation Function** → the `is_guess_valid(input_value, guessed_values)` function that checks the correctness of the player's input.
- **29.5 Function for Displaying Current Word State** → the `display_word_progress(word, guessed_values)` function to show already guessed letters.
- **29.6 Final Form of Main Function** → assembled game logic: user input, validation, state update, drawing display, and game completion.
- **29.8 Self-Check Work** → code fragments from self-check assignments.

---

## How to Run Examples

This chapter contains both short examples and complete programs.  
Use Python in the terminal (or in an online interpreter) to run them.  

Running a program:
```bash
python3 29_hangman_game.py
```

## Useful Links

- [PEP 8 — Function and Variable Names](https://peps.python.org/pep-0008/#function-and-variable-names)
- [Functions — Python Tutorial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Docstring Conventions — PEP 257](https://peps.python.org/pep-0257/)
- [`tuple` — Python Docs](https://docs.python.org/3/library/stdtypes.html#tuple)
- [`set` — Python Docs](https://docs.python.org/3/library/stdtypes.html#set)

**Navigation**

⬅️ [Chapter 28](../../28/en) | ➡️ [Chapter 30](../../30/en)
