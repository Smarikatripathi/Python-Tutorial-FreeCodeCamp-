#Add a ^ as the first character inside your character class and see what happens.

pattern = '[^a-z]t'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))