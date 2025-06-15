## Random-Password-Generator 🔐
### Easy-to-Remember Secure Password 

This Python script generates strong, secure, and easy-to-remember passwords by alternating between consonants and vowels, making them pronounceable while maintaining good complexity with the inclusion of digits, symbols, and capital letters.

### Features

- Alternating consonant-vowel pattern for readability and memorability
- Random uppercase letter for password strength
- Appends a digit and a special symbol to increase complexity
- Minimum password length enforcement (6 characters)

### How It Works

1. The user inputs the desired password length.
2. The script ensures that the generated password:
   - Alternates consonants and vowels
   - Contains at least one capital letter
   - Includes one digit and one special character
3. The final password is printed to the console.

### Requirements

- Python 3.x

### Running the Script

python rpg.py

### Sample Output

Enter the length of the password (at least 6): 10
Your password is: Lopeki3!

### File Structure

password_generator.py     # Main script
README.md                 # Project documentation

### ⚠️ Notes

- Minimum password length is 6 characters.
- Randomness means different output on each run.

### 📄 License

This project is open source and free to use.
