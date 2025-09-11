# Розділ 27. Song Words Counter

Цей розділ містить приклади з книги **"Перша книга програміста"**.  
У ньому ми створюємо програму **“Song Words Counter”** — застосунок, який аналізує текст пісні та визначає найчастіше вживане слово.  
Розділ демонструє практичне використання словників, циклів, умовних операторів, модулів `collections` та `re`.

---

## Структура папки

- [**`27_code_samples.py`**](./27_code_samples.py) — усі приклади коду з підрозділів книги, зібрані в одному файлі.
  ⚠️ Деякі приклади є фрагментами з контексту та використовуються лише для демонстрації окремих частин програми.
- [**`27_song_words_counter_program.py`**](./27_song_words_counter_program.py) — фінальний, робочий код програми.

---

## Зміст прикладів

- **27. Song Words Counter** → покрокове створення програми для підрахунку слів у тексті пісні “Ніч яка місячна”.
- **27.1 Інші способи вирішення задачі** → альтернативні варіанти розв’язку з використанням:
  - **`defaultdict`** — автоматичне створення початкових значень у словнику;
  - **`Counter`** — тип даних “лічильник” для спрощення підрахунків;
  - **`sorted()`** — сортування словника за значеннями;
  - **`re.findall()`** — застосування регулярних виразів для виділення слів із тексту.
- **27.3 Самостійна робота** → вправи для вдосконалення програми.

---

## Як запускати приклади

У цьому розділі наведені як короткі приклади, так і готові програми.  
Для запуску використовуйте Python у терміналі (або онлайн-інтерпретатор).  

Запуск окремої програми:
```bash
python3 27_song_words_counter_program.py
```

## Корисні посилання

- [`collections.defaultdict` — Python Docs](https://docs.python.org/3/library/collections.html#collections.defaultdict)
- [`collections.Counter` — Python Docs](https://docs.python.org/3/library/collections.html#collections.Counter)
- [`sorted()` — Built-in Functions (Python Docs)](https://docs.python.org/3/library/functions.html#sorted)
- [`re.findall()` — Regular Expressions (Python Docs)](https://docs.python.org/3/library/re.html#re.findall)
- [`string` methods — Python Docs](https://docs.python.org/3/library/stdtypes.html#string-methods)

**Навігація**

⬅️ [Розділ 26](../../26/ua) | ➡️ [Розділ 28](../../28/ua)
