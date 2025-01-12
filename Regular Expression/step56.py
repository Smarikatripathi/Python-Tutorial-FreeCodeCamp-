#pass your existent findall() call to the len() function.

        for constraint, pattern in constraints:
            len(re.findall(pattern, password))
