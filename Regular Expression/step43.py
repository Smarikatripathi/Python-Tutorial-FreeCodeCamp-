#If you need to match a character that has a special meaning in the pattern, such as . or +, you can escape it by prepending a backslash character, \. For example, this matches a literal plus sign: \+.

#Modify pattern so that it matches a single literal dot.

pattern = '\.'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))