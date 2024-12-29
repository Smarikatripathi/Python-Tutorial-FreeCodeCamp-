#Within the filter_expenses_by_category function, call filter() passing the lambda function you wrote in the previous step as the first argument and the expenses list as the second argument.

def filter_expenses_by_category(expenses, category):
    filter(lambda expense: expense['category'] == category,expenses)