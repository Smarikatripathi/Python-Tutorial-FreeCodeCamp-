#Finally, after the for loop, create an if statement to check if count is equal to 4 and break out of the while loop by using the break statement.


        for constraint, pattern in constraints:
            if constraint <= len(re.findall(pattern, password)):
                count += 1
        if count == 4:
            break