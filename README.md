# 🔐 Password Generator

A simple Python script to generate secure random passwords with customizable character types.

---

## ⚡ Features

* Choose password length
* Choose character types:

  * `u` = Uppercase (A-Z)
  * `l` = Lowercase (a-z)
  * `d` = Digits (0-9)
  * `s` = Symbols (punctuation)
* Ensures at least one character from each selected type
* Automatically shuffles characters for randomness

---

## 🛠️ Installation

Clone this repository:

```bash
git clone https://github.com/rifqiaz06/password-generator.git
cd password-generator
```

Make sure you have **Python 3.6+** installed.

---

## 🚀 Usage

Run the script with:

```bash
python password_generator.py --length 12 --chartype ulds
```

### Arguments

* `--length` : Password length (minimum 4)
* `--chartype` : Character types (combination of `u`, `l`, `d`, `s`)

---

### Examples

1. Length 16
```bash
python password_generator.py --length 16 --chartype ul
```

Output:

```
Generated Password : aLDfTgYhWbQzXkMn
```

2. Length 20
```bash
python password_generator.py --length 20 --chartype ulds
```

Output:

```
Generated Password : 9A$hQm^pB1d!XcZ&kV2j
```

---

## ⚠️ Error Handling

* If password length < 4:

  ```
  Error : Password length must be at least 4.
  ```
* If `--chartype` is empty or invalid:

  ```
  Error : You must choose at least one character type (ulds).
  ```
