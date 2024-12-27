#Use pop() to remove the last element from my_list, then print my_list
my_list = [1, 2]

my_list.append(3)
print(my_list)
my_list.pop()
print(my_list[0])

my_list[0] = 0
print(my_list)

my_list.insert(1, 1)
print(my_list)