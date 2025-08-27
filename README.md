
# DynaCalc – A Simple Arithmetic Interpreter

DynaCalc is a small **learning project** written in Python that demonstrates how interpreters work at a very basic level.
It is **not a full-fledged calculator or interpreter**, but instead a **study project** built for practice and understanding of concepts like tokenization, parsing, and interpretation.

---

## ✨ Features

* Tokenizes input expressions (`INT`, `+`, `-`, `*`, `/`).
* Supports simple arithmetic:

  * Addition (`+`)
  * Subtraction (`-`)
  * Multiplication (`*`)
  * Division (`/`)
* Interactive prompt (`DynaCalc >>`) for evaluating expressions.

---

## ⚠️ Limitations

* Only supports **single-digit integers** (`0–9`).
* Only handles **two operands at a time** (e.g., `2+3`, `7*8`).
* No parentheses, precedence handling, or error recovery.
* Very minimal and intended purely for **study and experimentation**.

---

## 🛠️ Example Usage

Run the interpreter:

```bash
python3 dynacalc.py
```

Then, try expressions:

```
DynaCalc >> 2+3
5  

DynaCalc >> 7-4
3  

DynaCalc >> 8*2
16  

DynaCalc >> 9/3
3.0
```

---

## 📚 Learning Goals

This project was made to:

* Practice **tokenization** (breaking input into tokens).
* Understand **parsing** and how an interpreter processes input.
* Learn the basics of building a simple REPL (Read–Eval–Print Loop).

---

## 🚧 Disclaimer

This is **not a production-grade calculator or parser**.
It is a **learning project** for educational purposes and experimentation.
