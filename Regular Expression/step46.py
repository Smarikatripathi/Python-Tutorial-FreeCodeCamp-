#The character class \d is a shorthand for [0-9]. Replace this character class with the shorthand inside your first constraint tuple.

constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, r'')
        ] 