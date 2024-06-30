import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

print("Generated password:", generate_password(length, use_uppercase, use_digits, use_special))
