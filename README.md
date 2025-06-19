# 🔠 Mastering Strings and ASCII in Python

This beginner-friendly project explores string manipulation and ASCII handling in Python. It demonstrates how to build core string functions like `capitalize()`, `upper()`, `lower()`, `isalpha()`, `isdigit()`, and `isalnum()` from scratch, and finally organizes them into a reusable utility module: `NLP_Library.py`.

---

## 📁 Project Structure

```text
📦 Mastering Strings and ASCII
├── Mastering Strings and ASCII.ipynb    # Main notebook demonstrating logic
├── NLP_Library.py                       # Custom string utilities module
├── Calling all funcs from lib.ipynb     # Demonstration of function imports
└── README.md                            # Project documentation
```
## ✨ Features

🔤 **Convert characters to and from ASCII**  
Using `ord()` and `chr()` functions to map characters and ASCII codes.

🔡 **Custom Implementations of:**
- `capitalize()`
- `upper()` and `lower()`
- `isalpha()`, `isdigit()`, `isalnum()`
- `title()` formatting

🧰 **Utility Module:** `NLP_Library.py`  
Reusable code organized for easy import and modular development.

✅ **Verification:**  
Compared outputs against Python’s built-in string methods to ensure accuracy.

---

## 📌 Example Usage

### ➕ Convert Character to ASCII
```python
ord('A')   # Output: 65
ord('a')   # Output: 97
```
### ➖ Convert ASCII to Character
```python
chr(65)    # Output: 'A'
chr(97)    # Output: 'a'
```
### 🔠 A-Z Generation
```python
print(''.join([chr(i) for i in range(65, 91)]))  # ABC...Z
```
### 🧪 Custom capitalize()
```python
capitalize("hello World")   # Output: "Hello world"
```
### 🧠 Custom title()
```python
title("i am learning python")  # Output: "I Am Learning Python"
```

---
## 📦 NLP_Library.py – Utility Functions
Includes the following:
- upper(text)
- lower(text)
- capitalize(text)
- title(text)
- isalpha(text)
- isdigit(text)
- isalnum(text)

All functions operate using ASCII logic (ord() and chr()) without relying on built-in string methods.

---
## ✅ Calling Functions
```python
import NLP_Library as lb

lb.capitalize("hello how are you")
# Output: 'Hello how are you'

from NLP_Library import title
title("i'm rishita")
# Output: "I'm Rishita"
```
---
## 🚀 How to Run
1. Clone the repo or download the files.
2. Run Mastering Strings and ASCII.ipynb to see all logic.
3. Use Calling all funcs from lib.ipynb to test the module-based approach.
---
## 📚 Concepts Covered
- ASCII basics with ord() and chr()
- Manual character checks for case conversion
- Writing functions that mimic Python’s string methods
- Using for loops and conditional checks for string operations

---
## 📃 License
This project is licensed under the MIT License.
---

Let me know if you'd like:
- A test suite (using `unittest`)
- A way to convert this into a Python package or PyPI uploadable module

I'll be happy to help!
