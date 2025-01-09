#Turn your pattern string into a raw string by prefixing it with a r.

pattern = r'\.'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))