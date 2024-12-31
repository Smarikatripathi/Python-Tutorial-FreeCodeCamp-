#inside the if statement, you should ask the user to enter the amount for the expense and store it in a variable.
#Pass the string 'Enter amount: ' to your empty input() call, so you can store the expense.

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
            amount = input('Enter amount: ')