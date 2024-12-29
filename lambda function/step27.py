#Finally, pass your map() call to the sum() function to obtain the total expenses and return the result.

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))