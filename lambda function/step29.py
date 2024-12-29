#Within the filter_expenses_by_category function, replace pass with a lambda function. Use expense as the parameter and evaluate the comparison between the value of the 'category' key of the expense dictionary and category using the equality operator.

def filter_expenses_by_category(expenses, category):
    lambda expense : expense['category']== category