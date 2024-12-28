#dd another key-value pair to the dictionary you are appending to the expense list. Use the string 'category' as the key, and the category parameter as the value.
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount,'category' : category})
    expenses = []