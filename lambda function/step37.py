#The input() function takes a user input and it returns the user input in the form of a string.
#Inside your while loop, call the input() function passing the string 'Enter your choice: ' as the argument, and assign the result to a variable named choice.

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