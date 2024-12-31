#Inside your if statement, create a variable named category to store the expense category. Assign it a call to input() and use the 'Enter category: ' as the argument.

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