#Create an elif clause to check if the user's choice equals the string '2'. Inside the elif clause, print the string '\nAll Expenses:'.

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
    elif choice == '2':
         print('\nAll Expenses:')