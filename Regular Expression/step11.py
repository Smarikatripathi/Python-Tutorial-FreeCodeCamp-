#Instead of importing random, import the secrets module. Then change the print() call to use secrets.choice(all_characters).

import secrets #generates random numbers for managing important data such as passwords, account authentication, security tokens,
import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)
print(secrets.choice(all_characters))