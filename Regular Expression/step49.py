#Now, turn pattern into the shorthand class for non-alphanumeric characters.

pattern = r'\W'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))