# Chapter 28. Functions

This chapter contains examples from the book **"The First Programmer's Book"**.  
We cover **functions in Python** in detail — how to create them, pass parameters, return values, document them, avoid common mistakes, and write clearer, more structured code.

---

## Folder Structure

- [**`28_code_samples.py`**](./28_code_samples.py) — all code snippets from the book sections collected in one file.
  ⚠️ Some examples intentionally demonstrate errors to show features of function creation and calling in Python.

---

## Contents of Examples

- **28.1 Function Creation and Calling** → basic syntax: the `def` keyword, defining and calling functions without parameters.
- **28.2 Function Creation and Calling with Parameters** → defining functions with parameters, passing arguments, and calling the same function with different values.
- **28.3 Function Names** → naming conventions according to [PEP 8](https://peps.python.org/pep-0008/#function-and-variable-names), using lowercase letters, underscores, and numbers in function names.
- **28.4 Functions with multiple parameters** → defining functions with multiple parameters and passing the corresponding arguments.
- **28.5 Number of arguments** → matching arguments to required parameters and understanding errors caused by missing arguments (`TypeError`).
- **28.6 Positional arguments** → passing arguments by position and understanding why their order matters.
- **28.7 Keyword arguments** → passing arguments by parameter name, improving readability, and combining positional and keyword arguments correctly.
- **28.8 Passing a variable as a function argument** → passing variables to functions, understanding local and outer variables, variable scope, and why reassigning a parameter does not change the original variable.
- **28.9 Default parameter values** → defining parameters with default values, overriding them with arguments, and following the rule that regular parameters without defaults must come before those with defaults.
- **28.10 Returning a function result** → returning values using `return`, storing returned results in variables, using multiple `return` statements, and understanding `return None` and implicit returns.
- **28.11 Mutable data types as function arguments** → passing lists and dictionaries as arguments, understanding mutable and immutable objects, and distinguishing between modifying an object and reassigning a parameter.  
  ⚠️ Common mistake with mutable default arguments (`friends=[]`) and the correct approach using `None`.
- **28.12 Using pass** → creating placeholder functions with `pass` and understanding the difference between `pass` and `return`.
- **28.13 Calling functions inside other functions** → calling one function from another, separating program logic into smaller tasks, and using `main()` to coordinate program execution.
- **28.14 Function Documentation** → writing basic docstrings using triple quotes, accessing documentation through `__doc__`, and understanding when function documentation is useful.
- **28.18 For the curious: `*args`, `**kwargs`** → accepting a variable number of positional and keyword arguments, collecting them into tuples and dictionaries, and unpacking dictionaries into function calls.
- **28.19 For the curious: positional-only parameters (`/`)** → defining parameters that accept arguments only by position using the `/` separator.
- **28.20 For the curious: keyword-only parameters (`*`)** → defining parameters that must be passed by keyword using the `*` separator and calling functions with unpacked dictionaries.
- **28.21 For the curious: combining positional-only (`/`) and keyword-only (`*`) parameters** → combining positional-only, regular, and keyword-only parameters in a single function definition.
- **28.22 For the curious: nested functions** → defining functions inside other functions, calling nested functions, and accessing variables from the enclosing function's scope.
- **28.23 For the curious: Google style for function documentation** → writing structured docstrings with `Args:` and `Returns:` sections, documenting parameters and return values, and understanding how IDEs use docstrings.

---

## How to Run Examples

This chapter contains only short examples, without complete programs.  
To test them:  

1. Copy the required code block.  
2. Paste it into a file (for example, `example.py`) or in an online interpreter.  
3. Run the file in the terminal:  
    ```bash
    python3 example.py
    ```
    or run the program in an online interpreter.

⚠️ Some examples intentionally contain errors (`TypeError`, `SyntaxError`, `NameError`) to demonstrate the function mechanism in Python.

## Useful Links

- [PEP 8 — Function and Variable Names](https://peps.python.org/pep-0008/#function-and-variable-names)
- [Functions — Python Tutorial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Docstring Conventions — PEP 257](https://peps.python.org/pep-0257/)

**Navigation**

⬅️ [Chapter 27](../../27/en) | ➡️ [Chapter 29](../../29/en)
