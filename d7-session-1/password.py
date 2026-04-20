import random
import string


def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password


print("--- Random Password Generator ---")

length = int(input("Enter password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
use_digits = input("Include digits? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

password = generate_password(length, use_upper, use_digits, use_symbols)
print("Generated password:", password)
