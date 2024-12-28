#Inside the for loop, replace pass with a print() call and pass it the following f-string: f'Amount: {expense}, Category: {expense}'.

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense}, Category: {expense}')
expenses = []        