#The dot character is a wildcard that matches any character in a string — except for a newline character by default. Modify pattern to match the entire string by replacing the current pattern with a . followed by the + quantifier.

pattern = '.+'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))