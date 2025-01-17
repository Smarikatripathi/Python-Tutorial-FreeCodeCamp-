#Right now, all() is taking an empty list as the argument. Populate that empty list using the comprehension syntax so that the list stores the results of evaluating the expression constraint <= len(re.findall(pattern, password)) for each constraint-pattern tuple in the constraints list.

#In this way, you'll break out of the while loop only after all the requirements are fulfilled.

        if all([
            constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ]):