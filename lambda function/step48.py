#After your print() call, you need to filter the expenses and print the filtered list. Declare a variable expenses_from_category and assign it a call to filter_expenses_by_category passing expenses and category as the argument.

lif choice == '4':
    category = input('Enter category to filter: ')
    print(f'\nExpenses for {category}:')
    expenses_from_category = filter_expenses_by_category(expenses, category)