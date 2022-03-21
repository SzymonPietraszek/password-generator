import random

def generate_passwords(characters, password_length, number_of_passwords):
    passwords = []
    for pass_numb in range(number_of_passwords):
        password = ""
        for _ in range(password_length):
            password += characters[random.randint(0, len(characters) - 1)]
        passwords.append(password)
    return passwords
