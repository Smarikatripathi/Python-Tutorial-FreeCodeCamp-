#Inside the for loop, call the findall() function passing pattern and password as the arguments.

        for constraint, pattern in constraints:
            re.findall(pattern, password)