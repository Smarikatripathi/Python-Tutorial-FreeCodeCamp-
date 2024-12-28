#You are currently interpolating the expense dictionary in your f-string. Modify the f-string expression to access the value of the 'amount' key and the 'category' key in the expense dictionary.
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

        