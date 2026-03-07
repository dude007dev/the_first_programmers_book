# Chapter 28. Functions

This chapter contains examples from the book **"The First Programmer's Book"**.  
We cover **functions in Python** in detail — how to create them, pass parameters, return values, document them, avoid common mistakes, and write clearer, more structured code.

---

## Folder Structure

- [**`28_code_samples.py`**](./28_code_samples.py) — all code snippets from the book sections collected in one file.
  ⚠️ Some examples intentionally demonstrate errors to show features of function creation and calling in Python.

---

## Contents of Examples

- **28.1 Function Creation and Calling** → basic syntax: the `def` keyword, function calls, examples without parameters.
- **28.2 Function Creation and Calling with Parameters** → functions with one and multiple parameters.
- **28.3 Function Name** → naming rules according to [PEP 8](https://peps.python.org/pep-0008/#function-and-variable-names).
- **28.4–28.7** → positional and keyword arguments, their order and combination.  
- **28.8 Positional-Only Arguments (/)** → functions that can only be called with positional arguments.
- **28.9 Keyword-Only Arguments (*)** → functions that accept only keyword arguments.
- **28.10 Combined Parameters: Positional-Only (/) and Keyword-Only (*) Arguments** → combining both approaches.
- **28.11 Passing a Variable as a Function Parameter** → local and external variables, the principle of "what happens in a function stays in a function".
- **28.12 Default Parameter Value** → creating parameters with default values and the rule "all parameters after default ones must also have defaults".
- **28.13 Returning Function Result** → examples of returning values, multiple `return` statements in a function, and `return None`.
- **28.14 Mutable Data Type in Function Parameter** → passing lists and dictionaries as arguments, the impact of mutability on the result.
  ⚠️ Common mistake with mutable types as default parameters (`friends=[]`) and the correct approach using `None`.  
- **28.15 Using pass** → creating "stubs" and empty functions.  
- **28.16 Nested Functions** → functions inside functions, scope and access to external variables.
- **28.17 Function Documentation** → documentation formatting in Google style, using IDE hints.
- **28.18 `*args`, `**kwargs`** → arbitrary number of positional and keyword arguments, their practical usage in functions.

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
