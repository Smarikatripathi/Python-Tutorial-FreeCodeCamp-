#The amount of the expense needs to be converted before performing any calculation. The float() function takes a string or an integer number as argument and returns a floating point number.
#Pass input('Enter amount: ') to the float() function.

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
            (amount) = float (input('Enter amount: '))