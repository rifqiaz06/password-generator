---

# 🔐 Password Generator

Script sederhana untuk generate password random yang aman dan bisa dikustomisasi berdasarkan jenis karakter. Dibuat dengan Python menggunakan **argparse**.

## ⚡ Features

* Pilih panjang password sesuai kebutuhan
* Pilih jenis karakter yang digunakan:

  * `u` = Uppercase (A-Z)
  * `l` = Lowercase (a-z)
  * `d` = Digits (0-9)
  * `s` = Symbols (punctuation)
* Password selalu mengandung minimal satu karakter dari setiap jenis yang dipilih
* Shuffle otomatis biar password lebih acak

## 🛠️ Installation

Clone repo ini:

```bash
git clone https://github.com/rifqiaz06/password-generator.git
cd password-generator
```

Pastikan sudah install **Python 3.6+** di komputer lo.

## 🚀 Usage

Jalankan script dengan perintah:

```bash
python password_generator.py --length 12 --chartype ulds
```

### Args

* `--length` : Panjang password (minimal 4)
* `--chartype` : Jenis karakter (kombinasi dari `u`, `l`, `d`, `s`)

### Example

```bash
python password_generator.py --length 16 --chartype ul
```

Output:

```
Generated Password : aLDfTgYhWbQzXkMn
```

```bash
python password_generator.py --length 20 --chartype ulds
```

Output:

```
Generated Password : 9A$hQm^pB1d!XcZ&kV2j
```

## ⚠️ Error Handling

* Kalau panjang password < 4:

  ```
  Error : Panjang password minimal adalah 4.
  ```
* Kalau `--chartype` kosong / tidak valid:

  ```
  Error : Anda harus memilih minimal satu jenis karakter (ulds).
  ```

## 📜 License

MIT License – bebas dipake dan dimodifikasi 👍

---
