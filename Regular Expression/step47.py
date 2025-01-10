#In a character class, you can combine multiple ranges by writing one range after another inside the square brackets (without any additional characters). For example: [a-d3-6] is the combination of [a-d] and [3-6].
#Now, modify the last regex pattern to match any non-alphanumeric character. Combine the a-z, A-Z, and 0-9 ranges into a single character class and add a ^ as the first character to negate the pattern.

constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, r'[^a-zA-Z0-9]')
        ]        