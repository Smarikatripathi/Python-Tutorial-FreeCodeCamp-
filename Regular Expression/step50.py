#Now turn your quote string into a single underscore character.

pattern = r'\W'
quote = '_'
print(re.findall(pattern, quote))
