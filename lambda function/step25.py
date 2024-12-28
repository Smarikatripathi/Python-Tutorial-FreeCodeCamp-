#In the total_expenses function, you'll now integrate a lambda function. Replace pass with a lambda function that has expense as its parameter.
#expense is expected to be a dictionary, and your lambda function should return the value of the 'amount' key in the expense dictionary.

def total_expenses(expenses):
    lambda expense: expense['amount']
