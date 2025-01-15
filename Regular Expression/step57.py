#Inside your for loop, compare constraint and the length of the list returned by findall(). Use the <= operator for that.


        for constraint, pattern in constraints:
            constraint<=len(re.findall(pattern, password))