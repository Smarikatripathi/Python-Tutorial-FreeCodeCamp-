#Now, call map() passing your lambda function as the first argument and the expenses list as the second argument.

def total_expenses(expenses):
    map(lambda expense: expense['amount'], expenses)
    