#Modify your pattern variable to match any letter t preceded by a lowercase letter in the quote variable. Use the range of characters from a to z for that.

import re
import secrets
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, '[0123456789]')
        ]        

    return password
    
# new_password = generate_password(8)
# print(new_password)
pattern = '[a-z]t'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))