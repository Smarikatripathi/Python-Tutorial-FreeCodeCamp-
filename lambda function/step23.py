#The sum() function returns the sum of the items in the iterable which is passed as its argument. You are going to use sum() together with map() and lambda functions to get the total amount of expenses.
#For now, make a little test and modify your current print() call replacing the list() call with a call to the sum() function passing it the current map() call as the argument.

test = lambda x: x * 2
print(sum(map(test, [2, 3, 5, 8])))