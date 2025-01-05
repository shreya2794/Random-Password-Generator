import random

def generate_password(length):
    # Define sets of consonants, vowels, digits, and symbols
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    digits = '0123456789'
    symbols = '!@#$%^&*'

    # Start with an empty password
    password = ''

    # Ensure alternating between consonants and vowels for easy pronunciation
    for i in range(length - 2):  # Reserve 2 spots for digit and symbol
        if i % 2 == 0:
            password += random.choice(consonants)  # Add a random consonant
        else:
            password += random.choice(vowels)      # Add a random vowel

    # Convert one of the letters to uppercase to ensure there's a capital letter
    random_index = random.randint(0, len(password) - 1)
    password = password[:random_index] + password[random_index].upper() + password[random_index + 1:]

    # Add a random digit and symbol at the end for strength
    password += random.choice(digits)      # Add a random digit
    password += random.choice(symbols)     # Add a random symbol

    return password

# Ask the user for the password length
try:
    length = int(input("Enter the length of the password (at least 6): "))
    if length < 6:
        print("Password length should be at least 6 characters.")
    else:
        # Generate and display the easy-to-remember password
        print("Your password is:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
