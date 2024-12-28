#You should see something like <map object at 0xd273a8> printed on the console, which is the string representation of the map object returned by map().
#To obtain a readable output you need to turn the map object into a list. Do it by passing the map() call as the argument to the list() function.

test = lambda x: x * 2
print(list(map(test, [2,3,5,8])))