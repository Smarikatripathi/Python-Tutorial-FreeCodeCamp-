#To show the total expenses, create an elif statement that checks if choice == '3'.

#If it's true, it means the user wants to see the total expenses. So call print() and pass the string '\nTotal Expenses: ' as the first argument and total_expenses(expenses) as the second argument.

elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        elif choice == '3':    
            print('\nTotal Expenses: ', total_expenses(expenses))