#Once you have the expense details, you need to call the add_expense function to add the new expense to the expenses list.

#After getting the amount and category using input(), call the add_expense function, passing three arguments: expenses, amount and category.

#expenses is the empty list created in the main function earlier in this project.
#amount is the amount of the expense.
#category is the category of the expense


def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')
    if choice == '1':
        amount = float(input('Enter amount: '))
        category = input('Enter category: ')
        add_expense(expenses, amount, category)