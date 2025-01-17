#Change your list comprehension into a generator expression by removing the square brackets.

        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
            
        ):