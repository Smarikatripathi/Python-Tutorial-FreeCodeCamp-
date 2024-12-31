#Still in the while loop, under the choice variable, write an if statement to check if choice equals the string '1'. If it's true, it will be the starting point for adding a new expense.
#nside the if statement body, declare a variable amount and assign it an empty input() call.

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
           amount = input()
