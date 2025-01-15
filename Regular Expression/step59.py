#Inside the new conditional statement, increment the count value by 1.

        for constraint, pattern in constraints:
            if constraint <= len(re.findall(pattern, password)):
                count += 1