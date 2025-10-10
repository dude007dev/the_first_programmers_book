# Розділ 20. Гра “Вгадай слово”

Цей розділ містить приклади з книги **"Перша книга програміста"**.  
У ньому ми створюємо повну версію гри “Вгадай слово” — підсумковий проєкт, що об’єднує знання про змінні, типи даних, цикли, умовні оператори та обробку введення користувача.

---

## Структура папки

- [**`20_guess_the_word_game.py`**](./20_guess_the_word_game.py) — повний, робочий код гри “Вгадай слово”.  

---

## Зміст прикладів

- **Вибір слова для гри** → створення змінної `word` та базових параметрів (`attempts`, `guessed_letters`).  
- **Цикл гри** → реалізація логіки повторних спроб за допомогою `while`.  
- **Перевірка введення** → перевірка коректності введеної літери, використання `continue`.  
- **Обробка вгаданих і невгаданих літер** → зменшення кількості спроб, відображення прогресу.  
- **Перевірка завершення гри** → перевірка, чи вгадано всі літери, або закінчились спроби.

---

## Як запускати програму

1. Перейдіть у відповідну директорію:
   ```bash
   cd chapters/20/ua
   ```

2. Запустіть програму у терміналі:
    ```bash
    python3 20_guess_the_word_game.py
    ```

## Корисні посилання

- [`while` statement (Python docs)](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [`break` and `continue` statements (Python docs)](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements)
- [`input()` — reading user input (Python docs)](https://docs.python.org/3/library/functions.html#input)
- [`f-string` — formatted string literals (Python docs)](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

**Навігація**

⬅️ [Розділ 19](../../19/ua) | ➡️ [Розділ 21](../../21/ua)
