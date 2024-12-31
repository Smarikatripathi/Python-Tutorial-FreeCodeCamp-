#Finally, return the result of the filter() call.

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)