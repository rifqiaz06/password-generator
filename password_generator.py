import argparse
import random
import string
import sys

def generate_password(length, chartype):
    if length < 4:
        print("Error : Panjang password minimal adalh 4.")
        sys.exit(1)

    char_list = ""
    password = []

    if "u" in chartype:
        char_list += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if "l" in chartype:
        char_list += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if "d" in chartype:
        char_list += string.digits
        password.append(random.choice(string.digits))
    if "s" in chartype:
        char_list += string.punctuation
        password.append(random.choice(string.punctuation))
    
    if char_list == "":
        print("Error : Anda harus memilih minimal satu jenis karakter (ulds).")
        sys.exit(1)
    
    # Menambahkan sisa karakter secara acak
    password += random.choices(char_list, k = length - len(password))
    random.shuffle(password)

    return "".join(password)



parser = argparse.ArgumentParser(description="Password Generator")
parser.add_argument("--length", type=int, required=True, help="Panjang Password")
parser.add_argument("--chartype", type=str, required=True, help="Jenis karakter (u=uppercase, l=lowercase, d=digits, s=symbol)")

args = parser.parse_args()
password = generate_password(args.length, args.chartype)
print(f"Generated Password : {password}")